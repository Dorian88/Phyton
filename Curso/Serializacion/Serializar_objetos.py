import pickle

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print "Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena

carro1 = Vehiculos("Mazda", "MX5")
carro2 = Vehiculos("Seat", "Leon")
carro3 = Vehiculos("Reanult", "Megane")

carro = [carro1, carro2, carro3]

archivo = open("losCarros", "wb")
pickle.dump(carro, archivo)
archivo.close()
del (archivo)

"""archivoArpetura = open("losCarros", "rb")
misCarros = pickle.load(archivoArpetura)
archivoArpetura.close()
for c in misCarros:
    print c.estado()"""