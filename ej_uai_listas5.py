edificios=[]
oficinas=[]
print("Bienvenido a nuestro sistema")
wea=True
while wea:
    opc=input("[1] para ingresar edificios y sus oficinas [2] para ver la información ordenada [3] para salir del programa \n")
    if opc=="1":
        edificio=input("Ingrese nombre de edificio:\n")
        edificios.append(edificio)
        oficina=int(input("Ingrese cantidad de oficinas del edificio:\n"))
        oficinas.append(oficina)
    elif opc=="2":
        for i in range(len(edificios)):
            print("el",edificios[i],"tiene una cantidad de" ,oficinas[i], "oficinas")
        print("Hay un total de", len(edificios), "edificios y una cantidad total de", sum(oficinas), "oficinas")
    elif opc=="3":
        print("Hasta pronto y gracias por usar nuestro sistema")
        wea=False
    else:
        print("Ingrese valores válidos")