import Reto2_Variables as r2
import Reto3_Operadores as r3
import Reto4_TablaMultiplicar as r4
import Reto5_Precio as r5
import RetoFinal as rf

print("2. Reto Variables")
print("3. Reto Operadores")
print("4. Reto Tabla de Multiplicar")
print("5. Reto Precio")
print("6. Reto Final")
print("-" * 50)

seleccion = int(input("Digite el reto: "))

#Limpiar Consola
print("\033[H\033[J", end="")

if seleccion == 2:
    r2.reto_2()
    input()

if seleccion == 3:
    r3.reto_3()
    input()

if seleccion == 4:
    r4.reto_4()
    input()

if seleccion == 5:
    r5.reto_5()
    input()

if seleccion == 6:
    rf.reto_final()
    input()
    

#Limpiar Consola
print("\033[H\033[J", end="")
