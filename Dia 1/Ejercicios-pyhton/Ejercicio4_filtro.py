#Construya un programa que lea 10 números ingresados por el usuario y que al final, muestre el mayor y el menor de todos estos números

def encontrar_mayor_y_menor():
    numeros = []  # Variable para almacenar los números ingresados

    print("Ingrese 10 números:")
    for i in range(10):
        while True:
            try:
                numero = float(input(f"Ingrese el número {i+1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")

    mayor = max(numeros)  # Encuentra el número mayor
    menor = min(numeros)  # Encuentra el número menor

    print(f"\nEl número mayor es: {mayor}")
    print(f"El número menor es: {menor}")


encontrar_mayor_y_menor()

#Desarrollado: Adrián Quintero Pinzon/

