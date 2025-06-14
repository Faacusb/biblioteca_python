from libros import agregar_libro,mostrar_libros, modificar_libro,borrar_libro


def abrir_menu():
    while True:
        
        print('Bienvenido a nuestra biblioteca')
        print('1. Agregar libro')
        print('2. Mostrar libros')
        print('3. Modificar libro')
        print('4. Borrar libro')
        print('5. Volver al menu principal')

        opcion_menu = input('Elija una opcion: ')

        if opcion_menu == '1':
            agregar_libro()
        
        elif opcion_menu == '2':
            mostrar_libros()

        elif opcion_menu == '3':
            modificar_libro()

        elif opcion_menu  == '4':
            borrar_libro()

        elif opcion_menu == '5':
            
            break

        else:
            print('Opcion no valida, pruebe otra opcion.')   


