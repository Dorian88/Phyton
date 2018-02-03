nombreUsuario = input("Introduce tu nombre de usuario: ")

print "El nombre es: ", nombreUsuario.upper()
print "El nombre es: ", nombreUsuario.lower()
print "El nombre es: ", nombreUsuario.capitalize()

edad = input("Introduce la edad: ")

while(edad.isdigit() == False):
    print "Por favor introduce un valor numerico."
    edad = input("Introduce la edad: ")

if(int(edad)<18):
    print "No Puede pasar"
else:
    print "Puede pasar"