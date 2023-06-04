vendedores=[]
librosv=[]
mvvendedor=""
wea=True
print("Bienvenido a nuestro sistema")
while wea:
    print("[1] para ingresar su nombre y cantidad de libros vendidos [2] para ver la informacion ordenada [3] para salir del programa")
    opc=input("Ingrese la opción deseada:\n")
    if opc=="1":
        vendedor=input("Estimado vendedor, ingrese su nombre:\n")
        vendedores.append(vendedor)
        clibros=int(input("Ingrese la cantidad de libros que ha vendido:\n"))
        librosv.append(clibros)
    elif opc=="2":
        for i in range(len(vendedores)):
            print(vendedores[i], "vendió", librosv[i], "libros")
        print(librosv, "libros")
        print("El total de libros vendidos es:", sum(librosv))
        maxlibros=max(librosv)
        a=librosv.index(maxlibros)
        mvvendedor=vendedores[a]
        print("El mejor vendedor fue:", mvvendedor, "con un total de", maxlibros, "libros vendidos")
    elif opc=="3":
        print("Hasta pronto y gracias por usar nuestro sistema")
        wea=False
    else:
        print("Ingrese valores válidos")


