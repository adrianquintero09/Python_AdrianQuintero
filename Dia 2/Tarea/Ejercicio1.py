#Programa que pase de Celsius a Fahrenheit 

#Variables
x=0
x2=0

#Pedir al usuario que ingrese los grados
x=int(input("Ingrese los grados para pasarlos de Celsius a Fahrenheit: "))
def celsius_a_fahrenheit(celsius  ):
    fahrenheit= celsius *9/5+32
    return fahrenheit

resultado= celsius_a_fahrenheit(x)

print("El resultado de Celsius a Fahrenheit es: ",resultado)

x2=int(input("Ingrese los grados para pasarlos de Fahrenheit a Celsius: "))
def fahrenheit_a_celsius (Fahrenheit):
    celsius= Fahrenheit -32* 5/9
    return celsius

resultado2= fahrenheit_a_celsius(x2)
print("El resultado de Fahrenheit a Celsius es :", resultado2)

#Desarrollado: Adrián Quintero Pinzón /T.I : 1097 499 998