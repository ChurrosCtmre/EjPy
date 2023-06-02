sw=1
listaNotas=[]
print("presione 1 para ingresar sus notas")
print("presione cualquier tecla para salir")
op=int(input("Seleccione opcion"))
if(op==1):
    while sw==1:
        try:
            print("____________________________________________")
            nota=int(input("Incorpore su nota, si desea salir, presione 0:"))
            if(nota!=0):
                listaNotas.append(nota)
                print(f"Sus notas cargadas son: {listaNotas}")
                print(f"Cantidad de notas cargadas: {sum(listaNotas)}")
                print(f"Su promedio de notas es: {sum(listaNotas)/len(listaNotas)}")
            else:
                print("Adios")
                sw=0
        except:
            print("Ingreso erróneo")
else:
    print("Adios")
