import random
lista=[random.randint(1,49) for i in range(5)]
print("Ingrese sus cinco números de la suerte: (números participantes son del 1 al 49)")
n1=int(input("Ingrese el primer número:\n "))
n2=int(input("Ingrese el segundo número:\n "))
n3=int(input("Ingrese el tercer número:\n "))
n4=int(input("Ingrese el cuarto número:\n "))
n5=int(input("Ingrese el quinto número:\n "))
num_jugador=[n1,n2,n3,n4,n5]
set1=set(lista)
set2=set(num_jugador)
if (n1>=1 and n1<=49) and (n2>=1 and n2<=49) and (n3>=1 and n3<=49) and (n4>=1 and n4<=49) and (n5>=1 and n5<=49):
    print("Los números sorteados fueron:", " ", lista)
    print("Los números que escogió usted fueron:", " ", num_jugador)
    aciertos=set1.intersection(set2)
    if len(aciertos)==5:
        print("Felicidades, has ganado en esta ronda")
    else:
        print("Lo siento, no has ganado en esta ronda")
else:
    print("Ingrese valores válidos por favor")