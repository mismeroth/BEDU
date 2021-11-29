class vehiculo():
  """Clase que define las propiedades de un vehiculo"""
  def __init__(self, color, ruedas, tipo, marca):
    #Constructor de la clase
      self.color = color
      self.ruedas = ruedas
      self.tipo = tipo
      self.marca = marca

  def construir_vehiculo(self):
    #Metodo que imprime el vehiculo solicitado
    print("Caracteristicas del Vehiculo solicitado: \n")
    print("{:<10}: {}".format("Marca",self.marca))
    print("{:<10}: {}".format("Color",self.color))
    print("{:<10}: {}".format("Ruedas",self.ruedas))
    print("{:<10}: {}".format("Tipo",self.tipo))

##Ejemplo de instanciacion de la clase
vehiculo("Rojo","4","Sedan","BM").construir_vehiculo()

