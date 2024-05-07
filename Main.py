import json,os

with open("Info.json", encoding="utf-8") as archivo:
    Datos=json.load(archivo)

Booleano1=True
while Booleano1:                                                                                                                                            
    os.system("cls")
    print("================Menu Principal================\n1).Administrador usuarios.\n2).Administrador planes.\n3).Usuarios.\n4).Salir.\n================Menu Principal================")
    opcion=str(input("Ingrese un numero para ir a la opcion deseada: "))
    if opcion=="1":#Listo
        Usuario=str(input("Ingrese el usuario del coordinador: "))
        Contraseña=str(input("Ingrese la contraseña del coordinador: "))
        if Usuario==Datos[0]["Personas"][0]["Usuario"] and Contraseña==Datos[0]["Personas"][0]["Usuario"]:
            Booleano2=True
            while Booleano2:
                os.system("cls")
                print("================Menu Administrador================\n1).Crear usuarios.\n2).Ver usuarios.\n3).Actualizar usuarios.\n4).Eliminar usuarios.\n5).Salir.\n================Menu Administrador================")
                opcion=str(input("Ingrese un numero para ir a la opcion deseada: "))
                if opcion=="1":#Listo
                    os.system("cls")
                    Nombre=str(input("Ingrese el nombre del usuario a registrar: "))                                                                                  
                    Identificacion=str(input("Ingrese el numero de identificacion del usuario a registrar: "))
                    Edad=str(input("Ingrese la edad de la persona a registrar: "))
                    Direccion=str(input("Ingrese la direccion del usuario a registrar:"))
                    Telefono=str(input("Ingrese el telefono del usuario a registrar: "))
                    Datos[1]["Personas"].append({
                        "Identificacion": Identificacion,
                        "Nombre": Nombre,
                        "Edad": Edad,
                        "Categoria": "Nuevo usuario",
                        "Direccion": Direccion,
                        "Telefono": Telefono,
                        "Plan": "None"
                    })
                    input("Usuario registrado con exito, ingrese al menu planes para establecerle un plan referente a sus preferencias :D. Presione Enter para continuar")
                    with open("Info.json", "w") as file:
                        json.dump(Datos,file)
                elif opcion=="2":#Listo
                    for i in range(0,len(Datos[1]["Personas"])):
                        print("=====================Usuario=====================")
                        print("**",i+1,"**")
                        print("Identificaion:",Datos[1]["Personas"][i]["Identificacion"],"\nNombre:",Datos[1]["Personas"][i]["Nombre"],"\nEdad:",Datos[1]["Personas"][i]["Edad"],"\nCategoria:",Datos[1]["Personas"][i]["Categoria"],"\nPlan:",Datos[1]["Personas"][i]["Plan"])
                    input("Presione Enter para ir al menu principal")
                elif opcion=="3":#Listo
                    iD=str(input("Ingrese la iD del usuario que desea actualizar: "))
                    for i in range(0,len(Datos[1]["Personas"])):
                        if iD == Datos[1]["Personas"][i]["Identificacion"]:
                            Booleano3=True
                            while Booleano3:
                                os.system("cls")
                                print("================Actualizar usuario================\n1).Actualizar plan.\n2).Actualizar nombre.\n3).Actualizar identificacion.\n4).Actualizar edad.\n5).Actualizar categoria.\n6).Salir.\n================Actualizar usuario================")
                                opcion=str(input("Ingrese un numero para ir a la opcion deseada: "))
                                if opcion=="1": #Listo
                                    Nombre=str(input("Ingrese el codigo del plan que deseas actualizar o agregar al usuario: "))
                                    for j in range(0,len(Datos[2]["Personas"])):
                                        if Nombre==Datos[2]["Personas"][j]["Codigo"]:
                                            Datos[1]["Personas"][i]["Plan"]=Datos[2]["Personas"][j]["Nombre"]
                                            input("Plan actualizado con exito :D")
                                            Datos[2]["Personas"][j]["Clientes"]+=1
                                            with open("Info.json", "w") as file:                                                                                                            
                                                json.dump(Datos,file)
                                            break
                                        else:
                                            if j == len(Datos[2]["Personas"])-1:
                                                input("iD no encontrada, procure escribir bien la identificacion, presione Enter para continuar.")
                                                break
                                elif opcion=="2":
                                    NewNombre=str(input("Ingrese el nuevo nombre del usuario (Ingresar el nombre completo): "))
                                    Datos[1]["Personas"][i]["Nombre"]=NewNombre
                                    input("Nombre actualizado con exito :D")
                                elif opcion=="3":
                                    NewIdentificacion=str(input("Ingrese la nueva identificacion: "))
                                    Datos[1]["Personas"][i]["Identificacion"]=NewIdentificacion
                                    input("Identificacion actualizada con exito :D")
                                elif opcion=="4":
                                    NewEdad=str(input("Ingresar la nueva edad a actualizar: "))
                                    Datos[1]["Personas"][i]["Edad"]=NewEdad
                                    input("Edad actualizada con exito")
                                elif opcion=="5":
                                    NewCategoria=input("Ingresar la nueva categoria a actualizar: ")
                                    Datos[1]["Personas"][i]["Categoria"]=NewCategoria
                                    input("Categoria actualizada con exito")
                                elif opcion=="6":
                                    with open("Info.json", "w") as file:
                                        json.dump(Datos,file)
                                    Booleano3=False
                                    break
                                else:
                                    input("Elige una opcion valida para poder continuar con el menu :D")
                        else:
                            if i == len(Datos[1]["Personas"])-1:
                                input("iD no encontrada, procure escribir bien la identificacion, presione Enter para continuar.")
                                break
                elif opcion=="4":#Listo
                    iD=str(input("Ingrese la iD del usuario que desea eliminar: "))
                    for i in range(0,len(Datos[1]["Personas"])):
                        if iD == Datos[1]["Personas"][i]["Identificacion"]:
                            Datos[1]["Personas"].pop(i)                                                                                                       
                            with open("Info.json", "w") as file:                                                                                                            
                                json.dump(Datos,file)
                            break
                        else:
                            if i == len(Datos[1]["Personas"])-1:
                                input("iD no encontrada, procure escribir bien la identificacion, presione Enter para continuar.")
                                break
                elif opcion=="5":#Listo, este si costo
                    Booleano2=False
                else:
                    input("Elige una opcion valida para poder continuar con el menu :D")
        else:
            print(input("Usuario o contraseña invalido, presione Enter para volver al menu inicial :D"))
    elif opcion=="2":
        Usuario=str(input("Ingrese el usuario del coordinador: "))
        Contraseña=str(input("Ingrese la contraseña del coordinador: "))
        if Usuario==Datos[0]["Personas"][0]["Usuario"] and Contraseña==Datos[0]["Personas"][0]["Usuario"]:
            Booleano4=True
            while Booleano4:
                os.system("cls")
                print("================Menu Administrador================\n1).Crear plan.\n2).Ver planes existentes.\n3).Actualizar el precio del plan.\n4).Eliminar plan.\n5).Mostrar planes mas populares.\n6).Salir\n================Menu Administrador================")
                opcion=str(input("Ingrese un numero para ir a la opcion deseada: "))
                if opcion=="1":
                    os.system("cls")
                    iD=str(input("Ingrese la iD del plan que vas a crear: "))
                    Nombre=str(input("Ingrese el nombre del plan que se va a crear: "))
                    Duracion=str(input("Ingrese la duracion del plan que se va a crear: "))
                    Precio=str(input("Ingrese el precio del plan que se va a crear: "))
                    Datos[2]["Personas"].append(
                        {
                            "Codigo": iD,
                            "Nombre": Nombre,
                            "Duracion": Duracion,
                            "Precio": Precio,
                            "Clientes":0
                        }
                    )
                    with open("Info.json", "w") as file:                                                                                                            
                        json.dump(Datos,file)
                elif opcion=="2":
                    os.system("cls")
                    for i in range(0,len(Datos[2]["Personas"])):
                        print("=====================Plan=====================")
                        print("**",i+1,"**")
                        print("iD:",Datos[2]["Personas"][i]["Codigo"],"\nNombre:",Datos[2]["Personas"][i]["Nombre"],"\nDuracion:",Datos[2]["Personas"][i]["Duracion"],"\nPrecio:",Datos[2]["Personas"][i]["Precio"])
                    input("Presione Enter para continuar")
                elif opcion=="3":
                    iD=str(input("Ingrese la iD del plan al que le desea actualizar el precio: "))
                    for i in range(0,len(Datos[2]["Personas"])):
                        if iD == Datos[2]["Personas"][i]["Codigo"]:
                            Precio=str(input("Ingrese el nuevo precio para el plan: "))
                            Datos[2]["Personas"][i]["Precio"]=Precio                                                                                           
                            with open("Info.json", "w") as file:                                                                                                            
                                json.dump(Datos,file)
                            break
                        else:
                            if i == len(Datos[2]["Personas"])-1:
                                input("iD no encontrada, procure escribir bien el identificador, presione Enter para continuar.")
                                break
                elif opcion=="4":
                    iD=str(input("Ingrese la iD del plan que desea eliminar: "))
                    for i in range(0,len(Datos[2]["Personas"])):
                        if iD == Datos[2]["Personas"][i]["Codigo"]:
                            Datos[2]["Personas"].pop(i)                                                                                                       
                            with open("Info.json", "w") as file:                                                                                                            
                                json.dump(Datos,file)
                            break
                        else:
                            if i == len(Datos[2]["Personas"])-1:
                                input("iD no encontrada, procure escribir bien el identificador, presione Enter para continuar.")
                                break
                elif opcion=="5":
                    popular=[]
                    for i in range(0,len(Datos[2]["Personas"])):
                        popular.append(Datos[2]["Personas"]["Clientes"])
                elif opcion=="6":
                    Booleano4=False
        else:
            input("Usuario o contraseña invalido, presione Enter para volver al menu inicial :D")
    elif opcion=="3":
        iD=str(input("Ingrese la identificacion del usuario: "))
        Edad=str(input("Ingrese la edad del usuario: "))
        for i in range(0,len(Datos[1]["Personas"])):
            if iD==Datos[1]["Personas"][i]["Identificacion"] and Edad==Datos[1]["Personas"][i]["Edad"]:
                Booleano5=True
                while Booleano5:
                    os.system("cls")
                    print("================Menu usuarios================\n1).Cambiar plan.\n2).Planes disponibles.\n3).Datos personales.\n4).Salir\n================Menu Principal================")
                    opcion=str(input("Ingrese un numero para ir a la opcion deseada: "))
                    if opcion=="1":
                        iD=str(input("Ingrese la iD del plan que deseas adquirir: "))
                        for j in range(0,len(Datos[2]["Personas"])):
                            if iD == Datos[2]["Personas"][j]["Codigo"]:
                                Datos[1]["Personas"][i]["Plan"]=Datos[2]["Personas"][j]["Codigo"]
                                input("Plan actualizado con exito :D")
                                break
                            else:
                                if j == len(Datos[2]["Personas"])-1:
                                    input("iD no encontrada, procure escribir bien el identificador, presione Enter para continuar.")
                    elif opcion=="2":
                        os.system("cls")
                        for i in range(0,len(Datos[2]["Personas"])):
                            print("=====================Plan=====================")
                            print("**",i+1,"**")
                            print("iD:",Datos[2]["Personas"][i]["Codigo"],"\nNombre:",Datos[2]["Personas"][i]["Nombre"],"\nDuracion:",Datos[2]["Personas"][i]["Duracion"],"\nPrecio:",Datos[2]["Personas"][i]["Precio"])
                        input("Presione Enter para continuar")
                    elif opcion=="3":
                        print("===============================Datos Personales===============================")
                        print("Identificaion:",Datos[1]["Personas"][i]["Identificacion"],"\nNombre:",Datos[1]["Personas"][i]["Nombre"],"\nEdad:",Datos[1]["Personas"][i]["Edad"],"\nCategoria:",Datos[1]["Personas"][i]["Categoria"],"\nPlan:",Datos[1]["Personas"][i]["Plan"])
                        print("===============================Datos Personales===============================")
                        input("Presione Enter para continuar")
                    elif opcion=="4":
                        Booleano5=False
                        break
                    else:
                        input("Elige una opcion valida para poder continuar con el menu :D")
            else:
                if i==len(Datos[1]["Personas"])-1:
                    input("D:")
                
    elif opcion=="4":
        print(input("Salir"))
        Booleano1=False
    else:
        input("Elige una opcion valida para poder continuar con el menu :D")