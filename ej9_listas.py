listanombres=[]
alo=True
while alo:
    opc=str(input("Ingrese nombres para almacernarlos en una lista o escriba NO para detener\n"))
    if opc!="NO":
        listanombres.append(opc)
        continue
    else:
        alo=False
        nombre_mas_corto=min(listanombres, key=len)
        print("El nombre más corto que se ingresó a la lista fue:", nombre_mas_corto, ",por ende, será eliminado de la lista")
        listanombres.remove(nombre_mas_corto)
        print("Gracias por usar nuestro sistema de almacenamiento, los nombres ingresados fueron:", listanombres)
