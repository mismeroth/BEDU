import TarjetaDB as tdb
import Tarjeta as t

import json

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
        print("{:<10}{:<10}{:<10}{:<10}{:<10}".format("Nombre","Tasa (%)","Deuda","Pago","Cargos"))
        print("-"*50)
        for col in res:
            print("{:<10}{:<10}{:<10}{:<10}{:<10}".format(col[0],col[1],col[2],col[3],col[4]))

    def crearJSONTarjetas(self,pTarjetas):
      for tarjeta in pTarjetas:
          data = []
          for tarjeta in pTarjetas:
            item = {"userID": self.nombres}
            item["franquicia"] = tarjeta.nombre
            item["tasa"] = tarjeta.tasa
            item["deuda"] = tarjeta.deuda
            item["pago"] = tarjeta.pago
            item["cargos"] = tarjeta.cargos
            data.append(item)
            
          with open('Sesion_6/Reto_Final/tarjetas.json', 'w') as archivoJSON:
              json.dump(data, archivoJSON,indent=4)

    def leerJSON(self):
      listatarjetas = []
      with open('Sesion_6/Reto_Final/tarjetas.json') as file:
        objTarjeta = t.Tarjeta
        data = json.load(file)
        for client in data:
          objTarjeta.nombre=client["franquicia"]
          objTarjeta.tasa=client["tasa"]
          objTarjeta.deuda=client["deuda"]
          objTarjeta.pago=client["pago"]
          objTarjeta.cargos=client["cargos"]
          listatarjetas.append(objTarjeta)
        
        print("\nJSON leido y adicionado a un Objeto")
        print(listatarjetas)

        

        
