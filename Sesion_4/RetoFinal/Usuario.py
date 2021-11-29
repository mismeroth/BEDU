class Usuario(object):
  """Define la clase con los datos y tarjetas para un usuario"""
  def __init__(self,pNombres):
    self.nombres=pNombres
    self._tarjetas=[]
  
  def __str__(self):
    cadena = "Informe de Tarjetas de {}".format(self.nombres)
    return cadena
  
  @property
  def tarjetas(self):
    return self._tarjetas
  
  def Adicionar(self,tarjeta):
    self._tarjetas.append(tarjeta)
  
  def Eliminar(self):
    pass