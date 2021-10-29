def reto_4():
  print("Genera tabla de multiplicar")
  print("_" * 50)

  numero = int(input("Ingrese un número: "))

  i = 0
  while i <= 10:
      print("{} * {} = {}".format(numero, i, numero * i))
      i += 1
