# ejemplo prueba 3

'''
Un NIF, es un NÚMERO DE IDENTIFICACIÓN FISCAL (NIF) otorgado por la Unión
Europea a los ciudadanos mayores de 15 años. Es el equivalente o similar al Rut o número
de identificación chileno.
Este NIF tiene ciertos beneficios para quien lo obtiene.
La estructura del NIF en España, es la siguiente:
● 99999999-RTX
● 03034567-XXY
● 12312345-CCU
● 00000001-03F
En el registro de ciudadanos pertenecientes a la Unión Europea de España, del pueblo del
sur de Andalucía, se requiere desarrollar un programa con un menú que contenga las
siguientes opciones:
Opción 1
● Grabar. Corresponde a guardar ciertos datos de una persona, entre ellos: NIF,
nombre, apellido y edad.
Debe verificar que el NIF sea correcto, que el nombre incluya al apellido en una sola
entrada por teclado (un solo input() separado por espacio) y que el nombre y apellido
por separado tenga mínimo 8 caracteres y que la edad sea mayor igual a 15.
Opción 2
● Buscar: Corresponde buscar a una persona por su NIF y mostrar toda su
información almacenada.
Opción 3
● Guardar archivos: Corresponde a crear un archivo .csv que contenga los datos de
todas las personas entre un rango de edad dado por teclado ordenadas
alfabéticamente por nombre. El archivo debe llamarse: “edades_entre_a_y_b.csv”,
donde a y b son las edades del rango dado.
Opción 4
● Salir. Corresponde a salir del programa emitiendo un mensaje de salida. Considere,
además, su nombre y apellido y la versión del programa.
Instrucciones Generales:
Escribir un programa que contenga dos archivos:
1. Principal, en el cual, debe contener un menú con las opciones para acceder a cada
función requerida.
Sólo, considere el ingreso de datos y el despliegue de información.
2. Funciones: Debe contener todos los procesos y validaciones de los requerimientos

'''
import csv
l_nif = []
l_nom = []

lista_final = []
def menu():
    print(" 1-Grabar\n 2-Buscar\n 3-Guardar archivos\n 4-Salir")

def verificar_nif(fnif):
    flag = False
    try:
        if fnif[8] == "-":
            l_nif = fnif.strip().split("-")
            for i in l_nif[0]:
                if i  in "1234567890":
                    flag = True
                else:
                    flag = False
        if flag == True:
            return True
        else :
            return False
    except:
        return False
def verificar_nombre(fnombre):
    for letra in fnombre:
        if " " in letra:
            l_nom = fnombre.strip().split(" ")
            if len(l_nom[0]) >= 8 and len(l_nom[1]) >= 8:
                return True
    
def verificar_edad(fedad):
    try :
        if fedad < 15:
            return False
        else :
            return True
    except:
        return False

diccionario = {}               
op = ""
while op != "4":
    menu()
    op = input("ingrese una opcion ")

    if op == "1":
        while True:
            nif = input("ingrese nif ") 
            if verificar_nif(nif):
                print("nif guardado correctamente ")
                nif_final = nif
                break
            else:
                print("nif incorrecto")
        
        while True:
            nombre = input ("ingrese su nombre ")
            if verificar_nombre(nombre):
                print("nombre guardado correctamente ")
                nombrefinal= nombre
                break
            else:
                print("nombre incorrecto ")
        while True:
            edad = int(input("ingrese edad "))
            if verificar_edad(edad):
                edadfinal = edad
                print("edad guardada correctamente ")
                break
            else:
                print("error, edad no valida")   
        l_usuario = []
        l_usuario.append(nombrefinal)
        l_usuario.append(edadfinal)
        diccionario[nif_final] = l_usuario
        lista_final.append(list(diccionario.items()))
        print(lista_final)
    elif op == "2":
        nif_busqueda = input("ingrese nif a buscar ")
        print(diccionario[nif_busqueda])

    elif op == "3":
        archivo = open("archivo_de_nif.csv","w",newline= '')

        contenido = csv.writer(archivo)
        contenido.writerows(lista_final)
        
        archivo.close()
        


    


      




    





   
