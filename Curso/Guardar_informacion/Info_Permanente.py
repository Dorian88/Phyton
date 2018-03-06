import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print "Se ha creado una persona nueva con el nombre de ", self.nombre

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
    personas = []

    def __init__(self):
        ListaDePersona = open("Archivo_Externo.txt", "ab+")
        ListaDePersona.seek(0)

        try:
            self.personas = pickle.load(ListaDePersona)
            print "Se cargaron {} personas del archivo externo".format(len(self.personas))
        except:
            print ("El archivo esta vacio")
        finally:
            ListaDePersona.close()
            del(ListaDePersona)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonas()

    def mostrarPersonas(self):
        for p in self.personas:
            print p

    def guardarPersonas(self):
        listaDePersona = open("Archivo_Externo.txt", "wb")
        pickle.dump(self.personas, listaDePersona)
        listaDePersona.close()
        del(listaDePersona)

    def mostrarInfoArchivoExterno(self):
        print "La informacion del archivo externo es la siguiente: "
        for p in self.personas:
            print p

miLista = ListaPersonas()
persona = Persona("Diana", "Femenino", "29")

miLista.agregarPersonas(persona)
miLista.mostrarPersonas()