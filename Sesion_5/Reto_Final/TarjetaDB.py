import sqlite3 as sql


class TarjetaDB(object):
    """Clase que maneja la BBDD para Tarjetas"""
    def abrirConexion(self):
        #Retorna el Objecto de Conexion
        try:
            conn = sql.connect('mydatabase.db')
            return conn
        except sql.Error:
            print(sql.Error)

    def cerrarConexion(self, pConn):
        #Cierra Conexion
        try:
            pConn.close()
        except:
            pass

    def crearTablaTarjeta(self, pConn):
        #Crea la tabla de Tarjetas
        try:
            cursorObj = pConn.cursor()
            cursorObj.execute(
                "CREATE TABLE Tarjeta (Nombre VARCHAR,Tasa FLOAT,Deuda FLOAT,Pago FLOAT,Cargos FLOAT)"
            )
            pConn.commit()
        except sql.Error:
            print(sql.Error)

    def insertarTarjeta(self, pConn, pParams):
        cursorObj = pConn.cursor()
        cursorObj.execute(
            'INSERT INTO Tarjeta(Nombre,Tasa,Deuda,Pago,Cargos) VALUES(?, ?, ?, ?, ?)',
            pParams)
        pConn.commit()

    def consultarTarjetas(self, pConn):
        cursorObj = pConn.cursor()
        cursorObj.execute('SELECT * FROM Tarjeta')
        rows = cursorObj.fetchall()
        return rows

    def inicializarTabla(self, pConn):
        cursorObj = pConn.cursor()
        cursorObj.execute('DELETE FROM Tarjeta')
        pConn.commit()
