def reto_final():
  print("-" * 50)
  print("Calculadora de Interes")
  print("-" * 50)

  nombre = input("Nombre de la Franquicia: ") or "test"
  tasa = float(input("Ingrese la tasa de Interes (%): ")) or 12.0
  deuda = float(input("Ingrese el total de la deuda: ")) or 1000.0
  pago = float(input("Ingrese el pago a realizar: ")) or 5.0
  cargos = float(input("Ingrese los cargos adicionales: ")) or 50.0

  ##calculos internos
  interes_mensual = tasa / 12
  deuda_calculada = (deuda - pago) * (1 + interes_mensual)
  nueva_deuda = deuda_calculada + cargos
  proximo_pago = (nueva_deuda/12) * (1 + interes_mensual)

  print("-" * 50)
  print(f"Resumen de la tarjeta '{nombre}'")
  print("-" * 50)
  print("Tasa Ingresada: % {:0,.2f}".format(tasa))
  print("Deuda Total: $ {:0,.2f}".format(deuda_calculada))
  print("Nueva Deuda: $ {:0,.2f}".format(nueva_deuda))
  print("Proximo Pago: $ {:0,.2f}".format(proximo_pago))