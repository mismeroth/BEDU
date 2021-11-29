import sys

archivo=None
if len(sys.argv) == 3:
    archivo = sys.argv[1]
    lineaBuscar = int(sys.argv[2])
else:
    print("Error - Introduce los argumentos correctamente")
print(archivo)
archivo = open(archivo, "r")
lineas = archivo.readlines()
i = 0
for linea in lineas:
    i += 1
    if lineaBuscar == i:
        print(linea)

##"python Sesion_6/Reto_4/Reto_4_Arguments.py 'Sesion_6/Reto_4/salida.json' 2"