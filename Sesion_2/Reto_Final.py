import random as r

##########################
#Funciones del Script
##########################
def f_orden_lista(pLista):
    """"Ordenamiento de una Lista """
    tmpLista = list(pLista)
    tmpLista.sort()
    return tmpLista


def f_genera_lista():
    """Genera una lista con numeros aleatorios"""
    lista = []
    #genera 20 numeros aleatorios
    lista = [r.randint(0, 1000) for i in range(20)]

    #ingresa valor repetido forzado
    lista.append(33)
    lista.append(33)
    return lista

def f_quita_duplicados(pLista):
    lista_sin_dup = f_orden_lista(list(set(pLista)))
    return lista_sin_dup
###########################

#Ejecucion  del ejercicio
def reto_final(lista):
  print("Lista \n{}".format("*"*50))
  print(lista)

  #eliminacion de duplicados
  print("\nLista Ordenada \n{}".format("*"*50))
  lista_ord = f_orden_lista(lista)
  print(lista_ord)

  print("\nLista Sin Duplicados\n{}".format("*"*50))
  lista_dup = f_quita_duplicados(lista_ord)
  print(lista_dup)