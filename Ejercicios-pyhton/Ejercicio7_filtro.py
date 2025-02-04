
# Función para calcular la suma de los divisores propios de un número
def suma_divisores_propios(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:  # Verifica si i es divisor de numero
            suma += i
    return suma

# Función para verificar si dos números son amigos
def son_numeros_amigos(n1, n2):
    suma_n1 = suma_divisores_propios(n1)  # Suma de divisores propios de n1
    suma_n2 = suma_divisores_propios(n2)  # Suma de divisores propios de n2
    
    # Verificar si cumplen la condición de números amigos
    return suma_n1 == n2 and suma_n2 == n1

# Programa principal
def main():
    # Solicitar números al usuario
    try:
        n1 = int(input("Ingrese el primer número positivo (n1): "))
        n2 = int(input("Ingrese el segundo número positivo (n2): "))
        
        if n1 <= 0 or n2 <= 0:
            print("Ambos números deben ser enteros positivos.")
            return
        
        # Verificar si los números son amigos
        if son_numeros_amigos(n1, n2):
            print(f"{n1} y {n2} son números amigos.")
        else:
            print(f"{n1} y {n2} no son números amigos.")
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")


main()

#Desarrolado: Adrián Quintero Pinzón/