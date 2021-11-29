class vehiculo():
  """Clase que define las propiedades de un vehiculo"""
  def __init__(self, color, ruedas, tipo, marca):
    #Constructor de la clase con atributos privados
      self._color = color
      self._ruedas = ruedas
      self._tipo = tipo
      self._marca = marca
  
  ##para acceder a los atributos privados
  def marca(self):
    return self._marca

  def color(self):
    return self._color
  
  def ruedas(self):
    return self._ruedas

  def tipo(self):
    return self._tipo

  def construir_vehiculo(self):
    #Metodo que imprime el vehiculo solicitado
    print("Caracteristicas del Vehiculo solicitado: \n")
    print("{:<10}: {}".format("Marca",self.marca()))
    print("{:<10}: {}".format("Color",self.color()))
    print("{:<10}: {}".format("Ruedas",self.ruedas()))
    print("{:<10}: {}".format("Tipo",self.tipo()))

##Ejemplo de instanciacion de la clase
vehiculo("Rojo","4","Sedan","BM").construir_vehiculo()
