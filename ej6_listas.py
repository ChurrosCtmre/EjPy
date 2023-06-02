##En el ejercicio no especificaba cuantos elementos tenía que tener lista así que reciclo la del ejercicio 4
import random 
lista=[random.randint(1,100) for i in range(20)]
print("Lista generada aleatoriamente:", lista)
nmayor=max(lista)
nmenor=min(lista)
print("El número mayor es:", nmayor)
print("El número menor es:", nmenor)