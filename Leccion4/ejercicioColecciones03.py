# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza : Dunadan del norte
# Nombre: Gandalf
# Clase: Mago
# Raza : Istar
# Nombre: Legolas
# Clase: Arquero
# Raza : Elfo Sindar


# creacion de diccionarios
aragon = {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dunadan del norte'}
gandalf = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
legolas = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
frodo = {'Nombre': 'Frodo Bolson', 'Clase': 'Explorador', 'Raza': 'Hobbit'}
arwen = {'Nombre': 'Arwen', 'Clase': 'Elfo', 'Raza': 'Peredhil'}
samwise = {'Nombre': 'Samwise Gamgee', 'Clase': 'Explorador', 'Raza': 'Hobbit'}

# agrego diccionarios a una lista
lista = []
lista.append(aragon)
lista.append(gandalf)
lista.append(legolas)
lista.append(frodo)
lista.append(arwen)
lista.append(samwise)

# imprimo la lista
print(lista)