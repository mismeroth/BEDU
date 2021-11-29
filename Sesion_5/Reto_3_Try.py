import random

def promedio(pLista):
  ##Uso de Try Except
  ##calcula el promedio de n numeros
  try:
    prom = pLista[0]/pLista[1]
    print("La division de {} y {} es -->{}".format(pLista[0],pLista[1],prom))
  except ZeroDivisionError:
    print("Denominador Invalido [0]")
  except:
    print("Excepcion no Controlada")

#crea una lista aletaria
lista = [random.randint(0,9) for i in range(0,2)]

#Excepcion no controlada
#lista = ["a","b"]
promedio(lista)