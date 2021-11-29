import math as libreriaMate
from math import gcd as maximo


def f_factorial(numero):
    #uso de funcion factorial
    print("El factorial para {} es --> {}  ".format(
        numero, libreriaMate.factorial(numero)))


def f_raiz(numero):
    #uso de funcion raiz
    print("La raiz para {} es --> {}  ".format(numero,
                                               libreriaMate.sqrt(numero)))


def mcd(numero_1, numero_2):
    m = maximo(numero_1, numero_2)
    print("\nEl MCD entre {} y {} es {}".format(numero_1, numero_2, m))

def reto_2():
    parametro = int(input("Digite un numero: "))
    f_factorial(parametro)
    f_raiz(parametro)

    parametro_2 = int(input("\nDigite otro numero: "))
    mcd(parametro, parametro_2)
