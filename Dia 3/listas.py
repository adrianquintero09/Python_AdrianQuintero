nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]

apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]
bo=True
while bo==True:
    print("////////////////////////////////////////////////////////")
    print("///Bienvenido al programa de lista de estudiantes///////")
    print("////////////////////////////////////////////////////////")
    print("Que te gustaría hacer?")
    print("1.Agregar estudiante")
    print("2. Ver estudiantes")
    print("3.Editar estudiante")
    print("4.Eliminar estudiante")
    print("5.Salir del programa")
    opc=int(input(":"))
    c1=0
    c=0
    if opc==1:
        print("ingrese el primer nombre del estudiante")
        n1=input(":")
        print("ingrese el segundo nombre (si lo tiene)")
        n2=input(":")
        print("Ingrese el primer apellido")
        ap1=input(":")
        print("ingrese el segundo apellido")
        ap2=input(":")
        nombres.append([n1,n2])
        apellidos.append([ap1,ap2])
    elif opc==2:
        for i in range(len(nombres)):
            ##nombres = [["Adrián"]] ---- apellidos = [["Quintero", "Pinzón"]] --- Adrían Quintero Pinzón
            print("estudiante#",i+1," "," ".join(nombres[c1])," ".join(apellidos[c]))
            c1+=1
            c+=1
    elif opc==3:
        for i in range(len(nombres)):
            ##nombres = [["Adrián"]] ---- apellidos = [["Quintero", "Pinzón"]] --- Adrían Quintero Pinzón
            print("estudiante#",i+1," "," ".join(nombres[c1])," ".join(apellidos[c]))
            c1+=1
            c+=1
        edt=int(input("Ingrese el estudiante que quiere editar (el numero de la lista)"))
        tamnombre=len(nombres[edt-1])
        tamapellido=len(apellidos[edt-1])
        if tamnombre==2:
            print("1. Primero nombre")
            print("2. Segundo nombre")
            o=int(input(": "))
            r=input("Ingrese el nombre corregido: ")
            if o==1:
                nombres[edt-1][0]=(r)
            else:
                nombres[edt-1][1]=(r)
        else:
            print("Ingrese el nombre corregido")
            r=input(": ")
            nombres[edt-1][0]=(r)
        if tamapellido==2:
            print("1. Primer apellido")
            print("2. Segundo apellido")
            t=int(input(": "))
            if t==1:
                ap=input("Digite el primer apellido corregido ")
                apellidos[edt-1][0]=(ap)
            else:
                ap=input("Digite el segundo apellido")
                apellidos[edt-1][1]=(ap)
        else:
            apr=input("Digite el apellido corregido")
            apellidos[edt-1][0]=(apr)
    elif opc==4:
        for i in range(len(nombres)):
            ##nombres = [["Adrián"]] ---- apellidos = [["Quintero", "Pinzón"]] --- Adrían Quintero Pinzón
            print("estudiante#",i+1," "," ".join(nombres[c1])," ".join(apellidos[c]))
            c1+=1
            c+=1
        el=int(input("ingrese el estudiante que quiere eliminar (el numero de la lista)"))
        nombres.pop(el-1)
        apellidos.pop(el-1)
    elif opc==5:
        break
    else:
        print("La opcion que ingreso es incorrecta")