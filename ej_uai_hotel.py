import time
habitaciones=[]
ropacama=[]
jabon=[]
shampoo=[]
pantuflas=[]
batas=[]
habstandard=[]
habfamiliar=[]
habdeluxe=[]
habsuite=[]
habsupersuite=[]
print("-----------------Bienvenido al [HOTEL INFINITO]-----------------")
wea=True
while wea:
    opc=input("[1] para listar las habitaciones y sus categorias [2] para ingresar elementos al inventario  [3] para ver el listado de habitaciones y el inventario [4] para salir del programa\n")
    if opc=="1":
        wea2=True
        while wea2:
            aghab=int(input("Cuántas habitaciones habitaciones desea agregar?:\n"))
            habitaciones.append(aghab)
            cathab=input("Cuál es la categoría de las habitaciones [Standard][Familiar][Deluxe][Suite][Super Suite]\n")
            if cathab=="Standard":
                habstandard.append(aghab)
            elif cathab=="Familiar":
                habfamiliar.append(aghab)
            elif cathab=="Deluxe":
                habdeluxe.append(aghab)
            elif cathab=="Suite":
                habsuite.append(aghab)
            elif cathab=="Super Suite":
                habsupersuite.append(aghab)
            else:
                print("Ingrese opciones válidas")
            agregarhab=input("Desea seguir agregando habitaciones? [Si] [No]\n")
            if agregarhab=="Si":
                continue
            elif agregarhab=="No":
                print("A continuación volverá al menú principal")
                time.sleep(1.5)
                wea2=False
            else:
                print("Escoja una opción válida")

    elif opc=="2":
        wea3=True
        while wea3:
            agelementos=input("¿Qué elemento desea ingresar al inventario? [Ropa de cama][Jabon][Shampoo][Pantuflas][Batas de ducha]\n")
            if agelementos=="Ropa de cama":
                agalo=int(input("¿Cuánta ropa de cama necesita?:\n"))
                ropacama.append(agalo)
            elif agelementos=="Jabon":
                agalo=int(input("¿Cuánto jabón necesita?:\n"))
                jabon.append(agalo)
            elif agelementos=="Shampoo":
                agalo=int(input("¿Cuánto shampoo necesita?:\n"))
                shampoo.append(agalo)
            elif agelementos=="Pantuflas":
                agalo=int(input("¿Cuántas Pantuflas necesita?:\n"))
                pantuflas.append(agalo)
            elif agelementos=="Batas de ducha":
                agalo=int(input("¿Cuántas batas de ducha necesita?:\n"))
                batas.append(agalo)
            else:
                print("Ingrese opciones válidas")
            quewea=input("Desea seguir agregando elementos?[Si][No]\n")
            if quewea=="Si":
                continue
            elif quewea=="No":
                print("A continuación volverá al menú principal")
                time.sleep(1.5)
                wea3=False
            else:
                print("Ingrese opciones válidas")
            
    elif opc=="3":
        print("Cargando inventario...")
        time.sleep(2)
        print("Hay un total de", sum(habitaciones), "habitaciones y se dividen de esta forma:")
        print(sum(habstandard), "Habitaciones Standard")
        print(sum(habfamiliar), "Habitaciones Familiar")
        print(sum(habdeluxe), "Habitaciones Deluxe")
        print(sum(habsuite), "Habitaciones Suite")
        print(sum(habsupersuite), "Habitaciones Super Suite")
        print("Hay un total de ",sum(ropacama), "Ropa de cama")
        print("Hay un total de",sum(jabon), "Jabón")
        print("Hay un total de", sum(shampoo), "Shampoo")
        print("Hay un total de", sum(pantuflas), "Pantuflas")
        print("Hay un total de", sum(batas), "Batas de ducha")

    elif opc=="4":
        print("Hasta pronto y gracias por usar nuestro sistema de inventario")
        wea=False




