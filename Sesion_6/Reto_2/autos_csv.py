import os
import csv

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
    archivo_cvs=None
    if os.path.isfile("Sesion_6/Reto_2/autos.csv"):
      archivo = open("Sesion_6/Reto_2/autos.csv", "a")
    else: 
      archivo = open("Sesion_6/Reto_2/autos.csv", "w")
      archivo_cvs=csv.writer(archivo)
      archivo_cvs.writerow( ["Nombre", "Color", "Nivel","precio"] )
    
    archivo_cvs=csv.writer(archivo)
    lineas=[]
    lineas.append([nombre,color,nivel,precio])
    archivo_cvs.writerows( lineas )

##Inicia el llamado
solicitar()
