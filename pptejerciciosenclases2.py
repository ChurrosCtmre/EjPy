import random as rd
import numpy as np
n1=int(input("Ingrese un número entre 3 y 6: (este número será usado para las filas de la matriz)\n"))
if n1>=3 and n1<=6:
    n2=int(input("Ingrese otro número entre 3 y 6: (este número será usado para las columnas de la matriz)\n"))
    if n2>=3 and n2<=6:
        arreglo1=[[rd.uniform(0.0,5.0)for i in range(n2)] for i in range(n1)]
        print("El arreglo poblado es:")
        for fila in arreglo1:
            print(fila)
        suma_filas=[sum(fila)for fila in arreglo1]
        print("")
        print("La suma por filas es:")
        for suma in suma_filas:
            print(suma)
        promedio_columnas=[sum(columna)/ n1 for columna in zip(*arreglo1)]
        print("")
        print("El promedio por columnas es:")
        for promedio in promedio_columnas:
            print(promedio)
    else:
        print("Ingrese valores válidos")
else:
    print("Ingrese valores válidos")

