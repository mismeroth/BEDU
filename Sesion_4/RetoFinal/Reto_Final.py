import Tarjeta as t ,Usuario as u
"""Inicializa el programa para el reto final"""

#Instancia de la clase tarjeta para pasarla por parametro
cliente = u.Usuario("Usuario A")
cliente.Adicionar(t.Tarjeta("visa",2,1000,5))
cliente.Adicionar(t.Tarjeta("master",3,3000,100))

print(cliente)
for tarjeta in cliente.tarjetas:
  tarjeta.calcular()
  tarjeta.reporte()