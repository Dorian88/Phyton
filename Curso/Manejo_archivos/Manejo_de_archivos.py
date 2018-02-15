from io import open

#Crear y escribir un archivo
'''archivoExterno = open("archivo.txt", "w")
frase = unicode("el conocimiento es saber que un tomate es una fruta; \nsabiduria es no ponerlo en una ensalada de frutas")
archivoExterno.write(frase)
archivoExterno.close()'''

#Leer informacion de un archivo
archivoExterno = open("archivo.txt", "r")
texto = archivoExterno.read()
archivoExterno.close()
print texto
print "\n"

#Leer la informacion de un archivo linea a linea
archivoExterno = open("archivo.txt", "r")
lineasTexto = archivoExterno.readlines()
archivoExterno.close()
print lineasTexto
print "\n"

#Agregar informacion al archivo
archivoExterno = open("archivo.txt", "a")
#archivoExterno.write(unicode("\nNo discutas con un idiota."))
archivoExterno.close()

#Ubicacion del puntero en el archivo
archivoExterno = open("archivo.txt", "r")
print archivoExterno.read()
print "\n"
archivoExterno.seek(0) #Posiciona el puntero al inicio del archivo
print archivoExterno.read()
print "\n"
archivoExterno.seek(11)
print archivoExterno.read()
print "\n"
archivoExterno.seek(len(archivoExterno.read())/2)
print archivoExterno.read()
archivoExterno.close()

#Lectura y Escritura
archivoExterno = open("archivo.txt", "r+")
#print archivoExterno.readlines()
archivoExterno.write(unicode("Se escribe en el archivo"))
lista_texto = archivoExterno.readlines()
lista_texto[1]= "Esta linea ha sido incluida desde el exterior \n"
lista_texto.seek(0)
archivoExterno.writelines(lista_texto)
archivoExterno.close()