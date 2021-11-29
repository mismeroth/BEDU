import Tarjeta as t, Usuario as u
import TarjetaDB as tdb
"""Inicializa el programa para el reto final"""
##Crea Objetos de BBDD
objTarjeta = tdb.TarjetaDB()
objConn = objTarjeta.abrirConexion()
#objTarjeta.crearTablaTarjeta(objConn)
objTarjeta.inicializarTabla(objConn)
objConn.close()

######################################################
#Parte 1
######################################################
#Datos de Prueba

cliente = u.Usuario("Juanito")
cliente.Adicionar(t.Tarjeta("visa", 2, 1000, 5, 55))
cliente.Adicionar(t.Tarjeta("master", 3, 3000, 100, 99))
#cliente.Adicionar(t.Tarjeta_Servicios(5000,4000))

print(cliente)
for tarjeta in cliente.tarjetas:
    tarjeta.calcular()
    tarjeta.reporte()

######################################################
#Parte 2 -- DB
######################################################
#Se incluyo en la clase de tarjeta al Insersion
objTarjeta = tdb.TarjetaDB()
objConn = objTarjeta.abrirConexion()
objTarjeta.consultarTarjetas(objConn)
objConn.close()

#Se consulta el reporte de las Tarjetas del Cliente desde DDBB
cliente.reporteDB()