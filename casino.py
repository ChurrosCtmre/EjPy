print ("Bienvenido a casino online, ingrese su nombre y edad para empezar a ganar")
nombre=str(input("ingrese su nombre:"))
edad=int(input("ingrese su edad:"))
if edad<18:
    print("Lo sentimos,", nombre, ", usted es menor de edad por ende no puede ingresar a este sitio")
elif edad>=70:
    print("Bienvenido,", nombre, ", No se gaste la jubilacion")
else:
    print("Bienvenido,", nombre, ", Que le vaya bien")