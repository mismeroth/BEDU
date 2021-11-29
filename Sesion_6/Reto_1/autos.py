import os
def solicitar():
    NOMBRE = "Nombre del Auto : "
    COLOR = "Color : "
    NIVEL = "Nivel de equipamiento [bajo, medio,alto] : "
    PRECIO = "Precio : "

    nombre = input(NOMBRE)
    color = input(COLOR)
    nivel = input(NIVEL)
    precio = input(PRECIO)

    #guarda el achivo
    archivo=None
    if os.path.isfile("Sesion_6/Reto_1/autos.txt"):
      archivo = open("Sesion_6/Reto_1/autos.txt", "a")
    else: archivo = open("Sesion_6/Reto_1/autos.txt", "w")

    archivo.write("{}{}\n".format(NOMBRE,nombre))
    archivo.write("{}{}\n".format(COLOR,color))
    archivo.write("{}{}\n".format(NIVEL,nivel))
    archivo.write("{}{}\n\n".format(PRECIO,precio))
    archivo.close()

##Inicia el llamado
solicitar()
