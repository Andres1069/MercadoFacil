import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ==============================
# CONEXIÓN BASE DE DATOS
# ==============================
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mercado_digital"
    )

# ==============================
# PANEL DEL ADMINISTRADOR (como ventana secundaria)
# ==============================
def abrir_interfaz_admin(nombre_admin, master):
    ventana = tk.Toplevel(master)
    ventana.title("Panel de Administrador")
    ventana.geometry("1000x500")
    ventana.configure(bg="#f4f4f4")

    titulo = tk.Label(ventana, text=f"Bienvenido, {nombre_admin} (Administrador)",
                      font=("Helvetica", 16, "bold"), bg="#f4f4f4")
    titulo.pack(pady=10)

    columnas = ("ID", "Documento", "Nombre", "Apellido", "Correo", "Teléfono", "Barrio", "Dirección", "Rol")
    tree = ttk.Treeview(ventana, columns=columnas, show="headings")
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=120)
    tree.pack(pady=10, fill="both", expand=True)

    def cargar_usuarios():
        for i in tree.get_children():
            tree.delete(i)
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("SELECT Id, Num_Doc, Nombre, Apellido, Correo, Telefono, Barrio, Direccion, Rol FROM usuario")
            for usuario in cursor.fetchall():
                tree.insert("", tk.END, values=usuario)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    cargar_usuarios()

    formulario = tk.Frame(ventana, bg="#e8e8e8", pady=10)
    formulario.pack(fill="x")

    campos = ["Num_Doc", "Nombre", "Apellido", "Correo", "Telefono", "Barrio", "Direccion", "Rol"]
    entradas = {}

    for i, campo in enumerate(campos):
        tk.Label(formulario, text=campo + ":", bg="#e8e8e8").grid(row=i // 3, column=(i % 3) * 2, padx=5, pady=3)
        entry = tk.Entry(formulario, width=20)
        entry.grid(row=i // 3, column=(i % 3) * 2 + 1, padx=5, pady=3)
        entradas[campo.lower()] = entry

    def crear_usuario():
        datos = {k: v.get().strip() for k, v in entradas.items()}
        if "" in datos.values():
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO usuario (Id, Num_Doc, Nombre, Apellido, Correo, Contraseña, Telefono, Barrio, Direccion, Rol)
                VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                datos["num_doc"], datos["nombre"], datos["apellido"], datos["correo"],
                datos["contraseña"], datos["telefono"], datos["barrio"],
                datos["direccion"], datos["rol"]
            ))
            conn.commit()
            cargar_usuarios()
            messagebox.showinfo("Éxito", "Usuario creado correctamente.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def eliminar_usuario():
        seleccionado = tree.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Selecciona un usuario.")
            return
        valores = tree.item(seleccionado, "values")
        id_usuario = valores[0]
        confirm = messagebox.askyesno("Confirmar", f"¿Eliminar usuario ID {id_usuario}?")
        if confirm:
            try:
                conn = conectar_bd()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM usuario WHERE Id = %s", (id_usuario,))
                conn.commit()
                cargar_usuarios()
                messagebox.showinfo("Eliminado", "Usuario eliminado correctamente.")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", str(err))
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()

    def editar_usuario():
        seleccionado = tree.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Selecciona un usuario.")
            return
        valores = tree.item(seleccionado, "values")
        id_usuario = valores[0]
        datos = {k: v.get().strip() for k, v in entradas.items()}
        if "" in datos.values():
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE usuario SET Num_Doc=%s, Nombre=%s, Apellido=%s, Correo=%s,
                Contraseña=%s, Telefono=%s, Barrio=%s, Direccion=%s, Rol=%s WHERE Id=%s
            """, (
                datos["num_doc"], datos["nombre"], datos["apellido"], datos["correo"],
                datos["contraseña"], datos["telefono"], datos["barrio"],
                datos["direccion"], datos["rol"], id_usuario
            ))
            conn.commit()
            cargar_usuarios()
            messagebox.showinfo("Actualizado", "Usuario actualizado correctamente.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def cargar_en_formulario(event):
        seleccionado = tree.focus()
        if seleccionado:
            valores = tree.item(seleccionado, "values")
            keys = list(entradas.keys())
            for i in range(1, len(keys) + 1):
                entradas[keys[i - 1]].delete(0, tk.END)
                entradas[keys[i - 1]].insert(0, valores[i])

    tree.bind("<<TreeviewSelect>>", cargar_en_formulario)

    def cerrar_sesion():
        ventana.destroy()
        master.deiconify()

    botones_frame = tk.Frame(ventana, bg="#f4f4f4")
    botones_frame.pack(pady=10)

    tk.Button(botones_frame, text="Crear Usuario", command=crear_usuario,
              bg="#4CAF50", fg="white", width=15).pack(side="left", padx=5)

    tk.Button(botones_frame, text="Editar Usuario", command=editar_usuario,
              bg="#2196F3", fg="white", width=15).pack(side="left", padx=5)

    tk.Button(botones_frame, text="Eliminar Usuario", command=eliminar_usuario,
              bg="#f44336", fg="white", width=15).pack(side="left", padx=5)

    tk.Button(botones_frame, text="Cerrar Sesión", command=cerrar_sesion,
              bg="#9E9E9E", fg="white", width=15).pack(side="left", padx=5)
