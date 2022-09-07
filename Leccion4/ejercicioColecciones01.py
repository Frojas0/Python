# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que acontinuacion elimine los elementos repetidos
# por ultimo mostrar la lista

lista = [6, 7, 4, 23, 1, 2, 3, 45, 2, 34, 1, 123, 3, 4, 1, 2, 2, 3, 3, 4, 5]
'''
cleanList = []
for i in lista:
    if i not in cleanList:
        cleanList.append(i)

print(f"Lista original: {lista}\n"
      f"Lista sin elementos repetidos: {cleanList}")
'''
# Resolucion en la clase

lista = list(set(lista))  # Convertimos la lista en conjunto y sobre la misma la volvemos a convertir en conjunto
print(lista)