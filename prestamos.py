import json
from usuarios import archivo_usuarios
from libros import archivo_libros
from datetime import datetime

ARCHIVO_DATOS = "biblioteca_python.json" 

# Función para cargar la información de préstamos
def cargar_datos():
    try:
        with open(ARCHIVO_DATOS, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"prestamos": []}

# Función para guardar datos
def guardar_datos(datos):
    with open(ARCHIVO_DATOS, "w") as archivo:
         json.dump(datos, archivo, indent=4)

# Registro de préstamos
def registrar_prestamos(usuario, libro):
    if not usuario_existe(usuario):
        print(f"Error: El usuario '{usuario}' no está registrado.")
        return
    if not libro_existe(libro):
        print(f"Error: El libro '{libro}' no existe en el catálogo.")
        return

    datos = cargar_datos()
    # Verificamos que el libro no esté prestado
    for prestamo in datos["prestamos"]:
        if prestamo["libro"] == libro and prestamo["estado"] == "prestado":
            print(f"Error: El libro '{libro}' ya está prestado.")
            return

    prestamo = {
        "usuario": usuario,
        "libro": libro,
        "fecha_prestamo": datetime.now().strftime("%Y-%m-%d"),
        "estado": "prestado"
    }
    datos["prestamos"].append(prestamo)
    guardar_datos(datos)
    print(f"Préstamo registrado: {usuario} eligió '{libro}'.")

# Mostrar los préstamos registrados
def mostrar_prestamos():
    datos = cargar_datos()
    if datos["prestamos"]:
        print("\nLista de Préstamos:")
        for i, prestamo in enumerate(datos["prestamos"], start=1):
            print(
                f"{i}. Usuario: {prestamo['usuario']}, Libro: {prestamo['libro']}, "
                f"Fecha: {prestamo['fecha_prestamo']}, Estado: {prestamo['estado']}"
            )
    else:
        print("No hay préstamos registrados.")

# Devolver un libro prestado
def devolver_libro(usuario, libro):
    if not usuario_existe(usuario):
        print(f"Error: El usuario '{usuario}' no está registrado.")
        return 
    if not libro_existe(libro):
        print(f"Error: El libro '{libro}' no existe en el catálogo.")
        return
    datos = cargar_datos()
    for prestamo in datos["prestamos"]:
        if prestamo["usuario"] == usuario and prestamo["libro"] == libro and prestamo["estado"] == "prestado":
            prestamo["estado"] = "devuelto"
            prestamo["fecha_devolucion"] = datetime.now().strftime("%Y-%m-%d")
            guardar_datos(datos)
            print(f"Libro '{libro}' devuelto por {usuario}.")
            return
    print("Error: No se encontró un préstamo activo para este usuario y libro.")

# Función para seleccionar un usuario de listado 
def seleccionar_usuario():
    try:
        with open("usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
        return None

    if not usuarios:
        print("No hay usuarios registrados.")
        return None

    print("Seleccione un usuario:")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. {usuario}")

    opcion = input("Ingrese el número del usuario: ")
    try:
        opcion = int(opcion)
        if 1 <= opcion <= len(usuarios):
            return usuarios[opcion - 1]
        else:
            print("Opción inválida.")
            return None
    except ValueError:
        print("Entrada inválida. Se esperaba un número.")
        return None

# Función para seleccionar un libro de listado 
def seleccionar_libro():
    try:
        with open("libros.json", "r") as archivo:
            libros = json.load(archivo)
    except FileNotFoundError:
        print("No se encontró el archivo de libros.")
        return None

    if not libros:
        print("No hay libros registrados.")
        return None

    print("Seleccione un libro:")
    for i, libro in enumerate(libros, start=1):
        print(f"{i}. {libro}")

    opcion = input("Ingrese el número del libro: ")
    try:
        opcion = int(opcion)
        if 1 <= opcion <= len(libros):
            return libros[opcion - 1]
        else:
            print("Opción inválida.")
            return None
    except ValueError:
        print("Entrada inválida. Se esperaba un número.")
        return None

# Menú para registrar un préstamo 
def menu_registrar_prestamo():
    usuario = seleccionar_usuario()
    if usuario is None:
        return

    libro = seleccionar_libro()
    if libro is None:
        return

    registrar_prestamos(usuario, libro)

if __name__ == "__main__":
    menu_registrar_prestamo()


