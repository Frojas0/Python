
# >>>Colecciones en Python <<<

# Listas, tambien llamadas arreglos o vectores
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
listNombres.append([1,2,3])   # Podemos agregar otra lista
listNombres.append(True)      # Booleanos
listNombres.append(10.45)     # Decimales
print(listNombres)

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
"""
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
"""

# Tipo set o conjunto
"""
# Set al no tener indice, devuelve elementos de forma totalmente aleatoreas
setPlanetas = {'Marte', 'Jupiter', 'Venus'}
print(setPlanetas)

# Revisar si un elemento existe dentro de set
print('Marte' in setPlanetas) # Devuelve un True/False
print('Martes' in setPlanetas) # Si el elemento no esta exactamente igual, retornara False

# Agregar un elemento
setPlanetas.add('Tierra') # Agrega un elemento al tipo set
print(setPlanetas)
setPlanetas.add('Tierra') # No se pueden agregar elementos duplicados o repetidos
print(setPlanetas)

# Eliminar elementos

setPlanetas.remove('Jupiter') # Arroja un error si el elemento no existe
print(setPlanetas)
setPlanetas.discard('Tierra') # Si no existe el elemento, no pasa nada. no arroja error
print(setPlanetas)

# Limpiar set
setPlanetas.clear()
print(setPlanetas)

# Eliminar set
del setPlanetas
"""

# Diccionario
"""

# Esta conformado por una llave y un valor
# dict(key, value)

diccionario ={
    'IDE': 'Integrated Development Enviroment',
    'POO': 'Programacion Orientada a Objetos',
    'SABD': 'Sistema de Administracion de Base de Datos'
}
# Verificamos la cantidad de elementos del diccionario
print(diccionario)
print(len(diccionario))

# Acceder a un diccionario con la llave (key)
print(diccionario['IDE']) # Nos imprime el valor de la llave
print(diccionario.get('POO')) # Otra manera de obtener el valor de la llave

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado' # Modificamos el valor de la llave seleccionada
print(diccionario)

# Como recorrer elementos
for i in diccionario: # Recorremos imprimiendo solo las llaves
    print(i)

# Funcion para recorrer un diccionario
for i, n in diccionario.items(): # Usamos la funcion items para poder acceder tambien al valor
                                 # y no solo a la llave
    print(i,n)

# Otras maneras de acceder a un diccionario
for i in diccionario.keys():# Recorremos imprimiendo solo las llaves
    print(i)

for i in diccionario.values(): # Recorremos imprimiendo solo los valores
    print(i)

# Comprobar la existencia de algun elemento
print ('IDE' in diccionario) # Devuelve True/False si el elemento existe

# Agregar un elemento
diccionario['PK'] = 'Primary key' # No pueden haber llaves repetidas
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar Diccionario
diccionario.clear()
print(diccionario)

# Eliminar Diccionario
del diccionario # Eliminamos el diccionario
"""

# Concatenar listas
"""
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1+lista2 # Concatenacion
print(lista3)

lista3.extend([7,8,9]) # Funcion para agregar varios elementos a la lista
print(lista3)

print(lista3.index(3)) # Buscamos un elemento y nos dice en que indice esta

# Saber cuantos valores repetidos hay en una lista
print(lista3.count(1)) # Cuenta la cantidad de veces que se repite el elemento

# Invertir una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = [1,2,3] * 2
print(lista)

# Metodos de ordenamiento
lista.sort() # Ordena elementos de forma ascendente
print(lista)
lista.sort(reverse=True) # Ordena elementos de forma descendente
print(lista)
"""

# Repaso de tuplas
"""
tupla = (1, 'hola', 2.50, [1, 2, 78], 4, 'Hola')
print(tupla)

print(4 in tupla) # Busca un elemento, retorna True/False
# Dentro de las tuplas podemos usar: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla
"""
# Repaso de set o conjunto
# Para definir un conjunto
"""
conjunto1 = set()
conjunto2 = {'bye', }
conjunto1.add(7)
conjunto1.add('Hola')
print(conjunto1)
conjunto2.add('hola')
print(conjunto2)
print(3 not in conjunto2) # Preguntamos si el numiero 3 No esta en el conjunto 1

# Como hacer la igualdad de dos conjuntos
print(conjunto2 == conjunto1) # Preguntamos si son iguales

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Comprueba elementos en comun y lo guarda en conjunto3
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)
conjunto3 = conjunto1 ^ conjunto2 # Son los elementos que estan en los dos conjuntos y no estan compartidos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3)) # Verificamos si un conjunto es subconjunto dentro de otro
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Verificamos si en un conjunto estan todos los elementos de otro conjunto
print(conjunto3.issuperset(conjunto2))
print(conjunto1.issuperset(conjunto3))
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) # Consultamos si hay elementos en comun

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea inmutable
# No se puede agregar, modificar, ni quitar elementos del conjunto
"""
# Repaso Diccionarios
"""
diccionarioNuevo = {
    'Azul' : 'Blue',
    'Rojo' : 'Red',
    'Verde': 'Green',
    'Amarillo' : 'Yellow'
}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Facundo' : {'edad' : 24, 'Altura' : 1.87}, 'Osvaldo' : [45, 1.85], 'Natalia' : [35, 1.67]}
print(diccionario2)
"""


seleccionArgentina = {
    10 : {'Nombre' : 'Lionel Messi', 'Edad' : 35, 'Altura' : 1.70, 'Precio' : '50 Millones', 'Posicion' : 'Extremo Derecho'},
    11 : {'Nombre' : 'Angel Di Maria', 'Edad' : 34, 'Altura' : 1.80, 'Precio' : '12 Millones', 'Posicion' : 'Extremo Derecho'},
    21 : {'Nombre' : 'Paulo Dybala', 'Edad' : 28, 'Altura' : 1.77, 'Precio' : '35 Millones', 'Posicion' : 'Media Punta'},
    19 : {'Nombre' : 'Nicolas Otamendi', 'Edad' : 34, 'Altura' : 1.83, 'Precio' : '3.5 Millones', 'Posicion' : 'Defensa Central'},
    1 : {'Nombre' : 'Franco Armani', 'Edad' : 35, 'Altura' : 1.89, 'Precio' : '3.5 Millones', 'Posicion' : 'Portero'},
    9 : {'Nombre' : 'Julian Alvarez', 'Edad' : 22, 'Altura' : 1.70, 'Precio' : '51 Millones', 'Posicion' : 'Delantero'},
    6 : {'Nombre' : 'Germán Pezzella', 'Edad' : 31, 'Altura' : 1.87, 'Precio' : '5 Millones', 'Posicion' : 'Defensa Central'},
    7 : {'Nombre' : 'Rodrigo De Paul', 'Edad' : 28, 'Altura' : 1.8, 'Precio' : '37 Millones', 'Posicion' : 'Centrocampista'}
}
"""
for key, value in seleccionArgentina.items():
    print(key, value)

# Revisamos la cantidad key : values que estan en el diccionario
print('Cantidad de jugadores cargados: ', end=' ')
print(len(seleccionArgentina))
"""
"""
# Pilas usando listas
pila = [1,2,3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoEliminado = pila.pop() # Quita el ultimo elemento y lo asigna a la variable elementoEliminado
print(f'Sacamos el elemento: {elementoEliminado}')
print(f'Estado actual de pila: {pila}')
"""

# Colas con listas
"""
# Estructuras de datos de tipo fifo (first input / first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

#Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido y se retira: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido y se retira: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido y se retira: {seRetira}')
print(cola)
"""

for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')
