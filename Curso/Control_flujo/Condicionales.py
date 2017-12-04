print ("-----Usando la instruccion if-----")
def evaluacion(nota):
    valoracion = "Aprobado"
    if nota < 6:
        valoracion = "Reprobado"
    return valoracion

print(evaluacion(4))
print(evaluacion(7))

print("Valor ingresado por teclado ")
nota_alumno = input("Ingrese la nota del alumno: ")
print(evaluacion(nota_alumno))

print ("\n-----Usando la instruccion if/else-----")
print ("Verificacion de acceso")

edad_usuario = input("Ingrese su edad: ")
if edad_usuario < 18:
    print ("No puede entrar")
else:
    print ("Puede entrar")

print ("\n-----Usando la instruccion elif-----")
print ("Verificacion de acceso")

edad_usuario = input("Ingrese su edad: ")
if edad_usuario < 18:
    print ("No puede entrar")
elif edad_usuario > 100:
    print ("Edad incorrecta")
else:
    print ("Puede entrar")

print ("\n-----Concatenacion de operadores de comparaciones-----")
edad = 7

if 0<edad < 100:
    print("Edad correcta")
else:
    print("Edad incorrecta")

salario_presidente = input("Ingrese el salario del presidente: ")
salario_director = input("Ingrese el salario del director: ")
salario_jefe_area = input("Ingrese el salario del jefe de area: ")
salario_administrativo = input("Ingrese el salario del administrativo ")

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print ("Todo funciona bien")
else:
    print ("Algo esta fallando")

print ("\n-----Practicando los condicionales-----")

print ("\nPrograma de becas ano 2017")
dist_escuela = int(input("Ingrese la distancia a la escuela en Km: "))
print (dist_escuela)

num_hermanos = int(input("Cuantos hermanos tienes?: "))
print (num_hermanos)

salario_familiar = int(input("Ingrese el salario anual bruto: "))
print (salario_familiar)

if dist_escuela > 40 and num_hermanos > 2 or salario_familiar <= 9600000:
    print ("Tienes derecho a la beca")
else:
    print ("No tienes derecho a la beca")

print ("\n-----Usando el operador in-----")

print ("\nListado de cursos electivos para ingenieria de sistemas en el ano 2017")

print ("\nIngenieria Web")
print ("Calidad de Software")
print ("Computacion Movil")

opcion = raw_input("Escriba la asignatura escogida: ")

asignatura = opcion.lower()

if asignatura in ("ingenieria web", "calidad de software", "computacion movil"):
    print ("Escogio el curso: " + asignatura)
else:
    print ("El curso no se puede matricular")