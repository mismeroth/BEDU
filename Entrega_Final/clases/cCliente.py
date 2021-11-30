import clases.cDataBase as db

class Cliente(object):
    """Define la clase con los datos y tarjetas para un usuario"""
    def __init__(self, pNombres,pCorreo,pDocumento):
        self.nombres = pNombres
        self.correo = pCorreo
        self.documento = pDocumento
        self._tarjetas = []

    @property
    def tarjetas(self):
        return self._tarjetas

    def CrearCliente(self):
      pParams = (self.nombres,self.correo,self.documento)
      objDB = db.DBUtils()
      objConn = objDB.abrirConexion()
      mensaje=objDB.insertarCliente(objConn,pParams)
      objConn.close()
      return mensaje

    def AdicionarTarjeta(self, tarjeta):
        self._tarjetas.append(tarjeta)

    def EliminarTarjeta(self, pNombreTarjeta):
        pass

    def reporteClientes(self):
      objDB = db.DBUtils()
      objConn = objDB.abrirConexion()
      listaClientes=objDB.consultarClientes(objConn)
      objConn.close()
      return listaClientes

