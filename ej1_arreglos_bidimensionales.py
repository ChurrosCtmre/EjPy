import numpy as np
import random as rd
arreglo1=np.array([[rd.randint(1,100),rd.randint(1,100),rd.randint(1,100)]
                   ,[rd.randint(1,100),rd.randint(1,100),rd.randint(1,100)]
                   ,[rd.randint(1,100),rd.randint(1,100),rd.randint(1,100)]])
print("El primer arreglo es:")
print(arreglo1)
arreglo2=np.array([[9,8,7],[6,5,4],[3,2,1]])
print("El segundo arreglo es:")
print(arreglo2)
arreglo3=arreglo1*arreglo2
print("La multiplicación de los dos arreglos anteriores es:")
print(arreglo3)