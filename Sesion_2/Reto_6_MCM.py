def reto_6():
    print("-" * 50)
    print("Calcular Minimo Común Multiplo")
    num_a = int(input("Ingrese el numero A: "))
    num_b = int(input("Ingrese el numero B: "))

    #Evaluar cual es el minimo y max de los numeros
    a = max(num_a, num_b)
    b = min(num_a, num_b)

    while b:
        #Maximo comun divisor
        mcd = b
        b = a % b
        a = mcd
        #Minimo comun multiplo
        mcm = (num_a * num_b) // mcd

    print("El minimo comun multiplo de {} y {} es {}".format(
        num_a, num_b, mcm))
