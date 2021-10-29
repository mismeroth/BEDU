def reto_3():
    #Calcular el volumen de una esfera
    radio = float(input("Ingrese el radio del objeto: "))

    #define la constate PI
    pi = 3.1416
    volumen = (4 * pi * (radio**3)) / 3

    print("El volumen del Objeto es {}".format(round(volumen, 2)))
