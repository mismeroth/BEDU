import click,time
from os import path, stat, listdir


#########################################################
class Archivo(object):
    """Clase que obtiene la metadata de un archivo"""
    def __init__(self, pRuta):
        #Constructor de la Clase
        self.ruta = pRuta
        self.type = None
        self.size = None
        self.date = None

    def metadata(self):
        #Obtiene los metadados de un Archivo
        if path.isdir(self.ruta) is True:
            self.type = "Carpeta"
        else:
            self.type = "Archivo"
        self.size = path.getsize(self.ruta)
        self.date = time.ctime(path.getctime(self.ruta))
        return self


#########################################################
class Carpeta(object):
    """Clase que contiene las funcionalidades de lectura de una carpeta"""
    def __init__(self, pCarpeta):
        #Constructor de la Clase
        self.carpeta = pCarpeta

    def LeerCarpeta(self):
        #Obtiene los objetos del Directorio
        files = listdir(self.carpeta)
        filesMetaData = []

        ##Lee cada archivo y lo transforma en un Business Object
        for file in files:
            objArchivo = Archivo("{}{}".format(self.carpeta, file)).metadata()
            filesMetaData.append(objArchivo)

        return filesMetaData


def imprime_en_texto(pArchivos):
    #formatea la salida
    cadena = "{:<15}{:<15}{:<15}{:<15}\n".format("Nombre", "Tipo", "Tamaño","Fecha")
    for archivo in pArchivos:
      cadena += "{:<30}{:<15}{:<15}{:<15}\n".format(archivo.ruta,archivo.type,archivo.size,archivo.date)

    print(cadena)


#######################################################
@click.command()
@click.argument("carpeta", default=".", type=click.Path(exists=True))
def main(carpeta):
    """Rutina que lee un path y obtiene la metadata de sus objetos
    """
    print("Objetos en la ruta -->", carpeta)
    objArchivos = Carpeta(carpeta).LeerCarpeta()
    imprime_en_texto(objArchivos)


if __name__ == '__main__':
    main()
