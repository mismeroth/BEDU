import Reto_1_Listas as r1
import Reto_4_Diccionario as r4
import Reto_5_Fibbo as r5
import Reto_6_MCM as r6
import Reto_Final as rf

print("1. Reto Listas")
print("4. Reto Diccionario")
print("5. Serie Fibbo")
print("6. Minimo Comun Multiplo")
print("7. Reto Final")
print("-" * 50)

seleccion = int(input("Digite el reto: "))

#Limpiar Consola
print("\033[H\033[J", end="")

if seleccion == 1:
    r1.reto_1()
    input()

if seleccion == 4:
    r4.reto_4()
    input()

if seleccion == 5:
    r5.reto_5()
    input()

if seleccion == 6:
    r6.reto_6()
    input()

if seleccion == 7:
    rf.reto_final(rf.f_genera_lista())
    input()
