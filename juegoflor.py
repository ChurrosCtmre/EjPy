import random

ramita = ["mucho", "poco", "nada"]

while True:
    seleccion = ramita[random.randint(0, 2)]
    print("Te quiere", seleccion)
    if seleccion == "mucho":
        print("Felicidades! Te quiere mucho!")
    opcion = input("¿Quieres seguir jugando? (s/n): ")
    if opcion == "n":
        break
    elif opcion != "s":
        print("Opción no válida")
        continue


