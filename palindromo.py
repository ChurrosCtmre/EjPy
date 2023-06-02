palabra=str(input("Escriba una palabra para saber si es palíndromo o no:\n"))
alreves="".join(reversed(palabra))
if palabra==alreves:
    print("La palabra que ingresó, efectivamente, es un palíndromo")
else:
    print("La palabra que ingresó no es un palíndromo")