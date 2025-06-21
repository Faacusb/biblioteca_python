import json
import os

archivo_usuarios = 'usuarios.json'
usuarios = []
contador_socios = 1

def cargar_usuarios():
    global usuarios, contador_socios
    if os.path.exists(archivo_usuarios):
        with open(archivo_usuarios, 'r', encoding='utf-8') as f:
            try:
                usuarios = json.load(f)
                # Actualizar el contador con el mayor número de socio + 1
                if usuarios:
                    contador_socios = max(u["socio"] for u in usuarios) + 1
            except json.JSONDecodeError:
                usuarios = []
    else:
        usuarios = []

def guardar_usuarios():
    with open(archivo_usuarios, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

def agregar_usuario():
    global contador_socios

    nombre = input("Ingrese el nombre del usuario: ")
    apellido = input("Ingrese el apellido: ")
    tipo_doc = input("Ingrese el tipo de documento (DNI, Pasaporte, etc.): ")
    documento = input("Ingrese el número de documento: ")
    direccion = input("Ingrese la dirección: ")

    usuario = {
        "socio": contador_socios,
        "nombre": nombre,
        "apellido": apellido,
        "tipo_doc": tipo_doc,
        "documento": documento,
        "direccion": direccion
    }

    usuarios.append(usuario)
    guardar_usuarios()
    print(f"Usuario agregado con número de socio: {contador_socios}")
    contador_socios += 1

def mostrar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print("\nLista de usuarios:")
        for usuario in usuarios:
            print(f"Socio {usuario['socio']}: {usuario['nombre']} {usuario['apellido']} - {usuario['tipo_doc']} {usuario['documento']} - Dirección: {usuario['direccion']}")

def modificar_usuario():
    try:
        num_socio = int(input("Ingrese el número de socio del usuario que desea modificar: "))
        for usuario in usuarios:
            if usuario["socio"] == num_socio:
                usuario["nombre"] = input("Nuevo nombre: ")
                usuario["apellido"] = input("Nuevo apellido: ")
                usuario["tipo_doc"] = input("Nuevo tipo de documento: ")
                usuario["documento"] = input("Nuevo número de documento: ")
                usuario["direccion"] = input("Nueva dirección: ")
                guardar_usuarios()
                print("Usuario modificado con éxito.")
                return
        print("No se encontró un usuario con ese número de socio.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def borrar_usuario():
    try:
        num_socio = int(input("Ingrese el número de socio del usuario que desea borrar: "))
        for usuario in usuarios:
            if usuario["socio"] == num_socio:
                usuarios.remove(usuario)
                guardar_usuarios()
                print(f"Usuario con número de socio {num_socio} eliminado.")
                return
        print("No se encontró un usuario con ese número de socio.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def usuario_existe(socio_id):
    try:
        with open(archivo_usuarios, "r", encoding="utf-8") as archivo:
            lista_usuarios = json.load(archivo)
        return any(u["socio"] == socio_id for u in lista_usuarios)
    except FileNotFoundError:
        return False