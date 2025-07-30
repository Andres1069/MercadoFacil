import tkinter as tk
from tkinter import messagebox
import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Cambia si tienes contraseña
        database="mercado_digital"
    )

def registrar_usuario():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    contrasena = entry_contrasena.get()
    rol = entry_rol.get()

    if not nombre or not correo or not contrasena or not rol:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuario (Nombre, Correo, Contraseña, Rol) VALUES (%s, %s, %s, %s)",
            (nombre, correo, contrasena, rol)
        )
        conn.commit()
        messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
        entry_nombre.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        entry_contrasena.delete(0, tk.END)
        entry_rol.delete(0, tk.END)
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", str(err))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

root = tk.Tk()
root.title("Registro de Usuario")

tk.Label(root, text="Nombre:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Correo:").pack()
entry_correo = tk.Entry(root)
entry_correo.pack()

tk.Label(root, text="Contraseña:").pack()
entry_contrasena = tk.Entry(root, show="*")
entry_contrasena.pack()

tk.Label(root, text="Rol:").pack()
entry_rol = tk.Entry(root)
entry_rol.pack()

tk.Button(root, text="Registrar", command=registrar_usuario).pack(pady=10)

root.mainloop()