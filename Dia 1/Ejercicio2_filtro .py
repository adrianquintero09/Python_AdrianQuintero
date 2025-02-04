# Programa para calcular la suma de la serie: 1 - 1/2 + 1/3 - 1/4 + ... ± 1/N

def calcular_serie(n):
    suma = 0
    for i in range(1, n + 1):
        # Sumar o restar dependiendo de si el índice es impar o par
        if i % 2 == 0:
            suma -= 1 / i
        else:
            suma += 1 / i
    return suma

# Solicitar al usuario el valor de N
try:
    n = int(input("Ingrese un número entero N: "))
    if n <= 0:
        print("Por favor, ingrese un número entero positivo.")
    else:
        resultado = calcular_serie(n)
        print(f"\nCantidad de términos: {n}")
        print(f"Resultado de la serie: {resultado:.6f}")
except ValueError:
    print("Debe ingresar un número entero válido.")
#Desarrollado: Adrián Quintero Pinzón/