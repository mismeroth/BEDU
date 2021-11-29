from Reto_1 import Vehiculo as v

avion = v.VehiculoAereo("Rojo",4,"Avion","Boeing","2Ton","10","2 Turbinas")
print(avion)
avion.movimiento()

carro = v.VehiculoTerrestre("Rojo",4,"Avion","Mercedez","400Kilos","4","2000cc")
print(carro)
carro.movimiento()