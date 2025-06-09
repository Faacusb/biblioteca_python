libros = []

def agregar_libro():
    titulo = input('Ingrese el titulo del libro: ')
    autor  = input('Ingrese el autor: ')
    anio   = input('Ingrese el año del libro: ')

    libro = {'titulo': titulo, 'autor': autor, 'año': anio}
    libros.append(libro)
    print('Libro cargado.')

