import json
import os
from datetime import datetime

from usuarios import archivo_usuarios
from libros import archivo_libros

archivo_prestamos = 'prestamos.json'


# Cargar datos de préstamos
def cargar_prestamos():
    if os.path.exists(archivo_prestamos):
        with open(archivo_prestamos, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Guardar préstamos
def guardar_prestamos(prestamos):
    with open(archivo_prestamos, 'w', encoding='utf-8') as f:
        json.dump(prestamos, f, indent=4, ensure_ascii=False)

# Función para registrar un préstamo
def registrar_prestamo():
    usuario = seleccionar_usuario()
    if not usuario:
        return

    libro = seleccionar_libro()
    if not libro:
        return

    if libro['prestado']:
        print(f"El libro '{libro['titulo']}' ya está prestado.")
        return

    prestamos = cargar_prestamos()
    nuevo_prestamo = {
        "socio": usuario["socio"],
        "nombre": f"{usuario['nombre']} {usuario['apellido']}",
        "titulo_libro": libro["titulo"],
        "fecha_prestamo": datetime.now().strftime("%Y-%m-%d"),
        "estado": "prestado"
    }
    prestamos.append(nuevo_prestamo)

    # Marcar el libro como prestado
    libro['prestado'] = True
    libro['socio_prestamo'] = usuario["socio"]

    guardar_prestamos(prestamos)
    actualizar_libros()
    print(f"Préstamo registrado para {usuario['nombre']} - Libro: '{libro['titulo']}'")

# Mostrar préstamos
def mostrar_prestamos():
    prestamos = cargar_prestamos()
    if not prestamos:
        print("No hay préstamos registrados.")
        return
    print("\nLista de Préstamos:")
    for p in prestamos:
        estado = p["estado"]
        linea = f"Socio {p['socio']} - {p['nombre']} → '{p['titulo_libro']}' el {p['fecha_prestamo']} - Estado: {estado}"
        if estado == "devuelto":
            linea += f" (Devolución: {p['fecha_devolucion']})"
        print(linea)

# Devolver libro
def devolver_libro():
    prestamos = cargar_prestamos()
    socio = input("Ingrese número de socio: ")
    titulo = input("Ingrese título del libro: ")

    for prestamo in prestamos:
        if str(prestamo["socio"]) == socio and prestamo["titulo_libro"].lower() == titulo.lower() and prestamo["estado"] == "prestado":
            prestamo["estado"] = "devuelto"
            prestamo["fecha_devolucion"] = datetime.now().strftime("%Y-%m-%d")

            # Actualizar en libros.json
            actualizar_estado_libro(titulo, False, None)

            guardar_prestamos(prestamos)
            print(f"Libro '{titulo}' devuelto correctamente.")
            return

    print("No se encontró un préstamo activo con esos datos.")

# ----------- Auxiliares ------------

def seleccionar_usuario():
    if not os.path.exists(archivo_usuarios):
        print("Archivo de usuarios no encontrado.")
        return None
    with open(archivo_usuarios, 'r', encoding='utf-8') as f:
        usuarios = json.load(f)

    if not usuarios:
        print("No hay usuarios registrados.")
        return None

    print("\nUsuarios:")
    for u in usuarios:
        print(f"{u['socio']}: {u['nombre']} {u['apellido']}")

    try:
        socio = int(input("Ingrese el número de socio: "))
        for u in usuarios:
            if u["socio"] == socio:
                return u
        print("No se encontró ese número de socio.")
    except ValueError:
        print("Número inválido.")
    return None

def seleccionar_libro():
    if not os.path.exists(archivo_libros):
        print("Archivo de libros no encontrado.")
        return None
    with open(archivo_libros, 'r', encoding='utf-8') as f:
        libros = json.load(f)

    if not libros:
        print("No hay libros disponibles.")
        return None

    print("\nLibros:")
    for i, libro in enumerate(libros, start=1):
        estado = " (PRESTADO)" if libro.get("prestado") else ""
        print(f"{i}. {libro['titulo']} - {libro['autor']}{estado}")

    try:
        opcion = int(input("Ingrese el número del libro: ")) - 1
        if 0 <= opcion < len(libros):
            return libros[opcion]
    except ValueError:
        pass
    print("Selección inválida.")
    return None

def actualizar_libros():
    with open(archivo_libros, 'r', encoding='utf-8') as f:
        libros = json.load(f)
    with open(archivo_libros, 'w', encoding='utf-8') as f:
        json.dump(libros, f, indent=4, ensure_ascii=False)

def actualizar_estado_libro(titulo, prestado, socio_prestamo):
    with open(archivo_libros, 'r', encoding='utf-8') as f:
        libros = json.load(f)
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            libro["prestado"] = prestado
            libro["socio_prestamo"] = socio_prestamo
            break
    with open(archivo_libros, 'w', encoding='utf-8') as f:
        json.dump(libros, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    registrar_prestamo()
