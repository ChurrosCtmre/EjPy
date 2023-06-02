lista=[]
zero=True
while zero:
    opc=int(input("Ingrese número entero, si ingresa un cero se detiene"))
    if opc!=0:
        lista.append(opc)
        continue
    else:
        zero=False
        print("Los números que ingresó fueron:", lista)