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