from menu_libros import abrir_menu as menu_libros  #importe la funcion menu_libros 
from menu_usuarios import menu_usuarios  #importe la funcion menu_usuarios
from menu_prestamos import menu_prestamos
from menu_prestamos import menu_prestamos  #importar prestamos
from exportar_informe import exportar_informe #modulo para exportar a excel
import requisitos  #Verifica e instala openpyxl si hace falta

def menu_principal():
    print("\n Menú Principal")
    print("1. Libros")
    print("2. Usuarios")
    print("3. Prestamos")
    print("4. Exportar Informe")
    print("5. Salir")

def iniciar_menu():
    while True:
       menu_principal()
       opcion = input("Elegí una opción: ")

       if opcion == '1':
            menu_libros()  

       elif opcion == '2':
            menu_usuarios()
       
       elif opcion == '3':
            menu_prestamos()     
       
       elif opcion == '4':
            exportar_informe()     
              
       elif opcion == '5':
            print("¡nos vemos!")
            break
       else:
            print(" Error. Probá otra vez.")

if __name__ == "__main__": #esto es para que se ejecute directo 
    iniciar_menu()
