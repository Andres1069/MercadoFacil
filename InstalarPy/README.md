
# Mercado Fácil

Aplicación de escritorio en Python con interfaz gráfica para gestionar usuarios (clientes y administradores) y conectarse a una base de datos MySQL.

## 🧰 Requisitos

- Python 3.10 o superior
- MySQL instalado (puede ser con XAMPP, WAMP, etc.)
- Base de datos `mercado_digital` importada

## 🛠 Instalación

1. **Clona el repositorio o descarga el ZIP**

```bash
git clone https://github.com/tu-usuario/mercado-facil.git
cd mercado-facil
```

2. **Instala Python si no lo tienes**  
Descárgalo desde: https://www.python.org/downloads/  
Asegúrate de marcar la casilla “Add Python to PATH” durante la instalación.

3. **Instala las dependencias necesarias**

```bash
pip install -r requirements.txt
```

4. **Importa la base de datos**

- Abre phpMyAdmin o el cliente de MySQL
- Crea una base de datos llamada `mercado_digital`
- Importa el archivo `mercado_digital.sql` incluido en el repositorio

5. **Ejecuta la aplicación**

```bash
python iniciosesion.py
```

## 🖼 Características

- Login con validación contra base de datos
- Registro de nuevos usuarios (clientes)
- Panel de administración con funciones para crear, editar y eliminar usuarios
- Cierre de sesión sin cerrar la aplicación

## 📁 Estructura recomendada

```
mercado-facil/
├── iniciosesion.py
├── usuario_admin.py
├── mercado_digital.sql
├── requirements.txt
├── README.md
└── img/
    └── fondo.jpg
```

## 🧑‍💻 Autor

Raúl González
