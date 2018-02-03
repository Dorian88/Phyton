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

class Moto(Vehiculos):
        hCaballito=""

        def Caballito(self):
            self.hCaballito="Voy haciendo caballito"

        def estado(self):
            print "Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",\
                self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hCaballito

class Furgoneta(Vehiculos):

    def cargar(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super(self).__init__(marca, modelo)
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando="cargando"