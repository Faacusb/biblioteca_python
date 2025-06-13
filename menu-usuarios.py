from usuarios import agregar_un_usuario, mostrar_un_usuarios, modificar_un_usuario, borrar_un_usuario

def menu_usuarios():
    while True:
        print("\n--- Menú Usuarios ---")
        print("1. Agregar usuario")
        print("2. Mostrar usuario")
        print("3. Modificar usuario")
        print("4. Borrar usuario")
        print("5. Volver al menú principal")

        opcion = input("Elegí una opción: ")

        if opcion == '1':
            agregar_un_usuario()
        elif opcion == '2':
            mostrar_un_usuario()
        elif opcion == '3':
            modifica_un_usuario()
        elif opcion == '4':
            borrar_un_usuario()
        elif opcion == '5':
            print("Volviendo al menú principal...")
            break
        else:
            print("la  opción no es  válida.")


