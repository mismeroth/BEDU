class Usuario(object):
  """Define la clase con los datos y tarjetas para un usuario"""
  def __init__(self,pNombres):
    self.nombres=pNombres
    self._tarjetas=[]
  
  def __str__(self):
    cadena ="*"*50
    cadena += "\nInforme de Tarjetas de {}\n".format(self.nombres)
    cadena +="*"*50
    return cadena
  
  @property
  def tarjetas(self):
    return self._tarjetas
  
  def Adicionar(self,tarjeta):
    self._tarjetas.append(tarjeta)
  
  def Eliminar(self,pNombreTarjeta):
    for tarjeta in self.tarjetas:
      if tarjeta.nombre==pNombreTarjeta:
        self.tarjetas.remove(tarjeta)
        print("\n")
        print("?"*50)
        print("Tarjeta [{}] removida".format(pNombreTarjeta))
        print("?"*50)
        print("\n")