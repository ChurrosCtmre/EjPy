lista=[]
for i in range(3):
    nombre=str(input("Ingrese un nombre:\n"))
    lista.append(nombre)
print("Los nombres ingresados fueron:",lista)
nlargo=max(lista,key=len) #El parámetro "key=len" indicarán al programa ordenar la lista de nombres por longitud, del más pequeño al más largo.
print("El nombre más largo de la lista es:", nlargo)

