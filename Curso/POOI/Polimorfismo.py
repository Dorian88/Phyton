class Carro1():
    def desplazamiento(self):
        print "Me desplazo utilizando 4 llantas"

class Moto():
    def desplazamiento(self):
        print "Me desplazo utilizando 2 llantas"

class Camion():
    def desplazamiento(self):
        print "Me desplazo utilizando 6 llantas"

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Camion()
desplazamientoVehiculo(miVehiculo)
miVehiculo=Carro1()
desplazamientoVehiculo(miVehiculo)
miVehiculo=Moto()
desplazamientoVehiculo(miVehiculo)