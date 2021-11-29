import TarjetaDB as tdb

class Usuario(object):
    """Define la clase con los datos y tarjetas para un usuario"""
    def __init__(self, pNombres):
        self.nombres = pNombres
        self._tarjetas = []

    def __str__(self):
        cadena = "%" * 60
        cadena += "\nInforme de Tarjetas de {}\n".format(self.nombres)
        cadena += "%" * 60
        return cadena

    @property
    def tarjetas(self):
        return self._tarjetas

    def Adicionar(self, tarjeta):
        self._tarjetas.append(tarjeta)

    def Eliminar(self, pNombreTarjeta):
        for tarjeta in self.tarjetas:
            if tarjeta.nombre == pNombreTarjeta:
                self.tarjetas.remove(tarjeta)
                print("\n")
                print("?" * 50)
                print("Tarjeta [{}] removida".format(pNombreTarjeta))
                print("?" * 50)
                print("\n")

    def reporteDB(self):
        objTarjeta = tdb.TarjetaDB()
        objConn = objTarjeta.abrirConexion()
        res = objTarjeta.consultarTarjetas(objConn)
        objConn.close()

        print("-"*50)
        print("{:<10}{:<10}{:<10}{:<10}{:<10}".format("Nombre","Tasa (%)","Deduda","Pago","Cargos"))
        print("-"*50)
        for col in res:
            print("{:<10}{:<10}{:<10}{:<10}{:<10}".format(col[0],col[1],col[2],col[3],col[4]))
