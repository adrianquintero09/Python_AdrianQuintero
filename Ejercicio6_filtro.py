# Programa para calcular la nómina de N empleados en la empresa ACME

def calcular_nomina():
    # Constante del valor por hora
    VALOR_HORA = 20000
    
    # Listas para almacenar información de los empleados
    empleados = []
    totales_salario_bruto = 0
    totales_eps = 0
    totales_pension = 0
    totales_salario_neto = 0

    # Leer la cantidad de empleados
    while True:
        try:
            n = int(input("Ingrese el número de empleados: "))
            if n <= 0:
                print("Por favor, ingrese un número mayor a 0.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    
    # Recolectar datos de cada empleado
    for i in range(n):
        print(f"\nEmpleado {i + 1}:")
        nombre = input("Ingrese el nombre del empleado: ")
        while True:
            try:
                horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
                if horas_trabajadas < 0:
                    print("Las horas trabajadas no pueden ser negativas.")
                else:
                    break
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        # Calcular el sueldo bruto
        sueldo_bruto = horas_trabajadas * VALOR_HORA
        # Calcular los descuentos
        eps = sueldo_bruto * 0.04
        pension = sueldo_bruto * 0.04
        # Calcular el sueldo neto
        sueldo_neto = sueldo_bruto - eps - pension

        # Agregar datos del empleado a la lista
        empleados.append({
            "nombre": nombre,
            "sueldo_bruto": sueldo_bruto,
            "eps": eps,
            "pension": pension,
            "sueldo_neto": sueldo_neto
        })

        # Acumular totales
        totales_salario_bruto += sueldo_bruto
        totales_eps += eps
        totales_pension += pension
        totales_salario_neto += sueldo_neto

    # Mostrar información de cada empleado
    print("\nResumen de la nómina:")
    for empleado in empleados:
        print(f"\nEmpleado: {empleado['nombre']}")
        print(f"  Sueldo Bruto: ${empleado['sueldo_bruto']:.2f}")
        print(f"  Descuento EPS: ${empleado['eps']:.2f}")
        print(f"  Descuento Pensión: ${empleado['pension']:.2f}")
        print(f"  Sueldo Neto: ${empleado['sueldo_neto']:.2f}")
    
    # Estadísticas generales
    empleado_mayor = max(empleados, key=lambda x: x["sueldo_neto"])
    empleado_menor = min(empleados, key=lambda x: x["sueldo_neto"])
    promedio_sueldo_bruto = totales_salario_bruto / n
    promedio_sueldo_neto = totales_salario_neto / n

    print("\nEstadísticas de la nómina:")
    print(f"  Total Sueldos Brutos: ${totales_salario_bruto:.2f}")
    print(f"  Total EPS: ${totales_eps:.2f}")
    print(f"  Total Pensión: ${totales_pension:.2f}")
    print(f"  Total Sueldos Netos: ${totales_salario_neto:.2f}")
    print(f"  Promedio Sueldo Bruto: ${promedio_sueldo_bruto:.2f}")
    print(f"  Promedio Sueldo Neto: ${promedio_sueldo_neto:.2f}")
    print(f"\nEmpleado que más gana (Neto): {empleado_mayor['nombre']} con ${empleado_mayor['sueldo_neto']:.2f}")
    print(f"Empleado que menos gana (Neto): {empleado_menor['nombre']} con ${empleado_menor['sueldo_neto']:.2f}")

calcular_nomina()

#Desarrolado: Adrián Quintero Pinzón/