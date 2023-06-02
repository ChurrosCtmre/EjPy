wea=True
while wea:
        
    tabla=int(input("Ingrese el número del cual desea sacar su tabla de multiplicar del 1 al 10:\n"))
    resultados=[]
    for i in range(1,11):
        resultado=tabla*i
        resultados.append(resultado)
    print(resultados)
    lista_ordenada=resultados
    lista_ordenada.sort()
    print("lista ordenada ascendemente: ", lista_ordenada)
    lista_ordenada.sort(reverse=True)
    print("Lista ordenada descendentemente:", lista_ordenada)
    opcion=str(input("Ingrese si desea seguir haciendo operaciones o salir (Salir/Continuar)\n"))
    if opcion=="Salir":
        wea=False
        print("Hasta pronto, gracias por usar nuestro programa")
    elif opcion=="Continuar":
        wea=True
    else:
        print("Ingrese opciones válidas")
