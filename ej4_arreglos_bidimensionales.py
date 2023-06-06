import numpy as np
listaletras=[]
contadorvocales=0
for i in range(16):
    letra=str(input("Ingrese una letra:\n"))
    listaletras.append(letra)
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        contadorvocales=contadorvocales+1
arreglo1=np.array([[listaletras[0],listaletras[1],listaletras[2],listaletras[3]],
                   [listaletras[4],listaletras[5],listaletras[6],listaletras[7]],
                   [listaletras[8],listaletras[9],listaletras[10],listaletras[11]],
                   [listaletras[12],listaletras[13],listaletras[14],listaletras[15]]])
print("Estas fueron las letras que ingresó:")
print(arreglo1)
print("La cantidad de vocales que ingresó fue:", contadorvocales, "vocales")

