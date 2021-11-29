import Reto_1_Argumentos as r1
import Reto_2_Import as r2
import Reto_4_Archivos as r4
import RetoFinal.Reto_Final as rf

print("1. Reto Argumentos")
print("2. Reto Import")
print("3. Reto Modulos")
print("4. Reto Archivos")
print("5. Reto Final")
print("-" * 50)

seleccion = int(input("Digite el reto: "))

#Limpiar Consola
print("\033[H\033[J", end="")

if seleccion == 1:
    r1.reto_1()
    r1.reto_1_2()
    input()

if seleccion == 2:
    r2.reto_2()
    input()

if seleccion == 4:
    r4.reto_4()
    input()

if seleccion == 5:
    rf.Reto_Final()
    input()

