"""Contiene todos las clases para el acceso a la BBDD"""
import sqlite3 as sql

class DBUtils(object):
    """Clase que maneja la BBDD para Tarjetas"""
    def abrirConexion(self):
        #Retorna el Objecto de Conexion
        try:
            conn = sql.connect('Entrega_Final/DB/BankData.db')
            return conn
        except sql.Error:
            print(sql.Error)

    def cerrarConexion(self, pConn):
        #Cierra Conexion
        try:
            pConn.close()
        except:
            pass

    def crearTablaCliente(self, pConn):
        #Crea la tabla de Tarjetas
        try:
            cursorObj = pConn.cursor()
            cursorObj.execute(
                "CREATE TABLE Cliente (IDCliente INT PRIMARY KEY,Nombres VARCHAR,Correo VARCHAR)"
            )
            pConn.commit()
        except sql.Error:
            print(sql.Error)

    def insertarCliente(self, pConn, pParams):
        mensaje=None
        try:
          cursorObj = pConn.cursor()
          cursorObj.execute(
              'INSERT INTO Cliente(IDCliente,Nombres,Correo) VALUES(?, ?, ?)',
              pParams)
          pConn.commit()
          mensaje="Se inserto [CLIENTE] con exito"
        except Exception as e:
          mensaje="Ocurrio un error insertando [CLIENTE] -> {}".format(e)
        
        return mensaje

    def consultarClientes(self, pConn):
        cursorObj = pConn.cursor()
        cursorObj.execute('SELECT IDCliente,Nombres,Correo FROM Cliente')
        rows = cursorObj.fetchall()
        return rows

    def EliminarCliente(self, pConn):
        cursorObj = pConn.cursor()
        cursorObj.execute('DELETE FROM Tarjeta')
        pConn.commit()

    def consultarTarjetas(self, pConn):
        cursorObj = pConn.cursor()
        cursorObj.execute('SELECT * FROM Tarjeta')
        rows = cursorObj.fetchall()
        return rows
