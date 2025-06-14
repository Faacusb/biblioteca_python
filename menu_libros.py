from libros import (
    agregar_libro,
    mostrar_libros,
    modificar_libro,
    borrar_libro,
    cargar_libros
)

def abrir_menu():
    cargar_libros()  # Cargar libros al iniciar

    while True:
        print('\nBienvenido a nuestra biblioteca')
        print('1. Agregar libro')
        print('2. Mostrar libros')
        print('3. Modificar libro')
        print('4. Borrar libro')
        print('5. Salir')

        opcion_menu = input('Elija una opción: ')

        if opcion_menu == '1':
            agregar_libro()
        elif opcion_menu == '2':
            mostrar_libros()
        elif opcion_menu == '3':
            modificar_libro()
        elif opcion_menu == '4':
            borrar_libro()
        elif opcion_menu == '5':
            print('Saliendo del programa.')
            break
        else:
            print('Opción no válida. Intente de nuevo.')
