print("-----------------------MENÚ-------------------------")
pi=3.14
wea=True
while wea:
    opc=input(" Ingrese [1] para calcular el área de un círculo [2] para calcular el perímetro de un cuadrado:\n")
    if opc=="1":
        radio=float(input("Ingrese medida del radio del círculo:\n"))
        areacircle=((radio**2)*pi)
        print("El área del círculo es:", areacircle)
        opc2=input("Desea seguir realizando operaciones o salir del programa [Salir][Seguir]\n")
        if opc2=="Salir":
            print("Hasta pronto y gracias por utilizar nuestro programa")
            wea=False 
        elif opc2=="Seguir":
            continue        
    elif opc=="2":
        ladocuadrado=float(input("Ingrese medida de un lado del cuadrado:\n"))
        perimetrocuadrado=ladocuadrado*4
        print("El perimetro del cuadrado es:", perimetrocuadrado)
        opc2=input("Desea seguir realizando operaciones o salir del programa [Salir][Seguir]\n")
        if opc2=="Salir":
            print("Hasta pronto y gracias por utilizar nuestro programa")
            wea=False 
        elif opc2=="Seguir":
            continue
    else:
        print("Ingrese opción válida")