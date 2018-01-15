class Carro():

    # Constructor
    def __init__(self):
        self.__largoChasis = 250 #Variable encapsulada
        self.__anchoChasis = 120 #Variable encapsulada
        self.__llantas = 4 #Variable encapsulada
        self.__enMarcha = False #Variable encapsulada

    def arrancar(self, arranca):
        self.__enMarcha = arranca

        if(self.__enMarcha):
            chequeo = self.__chequeo_interno()

        if (self.__enMarcha and chequeo):
            return "El carro esta en marcha"
        elif(self.__enMarcha and chequeo==False):
            return "No paso el chequeo, no se puede arrancar"
        else:
            return "El carro esta parado"

    def estado(self):
        print 'El carro tiene ', self.__llantas, ' llantas. Un ancho de ', self.__anchoChasis, ' y un largo de ', self.__largoChasis

    def __chequeo_interno(self): #Metodo encapsulado
        print "Realizando chequeo interno"

        self.gasolina = "Ok"
        self.aceite = "Mal"
        self.puertas = "Cerradas"

        if (self.gasolina == "Ok" and self.aceite == "Ok" and self.puertas == "Cerradas" ):
            return True
        else:
            return False

miCarro = Carro()
print miCarro.arrancar(True)
miCarro.estado()

print "\n---------Ahora se creara el segundo objeto---------"

miCarro1 = Carro()
print miCarro1.arrancar(False)
miCarro1.estado()