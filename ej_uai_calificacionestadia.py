import time   
nombres_huespedes=[]
numeroreserva=[]
respevegeneral=[]
respevdesayuno=[]
respcambiohab=[]
respevrecepcion=[]
respevaseo=[]
respcomentariosadici=[]
print("Responda nuestra encuesta por favor, nos interesa muchísimo saber que le pareció su estadía en el hotel")
numhuespedesresp=int(input("¿Cuántos clientes responderan la encuesta?:\n"))
for i in range(numhuespedesresp):
    nombre=str(input("Ingrese su nombre para empezar la encuesta por favor:\n"))
    nombres_huespedes.append(nombre)
    numreserva=str(input("Ingrese su número de reserva por favor:\n"))
    numeroreserva.append(numreserva)
    opc=str(input("[1] para iniciar encuesta\n"))
    if opc=="1":
        resp1=str(input("¿Cómo evalúa la calidad de su estadía? \n evalúe con una calificación entre 1 y 7 donde 1 es la peor y 7 la mejor\n"))
        respevegeneral.append(resp1)
        resp6=str(input("¿Cuántas veces tuvo que cambiarse de habitación?\n"))
        respcambiohab.append(resp6)
        resp2=str(input("¿Tuvo la oportunidad de nuestro desayuno? [Si] [No]\n"))
        if resp2=="Si":
            resp3=str(input("Por favor evalúe la calidad de la misma forma que evaluó anteriormente:\n"))
        elif resp2=="No":
            print("Una pena que no haya podido probar nuestro desayuno.")
        else: 
            print("Ingrese valores válidos")
        resp4=str(input("¿Cómo calificaría el servicio en recepción?\n"))
        respevrecepcion.append(resp4)
        resp5=str(input("¿Cómo calificaría la limpieza y aseo en general?\n"))
        respevaseo.append(resp5)
        coment=str(input("Ingrese algún comentario adicional que desee:\n"))
        respcomentariosadici.append(coment)
    else:
        print("Ingrese opciones válidas")
print("Estos son los resultados de la encuesta:")
time.sleep(1)
print("Cargando resultados...")
time.sleep(1.5)
print("La encuesta ha sido respondida por un total de",len(nombres_huespedes),"Personas" )
print("Los nombres de los huéspedes son:", (nombres_huespedes))
print("Los números de reserva son:", (numeroreserva))
print("Las respuestas de evaluación general fueron:", (respevegeneral))
print("Los clientes tuvieron que cambiarse de habitación esta cantidad de veces:", (respcambiohab))
print("Los clientes que probaron el desayuno lo evaluaron de esta forma:", (respevdesayuno))
print("La evaluación de recepción quedó de esta forma:", (respevrecepcion))
print("Las evaluaciones del servicio de aseo y limpieza fueron estas:", (respevaseo))
print("Los comentarios adicionales fueron estos:", (respcomentariosadici))