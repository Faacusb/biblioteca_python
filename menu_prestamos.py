from prestamos import (
    registrar_prestamo,
    mostrar_prestamos,
    devolver_libro
)

def menu_prestamos():
    while True:
        print("\n--- Menú de Préstamos ---")
        print("1. Registrar préstamo")
        print("2. Devolver libro")
        print("3. Ver préstamos")
        print("4. Volver al menú principal")

        opcion = input("Elegí una opción: ")

        if opcion == '1':
            registrar_prestamo()
        elif opcion == '2':
            devolver_libro()
        elif opcion == '3':
            mostrar_prestamos()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Probá otra vez.")
