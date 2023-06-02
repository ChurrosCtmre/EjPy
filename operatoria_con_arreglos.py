import numpy as np

arreglo1=np.array([45,5,2,1,12,34])
print(arreglo1)
for x in range(len(arreglo1)): #len es la función para ver la longitud de una lista
    print(arreglo1[x])
arreglo2=np.arange(6)
print(arreglo2)
print(arreglo1[::2])