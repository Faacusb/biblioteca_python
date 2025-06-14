from menu_libros import archivo_libros as menu_libros  #importe la funcion menu_libros 


def menu_principal():
    print("\n Menú Principal")
    print("1. Libros")
    print("2. Salir")

def iniciar_menu():
    while True:
       menu_principal()
       opcion = input("Elegí una opción: ")

       if opcion == '1':
            menu_libros()  
       elif opcion == '2':
            print("¡nos vemos!")
            break
       else:
            print(" Error. Probá otra vez.")

if __name__ == "__main__": #esto es para que se ejecute directo 
    iniciar_menu()
