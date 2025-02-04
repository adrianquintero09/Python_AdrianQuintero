#1.Construya un programa que muestre los números divisibles de 3 y 7 entre 1 y 1000.

def divisibles_por_3_y_7():
    print("Números divisibles por 3 y 7 entre 1 y 1000:")
    for num in range(1, 1001):
        if num % 3 == 0 and num % 7 == 0:
            print(num)
divisibles_por_3_y_7()

#Desarrollado por: Adrián Quintero Pinzón/
    