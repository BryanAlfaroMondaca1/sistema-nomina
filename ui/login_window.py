import tkinter as tk
from tkinter import messagebox
from modules.auth import AuthService

class LoginWindow:  # ¡El nombre de la clase debe coincidir exactamente!
    def __init__(self, master):
        self.master = master
        master.title("Login - Sistema de Nómina")

        tk.Label(master, text="Usuario:").pack()
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        tk.Label(master, text="Contraseña:").pack()
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        tk.Button(master, text="Ingresar", command=self.login).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        rol = AuthService().login(username, password)
        if rol:
            messagebox.showinfo("Éxito", f"Bienvenido (Rol: {rol})")
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")