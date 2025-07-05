import sqlite3

def get_db_connection():
    return sqlite3.connect("database/nomina.db")  # La BD se creará automáticamente