class Vehiculo(object):
    """Clase que define las propiedades de un vehiculo"""
    def __init__(self, pColor, pRuedas, pTipo, pMarca):
        #Constructor de la clase con atributos privados
        self._color = pColor
        self._ruedas = pRuedas
        self._tipo = pTipo
        self._marca = pMarca

    def __str__(self):
        cadena = "Caracteristicas del Vehiculo solicitado: \n"
        cadena += "{:<10}: {}\n".format("Marca", self.marca)
        cadena += "{:<10}: {}\n".format("Color", self.color)
        cadena += "{:<10}: {}\n".format("Ruedas", self.ruedas)
        cadena += "{:<10}: {}\n".format("Tipo", self.tipo)
        return cadena

    ##para acceder a los atributos privados
    @property
    def marca(self):
        return self._marca

    @property
    def color(self):
        return self._color

    @property
    def ruedas(self):
        return self._ruedas

    @property
    def tipo(self):
        return self._tipo


class VehiculoAereo(Vehiculo):
    """Clase que define las propiedades de un vehiculo"""
    def __init__(self, pColor, pRuedas, pTipo, pMarca, pCapacidadCarga,
                 pPasajeros, pMotores):
        #Constructor clase padre
        Vehiculo.__init__(self, pColor, pRuedas, pTipo, pMarca)

        #Constructor de la clase con atributos privados
        self._capacidadCarga = pCapacidadCarga
        self._pasajeros = pPasajeros
        self._motores = pMotores

    def __str__(self):
        cadena = "Caracteristicas de la Aeronave: \n"
        cadena += "{:<15}: {}\n".format("Marca", self.marca)
        cadena += "{:<15}: {}\n".format("Color", self.color)
        cadena += "{:<15}: {}\n".format("Ruedas", self.ruedas)
        cadena += "{:<15}: {}\n".format("Tipo", self.tipo)
        cadena += "{:<15}: {}\n".format("Capacidad", self.capacidadCarga)
        cadena += "{:<15}: {}\n".format("Pasajeros", self.pasajeros)
        cadena += "{:<15}: {}\n".format("No. Motores", self.motores)
        return cadena

    ##para acceder a los atributos privados
    @property
    def capacidadCarga(self):
        return self._capacidadCarga

    @property
    def pasajeros(self):
        return self._pasajeros

    @property
    def motores(self):
        return self._motores


class VehiculoTerrestre(Vehiculo):
    """Clase que define las propiedades de un vehiculo"""
    def __init__(self, pColor, pRuedas, pTipo, pMarca, pCapacidadCarga,
                 pPasajeros, pCilindrada):
        #Constructor clase padre
        Vehiculo.__init__(self, pColor, pRuedas, pTipo, pMarca)

        #Constructor de la clase con atributos privados
        self._capacidadCarga = pCapacidadCarga
        self._pasajeros = pPasajeros
        self._cilindrada = pCilindrada

    def __str__(self):
        cadena = "Caracteristicas del Automotor: \n"
        cadena += "{:<15}: {}\n".format("Marca", self.marca)
        cadena += "{:<15}: {}\n".format("Color", self.color)
        cadena += "{:<15}: {}\n".format("Ruedas", self.ruedas)
        cadena += "{:<15}: {}\n".format("Tipo", self.tipo)
        cadena += "{:<15}: {}\n".format("Capacidad", self.capacidadCarga)
        cadena += "{:<15}: {}\n".format("Pasajeros", self.pasajeros)
        cadena += "{:<15}: {}\n".format("Cilindrada", self.cilindrada)
        return cadena

    ##para acceder a los atributos privados
    @property
    def capacidadCarga(self):
        return self._capacidadCarga

    @property
    def pasajeros(self):
        return self._pasajeros

    @property
    def cilindrada(self):
        return self._cilindrada
