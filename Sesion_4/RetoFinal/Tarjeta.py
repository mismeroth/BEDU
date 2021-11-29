class CargosTarjeta(object):
    """Clase que define los cargos de la tarjeta"""
    interes_mensual = 0.0
    deuda_calculada_anual = 0.0
    deuda_calculada_mes = 0.0
    nueva_deuda = 0.0
    proximo_pago = 0.0

class Tarjeta(object):
    """Define la clase Tarjeta"""
    def __init__(self, pFranquicia, pTasaAnual, pDeuda, pPago):
      #Constructor de la clase
        self.nombre = ''
        self.tasa = 0.0
        self.deuda = 0.0
        self.pago = .0
        self.cargos = 0.0
        self.cargos_tarjeta = CargosTarjeta()

    def calcular(self):
        ##calculos internos
        print("Calculando datos...")
        self.cargos_tarjeta.interes_mensual = self.tasa / 12

        self.cargos_tarjeta.deuda_calculada_anual = (
            self.deuda - self.pago) * (1 + self.cargos_tarjeta.interes_mensual)

        self.cargos_tarjeta.deuda_calculada_mes = (
            self.deuda - self.pago) + self.cargos_tarjeta.interes_mensual

        self.cargos_tarjeta.nueva_deuda = self.cargos_tarjeta.deuda_calculada_mes + self.cargos

        self.cargos_tarjeta.proximo_pago = (
            self.cargos_tarjeta.nueva_deuda /
            12) * (1 + self.cargos_tarjeta.interes_mensual)

    def reporte(self):
        print("\n" * 2)
        print("-" * 50)
        print("Resumen de la tarjeta")
        print("-" * 50)
        print("Nombre de la Franquicia: {}".format(self.nombre))
        print("Tasa Interes Anual: % {:0,.2f}".format(self.tasa))
        print("-" * 50)
        print("Deuda Actual: $ {:0,.2f}".format(self.deuda))
        print("Pago: $ {:0,.2f}".format(self.pago))
        print("-" * 50)
        print("Nueva Deuda: $ {:0,.2f}".format(self.deuda - self.pago))
        print("Interes Mensual: $ {:0,.2f}".format(
            self.cargos_tarjeta.interes_mensual))
        print("-" * 50)
        print("Deuda Recalculada: $ {:0,.2f}".format(
            self.cargos_tarjeta.deuda_calculada_mes))
        print("Nuevos Cargos: $ {:0,.2f}".format(self.cargos))
        print("-" * 50)
        print("Nueva Deuda: $ {:0,.2f}".format(
            self.cargos_tarjeta.nueva_deuda))
