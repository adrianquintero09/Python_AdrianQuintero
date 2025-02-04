def hello():
    print("\nBienvenido al programa de lista de estudiantes")
    print("Que te gustaría hacer?")
    print("1.Agregar estudiante")
    print("2. Ver estudiantes")
    print("3.Editar estudiante")
    print("4.Eliminar estudiante")
    print("5.Salir del programa")

def instruccionesCrear():
    
    print("ingrese el primer nombre del estudiante")
    n1=input(":")
    print("ingrese el segundo nombre (si lo tiene)")
    n2=input(":")
    print("Ingrese el primer apellido")
    ap1=input(":")
    print("ingrese el segundo apellido")
    ap2=input(":")

    return [n1, n2, ap1, ap2]

def verTodos(nombres, apellidos):
    c=0
    for i in range(len(nombres)):
        ##nombres = [["Adrián"]] ---- apellidos = [["Quintero", "Pinzón"]] --- Adrían Quintero Pinzón
        print("estudiante#",i+1," "," ".join(nombres[c])," ".join(apellidos[c]))
        c+=1

def EditarNombre(nombres,apellidos):
    c=0
    for i in range(len(nombres)):
        ##nombres = [["Adrián"]] ---- apellidos = [["Quintero", "Pinzón"]] --- Adrían Quintero Pinzón
        print("estudiante#",i+1," "," ".join(nombres[c])," ".join(apellidos[c]))
        c+=1
    # ingresa el indice
    indice=int(input("Ingrese el estudiante que quiere editar (el numero de la lista)"))
    tamnombre=len(nombres[indice-1])
    tamapellido=len(apellidos[indice-1])
    # validamos que tenga la extructura de la lista

    primerNombre=''
    segundoNombre=''
    primerApellido=''
    segundoApellido=''

    # llenamos nombre
    if tamnombre==2:
        print("1. Primer nombre")
        primerNombre=input("Ingrese el primer nombre: ")

        print("2. Segundo nombre")
        segundoNombre=input("Ingrese el segundo nombre: ")
    else:
        print("1. Primer nombre")
        primerNombre=input("Ingrese el primer nombre: ")

    # llenamos apellido
    if tamapellido==2:
        print("1. Primer apellido")
        primerApellido=input("Ingrese el primer apellido: ")

        print("2. Segundo apellido")
        segundoApellido=input("Ingrese el segundo apellido: ")
    else:
        print("1. Primer apellido")
        primerApellido=input("Ingrese el primer apellido: ")

    return [primerNombre, segundoNombre, primerApellido, segundoApellido, indice]