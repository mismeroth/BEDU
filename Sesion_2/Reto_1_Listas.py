import bisect as b

def reto_1():
  lista_alumnos = ['Juan', 'Maria', 'Carlos', 'Luis', 'Pedro']
  print("-" * 50)
  print("Lista de Alumnos --> ", lista_alumnos)
  print("-" * 50)

  lista_alumnos.sort()
  print("Lista Ordenada --> ", lista_alumnos)
  print("Primer Alumno: ", lista_alumnos[0])
  print("-" * 50)
  
  b.insort(lista_alumnos,input("Ingrese nuevo Alumno: "))
  print("Nueva Lista --> ", lista_alumnos)
