from prestamos import (
    registrar_prestamos,
    mostrar_prestamos,
    devolver_libro,
    seleccionar_usuario,
    seleccionar_libro
    
)
import json
def menu_prestamos():
    while True:
        print("\n--- Menu de Prestamos ---")
        print("1. Registrar prestamo")
        print("2. Mostrar todos los libros prestados")
        print("3. Devolver un libro")
        print("4. Volver al Menu Principal")

        opcion = input("Seleccione una opción: ")    

        if opcion == "1":
            usuario = seleccionar_usuario()
            if usuario:
                libro = seleccionar_libro()
                if libro:
                    registrar_prestamos(usuario["socio"], libro["titulo"])
        
        elif opcion == "2":
            mostrar_prestamos()

        elif opcion == "3":
            usuario = seleccionar_usuario()
            if usuario:
                libro = seleccionar_libro()
                if libro:
                    devolver_libro(usuario["socio"], libro["titulo"]) 

        elif opcion == "4":
            break
        else:
            print("Opcion invalida, pruebe otra opcion.")

if __name__ == "__main__":
    menu_prestamos()