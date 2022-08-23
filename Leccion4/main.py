
# Listas
"""
listNombres = ['Juan', 'Carlos', 'Martin', 'German']
print(listNombres)
print(listNombres[2]) # Le digo que indice imprimir
print(listNombres[-1]) # Imprime el ultimo elemento
print(listNombres[0:2]) # Recorre un intervalo dado, del indice 0 al 1 sin tomar el 2
print(listNombres[ :3]) # Recorre hasta el indice indicado
print(listNombres[1: ]) # Recorre desde el indice indicado

# Modificamos un valor
listNombres[1] = "Carlas" #Modifico un elemento en el indice indicado
print(listNombres)

# Iterar una lista
for i in listNombres :
    print(i)
else:
    print("Se acabaron los elementos")

# Consultamos elementos de la lista
print(len(listNombres)) # Nos devuelve la cantidad de elementos de la lista

# Agregamos elementos a la lista
listNombres.append('Jorgito') # Agrega el elemento al final de la lista
                              # Efecto Cola

listNombres.insert(2, "Alberso") # Agrego un elemento en el indice indicado, y desplaza el resto a la derecha
print(listNombres)

# Eliminamos un elemento de la lista
listNombres.remove("Jorgito")
print(listNombres)

# Elimitar el ultimo elemento en la lista
listNombres.pop()
print(listNombres)

# Eliminar un indice especifico
del listNombres[2]
print(listNombres)

# Eliminar todos los elementos de la lista
listNombres.clear()
print(listNombres)
"""

# Tuplas
tupCocina = ('cuchara', 'cucharita', 'cucharon')
print(tupCocina)
print(len(tupCocina)) # Imprime la longitud

# Acceder a un elemento
print(tupCocina[1])
print(tupCocina[-1]) # Imprime el ultimo elemento

# Acceder a un rango
print(tupCocina[0:1]) # Imprime un rango

# Recorremos los elementos de la tupla
for i in tupCocina:
    print(i, end=' ') # Utilizamos end para eliminar los saltos de linea

