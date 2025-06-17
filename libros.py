import json
import os

archivo_libros = 'libros.json'
libros = []

# Cargar libros desde el archivo al inicio
def cargar_libros():
    global libros
    if os.path.exists(archivo_libros):
        with open(archivo_libros, 'r', encoding='utf-8') as f:
            try:
                libros = json.load(f)
            except json.JSONDecodeError:
                libros = []
    else:
        libros = []

# Guardar libros en el archivo
def guardar_libros():
    with open(archivo_libros, 'w', encoding='utf-8') as f:
        json.dump(libros, f, indent=4, ensure_ascii=False)

def agregar_libro():
    titulo = input('Ingrese el titulo del libro: ')
    
    for libro in libros:
        if libro['titulo'].lower() == titulo.lower():
            print(f"Ya existe ese titulo en la biblioteca '{titulo}'.")
            return

    autor  = input('Ingrese el autor: ')
    anio   = input('Ingrese el año del libro: ')

    libro = {'titulo': titulo, 'autor': autor, 'año': anio, 'prestado':False, 'socio_prestamo':None}
    libros.append(libro)
    guardar_libros()
    print('Libro cargado.')

def mostrar_libros():
    if not libros:
        print('No hay libros en la biblioteca')
    else:
        print('\nLista de libros:') 
        for i, libro in enumerate(libros, start=1):
            print(f"{i}. {libro['titulo']} - Autor: {libro['autor']} - año: {libro['año']}")

def modificar_libro():
    if not libros:
        print("No hay libros para modificar.")
        return

    mostrar_libros()
    try:
        num_libro_modificar = int(input('Ingrese el número del libro que desea modificar: ')) - 1
        if 0 <= num_libro_modificar < len(libros):
            nuevo_titulo = input('Ingrese nuevo título: ')
            nuevo_autor  = input('Ingrese nuevo autor: ')
            nuevo_anio   = input('Ingrese nuevo año del libro: ')

            libros[num_libro_modificar] = {
                'titulo': nuevo_titulo,
                'autor': nuevo_autor,
                'año': nuevo_anio
            }
            guardar_libros()
            print('Libro modificado con éxito.')
        else:
            print("Número de libro inválido.")
    except ValueError:
        print('Por favor, ingrese un número válido.')

def borrar_libro():
    if not libros:
        print('No hay libros para borrar.')
        return

    mostrar_libros()
    try:
        num_libro_borrar = int(input('Ingrese el número del libro que desea borrar: ')) - 1
        if 0 <= num_libro_borrar < len(libros):
            libro_borrado = libros.pop(num_libro_borrar)
            guardar_libros()
            print(f"Libro borrado: {libro_borrado['titulo']} - {libro_borrado['autor']}")
        else:
            print('Número de libro inválido.')
    except ValueError:
        print('Por favor, ingrese un número válido.')   
