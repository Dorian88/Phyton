import math
print ("-----Usando el ciclo for-----")

for i in [1, 2, 3]:
    print ("Hola")

for estacionesAnos in ["primavera", "verano", "otono", "invierno"]:
    print (estacionesAnos)

print ("\nComprobar la direccion de un correo electronico")
#Perfeccionar el codigo
contador = 0
miEmail = raw_input("Digite su correo electronico: ")

for i in miEmail:
    if (i == "@" or i == "."):
        contador = contador + 1

if contador <> 0:
    print("El email es correcto")
else:
    print("El email no es correcto")

for i in range(0, 50, 3):
    print "El valor de la variable es: ", i

print ("Variante de la validacion del correo electronico")

valido = False

email = raw_input("Ingrese su correo electronico")

for i in range(len(email)):
    if email[i]=="@":
        valido = True

if valido:
    print ("El correo es correcto")
else:
    print ("El correo es no correcto")

print ("-----Usando el ciclo while-----")

i = 1

while i <= 10:
    print("Ejecucion " + str(i))
    i = i+1
print ("Termino la ejecucion")

edad = int (input("Introduce su edad por favor: "))

while edad < 0 or edad > 120:
    print ("Has ingresado una edad invalidad. Vuelve a intentarlo")
    edad = int(input("Introduce su edad por favor: "))

print ("Gracias por colaborar. Puedes pasar")
print ("Edad del aspirante " + str(edad))

print("Programa para calcular la raiz  cuadrada")

numero = int (input("Ingrese un numero: "))
intentos = 0

while numero < 0:
    print ("No se puede calcular la raiz de un numero negativo")
    if intentos == 2:
        print ("Has excedido el numero de intentos. El programa ha terminado")
        break
    numero = int(input("Ingrese un numero: "))
    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print ("La raiz cuadrada de: " + str(numero) + " es " + str(solucion))

print ("-----Usando continue, pass y else-----")

for letra in "Python":
    if letra == "h":
        continue
    print ("Viendo la letra: " + letra)

nombre = "Pildoras informaticas"
contador = 0

for i in nombre:
    if i == " ":
        continue
    contador += 1
print(contador)

email = raw_input("Ingrese su email, por favor: ")

for i in email:
    if i == "@":
        arroba = True
        break
else:
    arroba = False

print (arroba)