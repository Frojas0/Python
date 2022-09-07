# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuacion cree las siguientes listas
# (en las que no deben haber repeticiones)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 Lista de palabras que aparecen en ambas listas

listaA = ['Juancarlo', 'Juancarlo', 'Carla', 'Rubio', 'Traika', 'Chancha', 'Motomoto',  'Perro']
listaB = ['Coca', 'Perro', 'oso', 'helicoptero', 'Traika', 'Jazmin', 'Rubio', 'doce', 'uno']

lista1 = set(listaA) | set(listaB) # Imprime elementos de ambas listas sin repeticiones
print(f'Lista1: {lista1}')

lista2 = set(listaA) - set(listaB) # Imprime elementos de la primer lista
print(f'Lista2: {list(lista2)}')

lista3 = set(listaB) - set(listaA) # Imprime elementos de la segunda lista
print(f'Lista3: {list(lista3)}')

lista4 = set(listaA) & set(listaB) # Imprime elementos en comun de ambas listas
print(f'Lista4: {list(lista4)}')

