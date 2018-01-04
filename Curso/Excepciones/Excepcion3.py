def evaluaEdad(edad):
    if edad < 0:
        raise TypeError ("No se permiten edades negativas")
    if edad < 20:
        return "eres muy joven"
    elif edad < 40:
        return "eres joven"
    elif edad < 60:
        return "eres maduro"
    elif edad < 100:
        return "cuidate..."

print (evaluaEdad(15))

print ("----------Otro ejemplo: Calcular la raiz cuadrada de un numero----------")
import math

def calculaRaiz(num1):
    if num1 < 0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)

op1=(int(input("Introduce un numero: ")))

try:
    print(calculaRaiz(op1))
except ValueError as ErrorNumeroNegativo:
    print("ErrorNumeroNegativo")

print("Programa terminado")
