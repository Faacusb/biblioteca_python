import json
from datetime import datetime

ARCHIVO_DATOS = "biblioteca_python.json"

# Función para cargar la información
def cargar_datos():
    try:
        with open(ARCHIVO_DATOS, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
      # Estructura de datos inicial
        return {"prestamos": [], "reservas": []}

# Función para guardar datos
def guardar_datos(datos):
    with open(ARCHIVO_DATOS, "w") as archivo:
        json.dump(datos, archivo, indent=4)

# Registros de prestamos
def registrar_prestamos(usuario, libro):
    datos = cargar_datos()
    # Verificar si el libro está prestado
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

# Mosrtrar prestamos
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
# Devolver libro
def devolver_libro(usuario, libro):
    datos = cargar_datos()
    for prestamo in datos["prestamos"]:
        if prestamo["usuario"] == usuario and prestamo["libro"] == libro and prestamo["estado"] == "prestado":
            prestamo["estado"] = "devuelto"
            prestamo["fecha_devolucion"] = datetime.now().strftime("%Y-%m-%d")
            guardar_datos(datos)
            print(f"Libro '{libro}' devuelto por {usuario}.")
    print("Error: No se encontró un préstamo activo para este usuario y libro.")

# Registros de reservas 
def registrar_reservas(usuario, libro):
    datos = cargar_datos()

    for reserva in datos["reservas"]:
        if reserva["libro"] == libro and reserva["estado"] == "vigente":
            print(f"Error: El libro '{libro}' ya está reservado.")
            return

    reserva = {
        "usuario": usuario,
        "libro": libro,
        "fecha_reserva": datetime.now().strftime("%Y-%m-%d"),
        "estado": "vigente"
    }
    datos["reservas"].append(reserva)
    guardar_datos(datos)
    print(f"Reserva registrada: {usuario} ha reservado '{libro}'.")

# Mostrar reservas
def mostrar_reservas():
    datos = cargar_datos()
    if datos["reservas"]:
        print("\nLista de Reservas:")
        for i, reserva in enumerate(datos["reservas"], start=1):
            print(f"{i}. Usuario: {reserva['usuario']}, Libro: {reserva['libro']}, Fecha: {reserva['fecha_reserva']}, Estado: {reserva['estado']}")
    else:
        print("No hay reservas registradas.")

# Cancelar reserva
def cancelar_reserva(usuario, libro):
    datos = cargar_datos()
    for reserva in datos["reservas"]:
        if reserva["usuario"] == usuario and reserva["libro"] == libro and reserva["estado"] == "vigente":
            reserva["estado"] = "cancelado"
            guardar_datos(datos)
            print(f"Reserva cancelada para el libro '{libro}' por {usuario}.")
            return
    print("Error: No se encontró una reserva activa para este usuario y libro.")



