import os as util
from datetime import datetime

def reto_4():
  ruta = "/home/runner/BEDU/Sesion_3/README.md"
  s = util.path.getsize(ruta)
  f = util.path.getmtime(ruta)

  print("Detalles del Archivo {}".format(ruta))
  print("{0:>20}{1:>20}".format("Tamaño","Fecha Mod."))
  print("{0:>20}{1:>20}".format(s,datetime.fromtimestamp(f).strftime("%Y-%m-%d %H:%M:%S")))