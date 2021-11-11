def reto_4():
  directorio = {
      "Juan": "666-1234",
      "Pedro": "555-1112",
      "Carlos": "565-4455",
      "Luis": "767-5566",
      "Andrea": "989-0099"
  }

  #Imprime directorio
  print(directorio.keys())

  #Imprime Menu
  print("1. Buscar Numero")
  print("2. Ingresar Numero")
  seleccion = int(input("Opcion: "))

  if seleccion == 1:
      buscar = str(input("Ingrese un nombre: "))
      if directorio.get(buscar) is None:
          print("Nombre no encontrado")
      else:
          print("El Telefono de {} es {}".format(buscar, directorio.get(buscar)))

  if seleccion == 2:
      llave = input("Ingrese Nombre: ")
      valor = input("Ingrese Numero: ")
      directorio[llave] = valor
      print(directorio.keys())
