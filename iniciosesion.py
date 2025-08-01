import tkinter as tk
import usuario_admin
import usuario_cliente  # <-- Agrega esta línea
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# =========================
# CONEXIÓN A LA BASE DE DATOS
# =========================
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mercado_digital"
    )

# =========================
# FUNCIÓN LOGIN
# =========================
def iniciar_sesion():
    correo = entry_correo.get()
    contrasena = entry_contrasena.get()

    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT Nombre, Rol FROM usuario WHERE Correo = %s AND Contraseña = %s", (correo, contrasena))
        resultado = cursor.fetchone()

        if resultado:
            nombre, rol = resultado
            if rol.lower() == "administrador":
                root.withdraw()  # Oculta ventana principal
                usuario_admin.abrir_interfaz_admin(nombre, root)
            else:
                root.withdraw()  # Oculta ventana principal
                usuario_cliente.abrir_interfaz_usuario(nombre, root)
        else:
            messagebox.showerror("Error", "Correo o contraseña incorrectos.")

    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", str(err))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
# =========================
# CERRAR SESIÓN
# =========================
def cerrar_sesion():
    bienvenida_frame.pack_forget()
    entry_correo.delete(0, tk.END)
    entry_contrasena.delete(0, tk.END)
    mostrar_menu_principal()

# =========================
# FUNCIONES DE NAVEGACIÓN ENTRE FRAMES
# =========================
def ocultar_todos_los_frames():
    for frame in (menu_frame, login_frame, registro_frame, bienvenida_frame):
        frame.pack_forget()

def mostrar_menu_principal():
    ocultar_todos_los_frames()
    menu_frame.pack(expand=True)

def mostrar_login():
    ocultar_todos_los_frames()
    login_frame.pack(expand=True)

def mostrar_registro():
    ocultar_todos_los_frames()
    registro_frame.pack(expand=True)

def mostrar_bienvenida(nombre, rol):
    ocultar_todos_los_frames()
    label_bienvenida.config(text=f"Bienvenido, {nombre} ({rol})")
    bienvenida_frame.pack()

# =========================
# CONFIGURAR INTERFAZ
# =========================
root = tk.Tk()
root.title("Ingreso al Sistema")
root.geometry("400x300")
root.state("zoomed")
root.resizable(True, True)
root.configure(bg="#f0f0f0")

# ======== ESTILOS =========
fuente_titulo = ("Helvetica", 18, "bold")
fuente_normal = ("Helvetica", 12)
color_fondo = "#ffffff"
color_boton = "#4CAF50"
color_boton_texto = "#ffffff"

# ======== IMAGEN DE FONDO =========
ruta = r"C:\\xampp\\htdocs\\MercadoFacil\\img\\fondo.jpg"

imagen_fondo = Image.open(ruta)
imagen_fondo = imagen_fondo.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
fondo = ImageTk.PhotoImage(imagen_fondo)

fondo_label = tk.Label(root, image=fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# ======== FRAME MENU PRINCIPAL =========
menu_frame = tk.Frame(root, bg=color_fondo, padx=20, pady=20)

titulo_menu = tk.Label(menu_frame, text="Bienvenido a Mercado Fácil", font=fuente_titulo, bg=color_fondo)
titulo_menu.pack(pady=20)

btn_ir_login = tk.Button(menu_frame, text="Iniciar Sesión", font=fuente_normal,
                         bg=color_boton, fg=color_boton_texto, width=20, command=mostrar_login)
btn_ir_login.pack(pady=10)

btn_ir_registro = tk.Button(menu_frame, text="Registrarse", font=fuente_normal,
                            bg="#2196F3", fg="#ffffff", width=20, command=mostrar_registro)
btn_ir_registro.pack(pady=10)

# ======== FRAME LOGIN =========
login_frame = tk.Frame(root, bg=color_fondo, padx=20, pady=20)

titulo = tk.Label(login_frame, text="Iniciar Sesión", font=fuente_titulo, bg=color_fondo)
titulo.pack(pady=10)

label_correo = tk.Label(login_frame, text="Correo:", font=fuente_normal, bg=color_fondo)
label_correo.pack(pady=(10, 0))
entry_correo = tk.Entry(login_frame, font=fuente_normal, width=30)
entry_correo.pack(pady=5)

label_contrasena = tk.Label(login_frame, text="Contraseña:", font=fuente_normal, bg=color_fondo)
label_contrasena.pack(pady=(10, 0))
entry_contrasena = tk.Entry(login_frame, font=fuente_normal, show="*", width=30)
entry_contrasena.pack(pady=5)

boton_login = tk.Button(login_frame, text="Ingresar", command=iniciar_sesion, font=fuente_normal,
                        bg=color_boton, fg=color_boton_texto, width=15)
boton_login.pack(pady=20)

# ======== FRAME BIENVENIDA =========
bienvenida_frame = tk.Frame(root, bg=color_fondo, padx=20, pady=20)

label_bienvenida = tk.Label(bienvenida_frame, text="", font=fuente_titulo, bg=color_fondo)
label_bienvenida.pack(pady=20)

boton_logout = tk.Button(bienvenida_frame, text="Cerrar sesión", command=cerrar_sesion, font=fuente_normal,
                         bg="#f44336", fg="#ffffff", width=15)
boton_logout.pack()

# ======== FRAME REGISTRO =========
registro_frame = tk.Frame(root, bg=color_fondo, padx=20, pady=20)

titulo_registro = tk.Label(registro_frame, text="Registro de Usuario", font=fuente_titulo, bg=color_fondo)
titulo_registro.pack(pady=10)

labels_campos = ["Número de Documento", "Nombre", "Apellido", "Correo", "Contraseña", "Teléfono", "Barrio", "Dirección"]
entradas = {}

for campo in labels_campos:
    lbl = tk.Label(registro_frame, text=campo + ":", font=fuente_normal, bg=color_fondo)
    lbl.pack(pady=(5, 0))
    entry = tk.Entry(registro_frame, font=fuente_normal, width=30, show="*" if campo == "Contraseña" else "")
    entry.pack(pady=5)
    entradas[campo.lower()] = entry

def registrar_usuario():
    datos = {k: v.get().strip() for k, v in entradas.items()}
    if "" in datos.values():
        messagebox.showerror("Error", "Por favor completa todos los campos.")
        return

    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO usuario (Id, Num_Doc, Nombre, Apellido, Contraseña, Telefono, Correo, Barrio, Direccion, Rol)
            VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, 'Cliente')
        """, (
            datos["número de documento"], datos["nombre"], datos["apellido"], datos["contraseña"], datos["teléfono"],
            datos["correo"], datos["barrio"], datos["dirección"]
        ))
        conn.commit()
        messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
        mostrar_login()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo registrar: {err}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

btn_registrar = tk.Button(registro_frame, text="Registrar", font=fuente_normal, bg=color_boton,
                          fg=color_boton_texto, command=registrar_usuario, width=20)
btn_registrar.pack(pady=15)

btn_volver = tk.Button(registro_frame, text="Volver al Menú", font=fuente_normal,
                       bg="#f44336", fg="#ffffff", command=mostrar_menu_principal, width=20)
btn_volver.pack()

# ======== INICIAR EN EL MENÚ PRINCIPAL =========
mostrar_menu_principal()
root.mainloop()