import modulo
import data

nombres = data.nombres
apellidos = data.apellidos

bo=True
while bo==True:
    
    modulo.hello()
    
    opc=int(input(":"))
    c1=0
    c=0
    #crear uno
    if opc==1:
        resp1 = modulo.instruccionesCrear()
        nombres.append([resp1[0],resp1[1]])
        apellidos.append([resp1[2],resp1[3]])
    #Listar todos
    elif opc==2:
        modulo.verTodos(nombres, apellidos)
       
    # Editar
    elif opc==3:
        #[primerNombre, segundoNombre, primerApellido, segundoApellido, indice]
        nuevoUsuario = modulo.EditarNombre(nombres,apellidos)
        indice = nuevoUsuario[4]-1
        nombres[indice][0]=nuevoUsuario[0]
        if (nuevoUsuario[1]!=""): nombres[indice][1]=nuevoUsuario[1]

        apellidos[indice][0]=nuevoUsuario[2]
        if (nuevoUsuario[3]!=""): apellidos[indice][1]=nuevoUsuario[3]

    # eliminar
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
        print("La opcion que ingreso es incorrecta")