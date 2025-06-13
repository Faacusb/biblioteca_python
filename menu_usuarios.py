usuarios = []
contador_socios = 1

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
    print(f"Usuario agregado con número de socio: {contador_socios}") # Agregamos un número de socio que se asigna automáticamente para que sea mas personal
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
                print(f"Usuario con número de socio {num_socio} eliminado.")
                return

        print("No se encontró un usuario con ese número de socio.")

    except ValueError:
        print("Por favor, ingrese un número válido.")
