#Construya un programa tal que encuentre y muestre todos los enteros positivos, comenzando desde el cero, que satisfacen la siguiente expresión:

def encontrar_soluciones():
    limite = 680  
    print("Soluciones (P, Q) que cumplen P^3 + Q^4 - 2*P^2 < 680:\n")
    
    for P in range(0, 50):
        for Q in range(0, 50): 
            expresion = P**3 + Q**4 - 2 * P**2
            if expresion < limite:
                print(f"P = {P}, Q = {Q}, Expresión = {expresion}")


encontrar_soluciones()
