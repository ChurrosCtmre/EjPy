import numpy as np
import random as rd
matriz=np.array([[rd.randint(0,100), rd.randint(0,100), rd.randint(0,100)],
                 [rd.randint(0,100), rd.randint(0,100), rd.randint(0,100)],
                 [rd.randint(0,100), rd.randint(0,100), rd.randint(0,100)]])
print(matriz)
print(f"El número más alto del arreglo es:{np.max(matriz)}")
print(f"El número más bajo del arreglo es:{np.min(matriz)}")
print(f"El promedio de los elementos del arreglo es:{np.mean(matriz)}")
print(f"La suma de los elementos del arreglo es:{np.sum(matriz)}")

#Mostrar solo los elementos de la diagonal principal
print("En este caso los elementos de la diagonal principal serían:\n", matriz[0,0],matriz[1,1], matriz[2,2])
for i in range(3):
        print(matriz[i,i])
