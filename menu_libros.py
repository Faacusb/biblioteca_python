from libros import agregar_libro,mostrar_libros, modificar_libro,borrar_libro
def menu():
    print('Bienvenido a nuestra biblioteca')
    print('1. Agregar libro')
    print('2. Mostrar libros')
    print('3. Modificar libro')
    print('4. Borrar libro')
    print('5. Salir')

def abrir_menu():
    while True:
        menu()
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
            print('Adios.')
            break

        else:
            print('Opcion no valida, pruebe otra opcion.')   


abrir_menu()
