import os
menu='''
1.registrar vehiculo
2.lista
3.orden para reparacion
4.Salir
'''

titulo= '''                         Lista de vehiculos
----------------------------------------------------------------------------------------------
Marca          Año de fabricacion   Kilometraje  Costo de repacion  Impuesto  Costo Total
----------------------------------------------------------------------------------------------
'''
lista= []
marcas= ["Toyota","Subaru","Audi"]
def registrar_vehiculo():
    while True:
        try:
            os.system('cls')
            marca= input(f"Marca del vehiculo {marcas}: ").strip().lower()
            af= int(input("Año de fabricacion: "))
            k= int(input("Kilometraje: "))
            cs= int(input("costo de reparacion: "))
            cst= round(cs*0.8)
            aaa= round(cs+cst)
            lista.append([marca,af,k,cs,cst,aaa])
            input("Vehiculo registrado")
            break
        except:()

def lista_vehiculos():
    salida= titulo
    for t in lista:
        salida += f"{t[0]:6s}"
        salida += f"{t[1]:10s}"
        salida += f"{t[2]:10d}" 
        salida += f"{t[3]:10d}"
        salida += f"{t[4]:10d}"
        salida += f"{t[5]:10d}"
        salida += "\n"
    return salida

def lista_marca(marca):
    salida= titulo
    for t in lista:
        salida += f"{t[0]:6s}"
        salida += f"{t[1]:10s}"
        salida += f"{t[2]:10d}" 
        salida += f"{t[3]:10d}"
        salida += f"{t[4]:10d}"
        salida += f"{t[5]:10d}"
        salida += "\n"
    return salida

              

def orden_reparacion():
    x= input(f"Orden de reparacion [todos/{marcas}]: ").strip().lower()
    if x == "todos":
        with open("orden de reparacion.txt","w") as archivo:
            archivo.write(lista_vehiculos())
    elif x in marcas:
        with open("orden de reparacion.txt","w") as archivo:
            archivo.write(lista_marca(x))
    else:
        input("error de ingreso")



while True:
    try:
        opc= input(menu)
        if opc == "1":
            registrar_vehiculo()
        elif opc =="2":
            print(lista_vehiculos())
        elif opc =="3":
            orden_reparacion()
        elif opc == "4":
            print("adios")
            break
    except:()