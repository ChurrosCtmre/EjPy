hombres=[]
mujeres=[]
wea=True
print("--------------------BIENVENIDO AL MENÚ---------------------------")
print("Bienvenido a nuestro sistema de almacenamiento")
while wea:
    opc=input("[1] para agregar usuario al listado [2] para ver el listado y [3] para salir del programa\n")
    if opc=="1":
        nombre=str(input("Ingrese su nombre:\n"))
        genero=str(input("Ingrese su genero: h/m\n"))
        if genero=="h":
            hombres.append(nombre)
        elif genero=="m":
            mujeres.append(nombre)
            continue
    elif opc=="3":
        print("Hasta pronto y gracias por usar nuestro servicio")
        wea=False
    elif opc=="2":
        hombres.sort()
        mujeres.sort()
        print("Nombres de los hombres ingresados ordenados alfabeticamente:", hombres)
        print("Nombres de las mujeres ingresados ordenados alfabeticamente: ", mujeres)
        print("La cantidad de hombres almacenados en el sistema es:",(len(hombres)))
        print("La cantidad de maracas almacenadas en el sistema es:",(len(mujeres)))
        if len(hombres)>len(mujeres):
            print("Hay mas hombres que mujeres")
        elif len(hombres)<len(mujeres):
            print("Hay mas mujeres que hombres")
        else:
            print("Hay la misma cantidad de hombres y mujeres")
    else:
        print("Ingrese valores válidos")