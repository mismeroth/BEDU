def reto_5():
  x = 1
  y = 0
  z = 0

  print("Serie Fibbo hasta 1000")
  while x < 1000:
    if x == 1:
        #inicializa variables
        x = 1
        y = 1
        print(x)
        print(y)
        x = x + y
    else:
        #Calcula serie
        z = x
        x = x + y
        y = z
    if x < 1000:
      print(x)

