def calcular(p_tarjeta):
  tar = p_tarjeta
  
  ##calculos internos 
  tar.cargos_tarjeta.interes_mensual = tar.tasa / 12

  tar.cargos_tarjeta.deuda_calculada_anual = (tar.deuda - tar.pago) * (1 + tar.cargos_tarjeta.interes_mensual)
  tar.cargos_tarjeta.deuda_calculada_mes = (tar.deuda - tar.pago) + tar.cargos_tarjeta.interes_mensual  
  tar.cargos_tarjeta.nueva_deuda = tar.cargos_tarjeta.deuda_calculada_mes + tar.cargos
  tar.cargos_tarjeta.proximo_pago = (tar.cargos_tarjeta.nueva_deuda/12) * (1 + tar.cargos_tarjeta.interes_mensual)
  
  return tar
