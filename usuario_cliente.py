import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mercado_digital"
    )

def abrir_interfaz_usuario(nombre_usuario, root_principal=None):
    ventana = tk.Toplevel() if root_principal else tk.Tk()
    ventana.title("Panel del Cliente")
    ventana.geometry("1100x600")
    ventana.configure(bg="#f5f5f5")

    def cerrar_sesion():
        ventana.destroy()
        if root_principal:
            root_principal.deiconify()
            root_principal.state("zoomed")  # Mantiene la ventana maximizada

    btn_cerrar = tk.Button(ventana, text="Cerrar sesión", command=cerrar_sesion,
                           bg="#f44336", fg="white", font=("Helvetica", 12, "bold"))
    btn_cerrar.pack(anchor="ne", padx=20, pady=10)

    # Estilo para Treeview
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#e3f2fd", foreground="black", rowheight=30, fieldbackground="#e3f2fd", font=("Helvetica", 12))
    style.configure("Treeview.Heading", background="#1976d2", foreground="white", font=("Helvetica", 13, "bold"))
    style.map("Treeview", background=[("selected", "#90caf9")])

    tk.Label(ventana, text=f"Bienvenido, {nombre_usuario}", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#1976d2").pack(pady=15)

    frame_productos = tk.Frame(ventana, bg="#f5f5f5")
    frame_productos.pack(padx=10, pady=10, fill="both", expand=True)

    columnas = ("ID", "Nombre", "Descripción", "Precio", "Stock")
    tabla_productos = ttk.Treeview(frame_productos, columns=columnas, show="headings", height=12)
    for col in columnas:
        tabla_productos.heading(col, text=col)
        tabla_productos.column(col, width=180 if col == "Descripción" else 110, anchor="center")
    tabla_productos.pack(side="left", fill="both", expand=True, padx=(0, 10))

    # Scrollbar
    scrollbar = ttk.Scrollbar(frame_productos, orient="vertical", command=tabla_productos.yview)
    tabla_productos.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="left", fill="y")

    def cargar_productos():
        for row in tabla_productos.get_children():
            tabla_productos.delete(row)
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("SELECT Cod_Producto, Nombre, Descripcion, Precio, cantidad FROM producto")
            productos = cursor.fetchall()
            for producto in productos:
                tabla_productos.insert("", tk.END, values=producto)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    cargar_productos()

    # Frame para cantidad y botón
    frame_accion = tk.Frame(ventana, bg="#f5f5f5")
    frame_accion.pack(pady=10)

    tk.Label(frame_accion, text="Cantidad:", font=("Helvetica", 12), bg="#f5f5f5").pack(side="left")
    entry_cantidad = tk.Entry(frame_accion, width=5, font=("Helvetica", 12))
    entry_cantidad.pack(side="left", padx=5)

    def agregar_al_carrito():
        seleccionado = tabla_productos.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Selecciona un producto.")
            return
        cantidad = entry_cantidad.get()
        if not cantidad.isdigit() or int(cantidad) <= 0:
            messagebox.showerror("Error", "Ingresa una cantidad válida.")
            return
        producto = tabla_productos.item(seleccionado, "values")
        producto_id = producto[0]
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO carrito_item (Id_usuario, Producto_Id, Cantidad) VALUES ((SELECT Id FROM usuario WHERE Nombre = %s LIMIT 1), %s, %s)",
                           (nombre_usuario, producto_id, cantidad))
            conn.commit()
            messagebox.showinfo("Éxito", "Producto agregado al carrito.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    btn_agregar = tk.Button(frame_accion, text="Agregar al carrito", command=agregar_al_carrito, bg="#1976d2", fg="white", font=("Helvetica", 12, "bold"))
    btn_agregar.pack(side="left", padx=10)

    # Permitir doble clic para agregar rápido
    def on_double_click(event):
        agregar_al_carrito()
    tabla_productos.bind("<Double-1>", on_double_click)

    ventana.mainloop()