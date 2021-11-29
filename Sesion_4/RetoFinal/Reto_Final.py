import Tarjeta as t ,Usuario as u
"""Inicializa el programa para el reto final"""

#Datos de Prueba
cliente = u.Usuario("Juanito")
cliente.Adicionar(t.Tarjeta("visa",2,1000,5,55))
cliente.Adicionar(t.Tarjeta("master",3,3000,100,99))

print(cliente)
for tarjeta in cliente.tarjetas:
  tarjeta.calcular()
  tarjeta.reporte()

cliente.Eliminar("master")

print(cliente)
for tarjeta in cliente.tarjetas:
  tarjeta.calcular()
  tarjeta.reporte()