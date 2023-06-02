user_1="Calfun"
pass1="1234"
user_2="Pedro"
pass2="A4B7"
usuario=str(input("Ingrese su nombre por favor"))
contrasena=str(input("Ingrese su contraseña por favor"))
if (usuario==user_1 and contrasena==pass1) or (usuario==user_2 and contrasena==pass2):
    print ("Bienvenido")
else:
    print("Usuario o contraseña invalido")