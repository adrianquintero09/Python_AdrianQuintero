#Construya un programa que me ayude a encontrar el próximo número de la siguiente serie.

def encontrar_proximo_serie(serie):
    # Calculamos las diferencias entre los números consecutivos
    diferencias = [serie[i] - serie[i-1] for i in range(1, len(serie))]
    

    # Predicción de la siguiente diferencia
    if len(diferencias) % 2 == 0:
        proxima_diferencia = 2  # Después de -3, el patrón alterna con +2
    else:
        proxima_diferencia = -3  # Después de +2, el patrón alterna con -3

    
    proximo_numero = serie[-1] + proxima_diferencia
    return proximo_numero

# Serie inicial
serie = [1, 1, 2, -1, 1, -2]
proximo_numero = encontrar_proximo_serie(serie)

print(f"La serie es: {serie}")
print(f"El próximo número en la serie es: {proximo_numero}")
