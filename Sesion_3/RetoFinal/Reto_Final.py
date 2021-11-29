import RetoFinal.Tarjeta.Tarjeta as t
import RetoFinal.Tarjeta.Usuario as rr

##Business Objects
class CargosTarjeta():
  interes_mensual = 0.0
  deuda_calculada_anual = 0.0
  deuda_calculada_mes = 0.0
  nueva_deuda = 0.0
  proximo_pago = 0.0

class Tarjeta():
  """Define la clase Tarjeta"""
  nombre=''
  tasa=0.0
  deuda=0.0
  pago=.0
  cargos=0.0
  cargos_tarjeta=CargosTarjeta()


def Reto_Final():
    """Inicializa el programa para el reto final"""
    print("-" * 50)
    print("Calculadora de Interes")
    print("-" * 50)
    
    #Instancia de la clase tarjeta para pasarla por parametro
    tarjeta  = Tarjeta()

    tarjeta.nombre = input("Nombre de la Franquicia: ") or "test"
    tarjeta.tasa = float(input("Ingrese la tasa de Interes Anual (%): ") or 2.0)
    tarjeta.deuda = float(input("Ingrese el total de la deuda: ") or 1000.0)
    tarjeta.pago = float(input("Ingrese el pago a realizar: ") or 5.0)
    tarjeta.cargos = float(input("Ingrese los cargos adicionales: ") or 50.0)

    ##paso de la clase BO a la funcion tarjeta
    rr.reportes(t.calcular(tarjeta))
    


