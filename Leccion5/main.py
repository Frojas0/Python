# Comenzamos con funciones

# Definimos una funcion
def mi_funcion():  # Para identificar una funcion utilizamos parentesis
    print('Saludos a todos desde Mi Funcion')


mi_funcion()  # LLamamos a la funcion


# Desenpaquetado de listas o list Unpacking
def show(name, lastname):  # necesita dos parametros
    print(name + ' ' + lastname)


person = ["Juan", "Cruz"]
show(person[0], person[1])  # Pasamos uno por uno los datos de la lista a la funcion
show(*person) # Aca pasa todos los datos juntos

person2 = ("Osvaldo", "Veniabuscarajuancruz") # Desempaquetamos a travez de una tupla
show(*person2)

person3 = {"lastname": "Lucero", "name": "Natalia"}
show(**person3)

# Repaso variable for-else

numbers = [1,2,3,4,5]
for i in numbers:
    print(i)
    if i == 3:
        break # Esta es la unica forma de que no se ejecute el else
else:
    print('Esto se termino')

# List comprehension, lista de compresion
# Permite tomar elementos de listas y diccionarios sin modificarlos en nada

names = ["Juancruz", "Rodrigo", "Jorge", "Franco", "Paolo", "Pepe"]
alongP = [p for p in names if p[0] == 'P'] # Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(bottleC)
print(Arg)

# Paso de Argumentos

def mi_funcion2(name, lastName): # Parametros: Variables que declaramos en la funcion
    print("Saludos a todos")
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion2('Jorge', 'Lucero') # Argumentos: Valor que enviamos a la funcion
mi_funcion2('Juan', 'Carlo') # le pasamos un argumento diferente

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a,b):
    return a + b
#resultado = sumar(3,2)
#print(f'EL resultado de la suma es: {resultado}')
print(f'EL resultado de la suma es: {sumar(44,23)}') # Podemos llamar a la funcion desde un print

def sumar_2(a = 0, b = 0): # Determino un valor por default en los parametros de mi funcion
    return a + b
resultado = sumar_2() # no le asigno argumentos, utilizara los parametros default
print(f'Resultado: {resultado}')
print(f'Resultado: {sumar_2(23,22)}') # Le asigno argumentos a la funcion

# Argumentos, variables en funciones
def listarNombres(*nombres): # Normalmente utilizamos: *args
    for i in nombres: # Se va a convertir en tuplas
        print(i)
listarNombres('Jose', 'Marcos', 'Claudia', 'Rosa', 'Juancarlo') # Hardcodeo argumentos
listarNombres('Pablo', 'Daniel', 'Romina', 'Pepe', 'Marcela') # Agrego mas argumentos