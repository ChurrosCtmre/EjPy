import numpy as np
import random
arreglo1=np.array([random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)])
arreglo2=arreglo1[:].copy()
print(arreglo1)

print(f"El valor más alto del arreglo es:{max(arreglo2)}")
print(f"El valor más bajo del arreglo es:{min(arreglo2)}")
print(f"La suma de todos los valores del arreglo es:{arreglo2.sum()}")
print(f"El promedio de todos los valores del arreglo es:{arreglo2.mean()}")
print(arreglo2)
