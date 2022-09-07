# Ejercicio 3: Insertar elementos y ordenarlos
# pedir numeros y meterlos en una lista, cuando el usuario introduzca un numero 0, nuestro programa dejaria de insertar.
# por ultimo, mostrar los numeros ordenados de menor a mayor

lista = []
salir = False
while not salir:
    n = int(input('Digite un numero: '))

    if n == 0:# condicion para finalizar while
        salir = True
    else:
        lista.append(n)
print(sorted(lista)) # imprimimos la lista ordenada