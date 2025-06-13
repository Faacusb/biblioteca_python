import json

archivo_libros = 'libros.json'
libros = []

def agregar_libro():
    titulo = input('Ingrese el titulo del libro: ')
    autor  = input('Ingrese el autor: ')
    anio   = input('Ingrese el año del libro: ')

    libro = {'titulo': titulo, 'autor': autor, 'año': anio}
    libros.append(libro)
    print('Libro cargado.')

def mostrar_libros():
    if not libros:
        print('No hay libros en la biblioteca')
    else:
        print('\nLista de libros: ') 
        for i, libro in enumerate(libros, start=1):
            print(f"{i}. {libro['titulo']} - Autor: {libro['autor']} - año: {libro['año']}")
            

def modificar_libro():
    try:
        num_libro_modificar = int(input('Ingrese el numero del libro que desea modificar: ')) -1

        if 0 <= num_libro_modificar < len(libros):
            nuevo_titulo = input('Ingrese titulo: ')
            nuevo_autor  = input('Ingrese el Autor: ')
            nuevo_anio   = input('Ingrese el año del libro: ')

            libros[num_libro_modificar]['titulo'] = nuevo_titulo
            libros[num_libro_modificar]['autor']  = nuevo_autor
            libros[num_libro_modificar]['año']    = nuevo_anio

            print('Libro modificado con exito')
        else:
            print("El numero de libro elegido es incorrecto.")

    except ValueError:
        print('Tipo de caracter incorrecto, Por favor ingrese un numero valido')            

def borrar_libro():
    if not libros:
        print('No hay libros para borrar.')
        return
    mostrar_libros()   

    try:
        num_libro_borrar = int(input('Ingrese el numero del libro que desea borrar.')) -1

        if 0 <= num_libro_borrar < len(libros):
            libro_borrado = libros.pop(num_libro_borrar)
            print(f"Libro borrado: {libro_borrado['titulo']} - {libro_borrado['autor']}")

        else:
            print('Numero de libro invalido.')

    except ValueError:
        print('Tipo de caracter icorrecto, Por favor ingrese un numero valido.')            