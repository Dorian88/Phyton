import pickle

#Serializacion de colecciones
lista_nombres = ["Dorian", "Diana", "Jorge", "Maria", "Pedro"]
archivo_binario = open("lista_nombres", "wb")

pickle.dump(lista_nombres, archivo_binario)
archivo_binario.close()
del(archivo_binario)

archivo = open("lista_nombres", "rb")
lista = pickle.load(archivo)
print lista