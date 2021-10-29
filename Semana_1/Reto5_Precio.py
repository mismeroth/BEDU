def reto_5():
    print("-" * 50)
    print("1. Helado + Oreo")
    print("2. Helado + M&M")
    print("3. Helado + Fresas")
    print("4. Helado + Brownie")
    opcion = int(input("Seleccione una opcion: "))
    print("-" * 50)

    salida = "El precio del producto es $"

    if opcion == 1:
        print(salida, 19)
    elif opcion == 2:
        print(salida, 25)
    elif opcion == 3:
        print(salida, 22)
    elif opcion == 4:
        print(salida, 28)
    else:
        print("Producto Invalido")
