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
    opt=int(input(":"))
    if opt==1:
        for i in range(len(productos["productos"])):
         productoNuevo = {}
        productoNuevo["nombre"] = input("Ingrese el nombre del producto: ")
        productoNuevo["descripcion"] = input("Ingrese una descripción para el producto: ")
        productoNuevo["categoria"] = input("Ingrese la categoría a la que pertenece: ")
        productoNuevo["precio"] = float(input("Ingrese el precio del producto: "))  
        productos["productos"].append(productoNuevo)
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
input("Presiona Enter para salir...")
