def Calcular_Iva():
    iva=precio*0.19
    return iva
def Descuento():
    valorfinal=precio-rebaja
    return valorfinal
def Calcular_Imc():
    imc=peso/estatura**2
    return imc
print("BIENVENIDO AL MENÚ")
wea=True
while wea:
    opc=input("[1] para calcular iva y aplicar descuento [2] para saber su IMC [3] para salir del programa\n")
    if opc=="1":
        precio=int(input("Ingrese el precio del producto:\n"))
        print("El IVA es:", Calcular_Iva())
        rebaja=int(input("Ingrese el descuento que se le aplicará al producto:\n"))
        print("El valor final con descuento aplicado es:", Descuento())

    elif opc=="2":
        peso=float(input("Ingrese su peso:\n"))
        estatura=float(input("Ingrese su estatura (en metros):\n"))
        print("Su IMC es:", Calcular_Imc())

    elif opc=="3":
        print("Hasta pronto y gracias por utilizar nuestro programa")
        wea=False
