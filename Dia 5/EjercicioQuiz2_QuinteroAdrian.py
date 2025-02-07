import json


#Abrir Json
def abrirJSON():
    dicFinal={}
    with open("./basededatos.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

#Guardar Json
def guardarJSON(basededatos):
    with open("./basededatos.json",'w') as outFile:
        json.dump(basededatos,outFile)

productos={}
productos=abrirJSON()

#Crear Menu
booleanito = True
while(booleanito==True):
    pcgamer=abrirJSON()
    print("##########################")
    print("######-Compra Pc Gamers####")
    print("##########################")
    print("##########################")
    print("1.Crear producto")
    print("2.Ver productos")
    print("3.Actualizar informacion")
    print("4.Eliminar productos")
    print("5.Salir del programa")
    opt=int(input(":"))
    if opt==1:
        for i in range(len(productos["productos"])):
             productoNuevo = {}
             productoNuevo["Nombre"] = input("Ingrese el nombre del producto: ")
             productoNuevo["Descripcion"] = input("Ingrese una descripcion para el producto: ")
             productoNuevo["Categoria"] = input("Ingrese la categoria en la que pertenece: ")
             productoNuevo["Precio"] = float(input("Ingrese el precio del producto: "))
             productos["productos"].append(productoNuevo)
             print("El Producto Ha Sido Creado Exitosamente!!!")
             break
    if opt==2:
        for i in range(len(productos["productos"])):
            print("########################")
            print(productos['productos'][0])
            print("########################")
            print(productos['productos'][1])
            print("########################")
            print(productos['productos'][2])
            print("########################")
            print(productos['productos'][3])
            print("########################")
            print(productos['productos'][4])
    if opt==3:
        for i in range(len(productos["productos"])):
            print(productos["productos"][0]["nombre"])
            print(productos["productos"][1]["nombre"])
            print(productos["productos"][2]["nombre"])
            print(productos["productos"][3]["nombre"])
            print(productos["productos"][4]["nombre"])
            seleccion = int(input("Que pc deseas actualizar: "))
            print()

            
