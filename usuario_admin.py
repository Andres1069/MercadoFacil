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

def abrir_interfaz_admin(nombre_admin, master):
    ventana = tk.Toplevel(master)
    ventana.title("Panel de Administrador")
    ventana.state("zoomed")
    ventana.configure(bg="#f4f6fb")

    # Estilo moderno para Treeview y botones
    style = ttk.Style(ventana)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="#eaf1fb",
                    foreground="#222",
                    rowheight=32,
                    fieldbackground="#eaf1fb",
                    font=("Segoe UI", 12))
    style.configure("Treeview.Heading",
                    background="#1976d2",
                    foreground="white",
                    font=("Segoe UI", 13, "bold"))
    style.map("Treeview", background=[("selected", "#bbdefb")])
    style.configure("TButton",
                    font=("Segoe UI", 11, "bold"),
                    padding=8,
                    borderwidth=0)
    style.configure("TEntry",
                    font=("Segoe UI", 11),
                    padding=6)

    # Alternar color de filas
    style.map('Treeview', background=[('selected', '#90caf9')])
    style.layout("TButton", [('Button.padding', {'children': [('Button.label', {'sticky': 'nswe'})]})])

    tk.Label(ventana, text=f"Bienvenido, {nombre_admin} (Administrador)",
             font=("Segoe UI", 20, "bold"), bg="#f4f6fb", fg="#1976d2").pack(pady=20)

    columnas = ("ID", "Documento", "Nombre", "Apellido", "Correo", "Teléfono", "Barrio", "Dirección", "Rol")
    tree = ttk.Treeview(ventana, columns=columnas, show="headings", selectmode="browse")
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=140 if col != "Dirección" else 200, anchor="center")
    tree.pack(pady=10, fill="both", expand=True, padx=30)

    # Scrollbar moderno
    scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.place(relx=0.98, rely=0.13, relheight=0.7)

    def cargar_usuarios():
        for i in tree.get_children():
            tree.delete(i)
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("SELECT Id, Num_Doc, Nombre, Apellido, Correo, Telefono, Barrio, Direccion, Rol FROM usuario")
            for idx, usuario in enumerate(cursor.fetchall()):
                tag = "evenrow" if idx % 2 == 0 else "oddrow"
                tree.insert("", tk.END, values=usuario, tags=(tag,))
        except mysql.connector.Error as err:
            messagebox.showerror("Error", str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
        tree.tag_configure('evenrow', background='#eaf1fb')
        tree.tag_configure('oddrow', background='#f4f6fb')

    cargar_usuarios()

    # Formulario moderno
    formulario = tk.Frame(ventana, bg="#f4f6fb")
    formulario.pack(fill="x", pady=10, padx=30)

    campos = ["Num_Doc", "Nombre", "Apellido", "Correo", "Telefono", "Barrio", "Direccion", "Rol"]
    entradas = {}

    for i, campo in enumerate(campos):
        tk.Label(formulario, text=campo + ":", bg="#f4f6fb", font=("Segoe UI", 11)).grid(row=i // 4, column=(i % 4) * 2, padx=5, pady=8, sticky="e")
        entry = ttk.Entry(formulario, width=18)
        entry.grid(row=i // 4, column=(i % 4) * 2 + 1, padx=5, pady=8, sticky="w")
        entradas[campo.lower()] = entry

    def limpiar_formulario():
        for campo in entradas.values():
            campo.delete(0, tk.END)

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

    # SOLO este bloque de botones (elimina el anterior)
    botones_frame = tk.Frame(ventana, bg="#f4f6fb")
    botones_frame.pack(pady=20)

    ttk.Button(botones_frame, text="Nuevo", command=limpiar_formulario, style="TButton").pack(side="left", padx=10)
    ttk.Button(botones_frame, text="Crear", command=crear_usuario, style="TButton").pack(side="left", padx=10)
    ttk.Button(botones_frame, text="Editar", command=editar_usuario, style="TButton").pack(side="left", padx=10)
    ttk.Button(botones_frame, text="Eliminar", command=eliminar_usuario, style="TButton").pack(side="left", padx=10)
    ttk.Button(botones_frame, text="Cerrar Sesión", command=cerrar_sesion, style="TButton").pack(side="left", padx=10)

    ventana.mainloop()