import numpy as np
import random as rd
wea=True
while wea:
    num=int(input("Ingrese el número que crea que está dentro de la lista de diez números del uno al cien generados al azar:\n"))
    arreglo=np.array=([rd.randint(1,100), rd.randint(1,100), rd.randint(1,100), rd.randint(1,100), rd.randint(1,100), rd.randint(1,100), rd.randint(1,100), rd.randint(1,100), rd.randint(1,100), rd.randint(1,100)])
    if num>=1 and num<=100:
        print("Esta es la lista de números del uno al cien generada aleatoriamente:")
        print(arreglo)
        if num==arreglo[0] or num==arreglo[1] or num==arreglo[2] or num==arreglo[3] or num==arreglo[4] or num==arreglo[5] or num==arreglo[6] or num==arreglo[7] or num==arreglo[8] or num==arreglo[9]:
            print("Felicidades ha adivinado un número!!!!")
        else:
            print("Lo sentimos, no ha adivinado ninguno de los diez números")
            opc=input("Desea volver a intentarlo? [Si][No]:\n")
            if opc=="Si":
                continue
            elif opc=="No":
                print("Hasta pronto y gracias por jugar")
                wea=False
            else:
                print("Ingrese opción válida")
    else:
        print("Ingrese valores válidos")