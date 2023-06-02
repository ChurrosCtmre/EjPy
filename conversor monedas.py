print("Bienvenido al programa conversor de pesos a dolar o a yen y viceversa:")
peso=1
dolar=1
yen=1
conversion=(input("Cual es la moneda que desea convertir a otra? (dolar, peso o yen)"))
destino=(input("hacia que moneda desea convertirla? (peso, dolar o yen)"))
if conversion=="peso" and destino=="dolar":
    peso=float(input("ingrese la cantidad de pesos que desea convertir a dolares"))
    print("La cantidad de pesos ingresada es igual a :", peso*0.0013, "dolares")
elif conversion=="dolar"and destino=="peso":
    dolar=float(input("ingrese la cantidad de dolares que desea convertir a pesos"))
    print("La cantidad de dolares ingresada es igual a :", dolar*794.73, "pesos")
elif conversion=="peso" and destino=="yen":
    peso=float(input("ingrese la cantidad de pesos que desea convertir a yenes"))
    print("La cantidad de pesos ingresada es igual a:", peso*0.17 ," yenes")
elif conversion=="yen"  and destino=="peso":
    yen=float(input("ingrese la cantidad de yenes que desea convertir a pesos:"))
    print("la cantidad de yenes ingresada es igual a:", yen*5.93 ," pesos")
elif conversion=="dolar" and destino=="yen":
    dolar=float(input("ingrese la cantidad de dolares que desea convertir a yenes:"))
    print("la cantidad de dolares ingresada es igual a:", dolar*134.06, " yenes")
elif conversion=="yen" and destino=="dolar":
    yen=float(input("ingrese la cantidad de yenes que desea convertir a dolares:"))
    print("la cantidad de yenes ingresada es igual a:", yen*0.0075, " dolares")
else:
    print("no se puede realizar la conversion")