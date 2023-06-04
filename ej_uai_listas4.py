prueba1=[]
prueba2=[]
nombres=[]
azules=[]
rojos=[]
azul1=[]
rojo1=[]
azul2=[]
rojo2=[]
wea=True
print("Bienvenido a nuestro sistema")
while wea:
    opc=input("[1]para ingresar sus notas al sistema [2]para ver los datos ordenados [3]para salir del programa\n")
    if opc=="1":
        nombre=input("Ingrese nombre del estudiante:\n")
        nombres.append(nombre)
        nota1=float(input("Ingrese la nota del estudiante en la primera prueba:\n"))
        prueba1.append(nota1)
        nota2=float(input("Ingrese la nota del estudiante en la segunda prueba:\n"))
        prueba2.append(nota2)
        if nota1>=4:
            azules.append(nota1)
            azul1.append(nota1)
        else:
            rojos.append(nota1)
            rojo1.append(nota1)
        if nota2>=4:
            azules.append(nota2)
            azul2.append(nota2)
        else:
            rojos.append(nota2)
            rojo2.append(nota2)
    elif opc=="2":
        for i in range(len(prueba1)):
            print(nombres[i], "se sacó un", prueba1[i], "en la primera prueba y en la segunda se sacó un", prueba2[i])
        print("El estudiante con mejor nota en la primera prueba fue:", nombres[i], "con un", max(prueba1))
        print("El estudiante con mejor nota en la segunda prueba fue:", nombres[i], "con un", max(prueba2))
        print("El promedio general de las notas en la primera prueba fue un:", (sum(prueba1)/len(prueba1)))
        print("El promedio general de las notas en la segunda prueba fue un:", (sum(prueba2)/len(prueba2)))
        print("Hay una cantidad de", len(azul1), "notas azules y una cantidad de", len(rojo1), "notas rojas en la primera prueba")
        print("Hay una cantidad de", len(azul2), "notas azules y una cantidad de", len(rojo2), "notas rojas en la segunda prueba")

    elif opc=="3":
        print("Hasta pronto y gracias por usar nuestro sistema")
        wea=False
    else:
        print("Ingrese valores válidos")

            

