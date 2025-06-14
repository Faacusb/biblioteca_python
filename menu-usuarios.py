from usuarios import (
    agregar_usuario,
    mostrar_usuarios,
    modificar_usuario,
    borrar_usuario,
    cargar_usuarios
)

def menu_principal():
    print("\n Menú Principal: ")
    print("1. libros")
    print("2. usuarios")
    print("3. Salir")

def menu_usuarios():
    cargar_usuarios()  # Cargar usuarios al iniciar el menú

    while True:
        print("\n--- Menú Usuarios ---")
        print("1. Agregar usuario")
        print("2. Mostrar usuarios")
        print("3. Modificar usuario")
        print("4. Borrar usuario")
        print("5. Volver al menú principal")

        opcion = input("Elegí una opción: ")

        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            mostrar_usuarios()
        elif opcion == '3':
            modificar_usuario()
        elif opcion == '4':
            borrar_usuario()
        elif opcion == '5':
            print("Volviendo al menú principal...")
            break
        else:
            print("La opción no es válida.")
