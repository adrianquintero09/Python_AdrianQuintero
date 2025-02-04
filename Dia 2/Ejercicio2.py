#Verificar si un numero es par o impar, clasificar numeros primos o compuestos, comprobar si un número es un cuadrado perfecto.

#Importar una libreria para el cuadrado perfecto.
import math

#Variables
Num=0
Num2=0
Num3=0

#Funcion de numero par o impar.
def par(numero):
    if numero % 2 == 0:
        return "Es par"
    else:
        return "Es impar"

#Funcion clasificar números como primos o compuestos.
def clasificar_numero(Num2):
    if Num2 < 2:
        return "No es primo ni compuesto"
    for i in range(2, int(Num2 ** 0.5) + 1):  
        if Num2 % i == 0:
            return f"{Num2} es un número compuesto"
    return f"{Num2} es un número primo"

#Funcion comprobar si un número es un cuadrado perfecto.
def cuadrado_perfecto(Num3):
    if Num3 > 0:
        print("Tu número es positivo")
        r = math.sqrt(Num3)
        if r % 1 == 0:  
            print("Es un número cuadrado perfecto")
        else:
            print("El número no es un cuadrado perfecto")
    elif Num3 == 0:
        print("0 es un cuadrado perfecto (0 * 0 = 0)")
    else:
        print("El número es negativo y no tiene raíz cuadrada real")

#Menu de opciones
print("//////////////////////////////////////////")
print("///////// Bienvenido a mi Programa ///////")
print("//////////////////////////////////////////")
print("------------ Elija una opción ------------")
print("1. Verificar si un número es par o impar.")
print("2. Clasificar un número como primo o compuesto.")
print("3. Comprobar si un número es un cuadrado perfecto.")

#Leer la opcion del usuario
opc = int(input("Ingresa una Opcion: "))
if opc == 1:
    Num = int(input("Ingrese un número: "))
    print(par(Num))
elif opc == 2:
    Num2 = int(input("Ingrese un número para verificar si es primo o compuesto: "))
    print(clasificar_numero(Num2))
elif opc == 3:
    Num3 = int(input("Ingrese un número para verificar si es cuadrado perfecto: "))
    cuadrado_perfecto(Num3)
else:
    print("Opción no válida. Inténtelo de nuevo.")

#Desarrollado: Adrián Quintero Pinzón /T.I : 1097 499 998