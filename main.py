


def imprimir_Arreglo(arreglo):
  tamanio = len(arreglo)
  for i in range(tamanio):
    print(f' [ {arreglo[i]} ] ',end="")


def algoritmo_Busqueda_Lineal(arreglo,sueldo):
  resultado = False
  tamanio = len(arreglo)-1
  for i in range(tamanio):
    if (arreglo[i] == sueldo):
      resultado = True
      return resultado
  return resultado






listaSueldos = [20.8,150.5,170.5,180.8,190,30,75.6,200]
print("\n Suelo de empleados \n")

imprimir_Arreglo(listaSueldos)

sueldo = float(input("\n\n Ingrese el sueldo a encontrar: "))

respuesta = algoritmo_Busqueda_Lineal(listaSueldos,sueldo)


if respuesta:
  print("\n El sueldo fue encontrado en nuestro sistema")
else:
  print("\n El sueldo no fue encontrado en nuestro sistema")
  