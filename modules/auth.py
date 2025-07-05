from database.db_connection import get_db_connection

class AuthService:
    def login(self, username, password):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Crear tabla de usuarios si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                rol TEXT NOT NULL
            )
        """)
        
        # Insertar datos de prueba (solo una vez)
        cursor.execute("INSERT OR IGNORE INTO usuarios VALUES (?, ?, ?)", ("admin", "1234", "admin"))
        cursor.execute("INSERT OR IGNORE INTO usuarios VALUES (?, ?, ?)", ("rrhh", "1234", "rrhh"))
        cursor.execute("INSERT OR IGNORE INTO usuarios VALUES (?, ?, ?)", ("empleado1", "1234", "trabajador"))
        conn.commit()
        
        # Validar credenciales
        cursor.execute("SELECT rol FROM usuarios WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None