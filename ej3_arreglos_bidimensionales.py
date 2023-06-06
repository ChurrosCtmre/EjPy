import numpy as np
import random as rd
arreglo1=np.array([[rd.randint(1,100),rd.randint(1,100),rd.randint(1,100),rd.randint(1,100),rd.randint(1,100)],
                   [rd.randint(1,100),rd.randint(1,100),rd.randint(1,100),rd.randint(1,100),rd.randint(1,100)],
                   [rd.randint(1,100),rd.randint(1,100),rd.randint(1,100),rd.randint(1,100),rd.randint(1,100)],
                   [rd.randint(1,100),rd.randint(1,100),rd.randint(1,100),rd.randint(1,100),rd.randint(1,100)]])
print(arreglo1)
print("el número más alto del arreglo es:", np.max(arreglo1))
print("El número más bajo del arreglo es:", np.min(arreglo1))

#Tuve problemas con esta parte por el tema de que la matriz no es
# cuadrada por ende el código que sabía para realizar este caso no me sirve.
#Básicamente no sé de que forma ver la diagonal principal en una matriz no cuadrada.

#El sgte. código es la solución que me mostró ChatGPT:

#print("Los elementos de la diagonal principal son:")
#print("La suma de los elementos de la diagonal principal es:")
#suma_diagonal=sum(arreglo1[i,i] for i in range(min(4,5)))
#print(suma_diagonal)
