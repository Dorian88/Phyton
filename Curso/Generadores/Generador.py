print ("----------Yield----------")
def generaPares(limite):
    num = 1

    while num < limite:
        yield num*2
        num += 1



devuelvePares = generaPares(10)

#for i in devuelvePares:
#    print(i)

print (next(devuelvePares))
print ("Va mas codigo...")
print (next(devuelvePares))
print ("Va mas codigo...")
print (next(devuelvePares))
print ("Va mas codigo...")

print ("----------Yield from solo para versiones de phyton 3.3 o mayores----------")
def ciudades (*ciudades):
    for elemento in ciudades:
        yield elemento
        #yield from elemento

ciudades_devueltas = ciudades("Medellin", "Bogota", "Bucaramanga", "Villavicencio")

print (next(ciudades_devueltas))
print (next(ciudades_devueltas))