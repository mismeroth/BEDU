def f_operacion(tipoOperacion, *args):
    """Funcion que permite realizar operacion + o * sobre un numero n de argumentos numericos"""
    resOper = None  # Inicializacion de Variable
    #Evalua el tipo de operador
    if (tipoOperacion == "+"):
        resOper = 0  #Se asigna 0 para iniciar la Suma
        for valor in args:
            resOper += valor
    elif (tipoOperacion == "*"):
        resOper = 1  #Se asigna 1 para evitar la multiplicacion por cero al inicio
        for valor in args:
            resOper *= valor
    else:
        print("operador invalido")

    return resOper


def directorioTel(**kargs):
    """Funcion que ordena una lista de argumentos de entrada"""
    print("\n Directorio telefonico")
    print("-" * 50)
    listaOrd = sorted(kargs)
    for entrada in listaOrd:
        print("{0:10} Phone: {1}".format(entrada, str(kargs[entrada])))


def reto_1():
    resultado = f_operacion(input("Operacion a realizar [+/*] : "), 1, 2, 3, 5)

    print("Resultado de la Operacion :", resultado)


def reto_1_2():
    directorioTel(Carlos="555-2233", Juan="555-1234", Ana="555-4567")
