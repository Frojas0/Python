print('Hola Mundo')

# Clase 2
# Variables en Python

miVariable = 3
print(miVariable)
miVariable = "Hola a todo aquel que lea"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 5
y = 2
z = x + y
print(z)
# Las literales se escriben con x752, los ultimos 3 numeros de su id
print(id(y))
print(id(z))
# Ejemplo Variable x = x752 serian las literales de la variable a esto se lo conoce como referencia de memoria

# Clase 3:
# Tipos de datos en Python: Int, Float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = 'Hola a todos'
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas
miGrupoFavorito = "Queen"
caracteristicas = "La de Freddie"
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))  # Conversion a entero

# Tipos Bool
miBooleano = 3 > 3
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# funcion input
#resultado = input("Digite un numero: ")  # regresa un dato tipo string
#print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escibe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)

# Ejercicio 1 //Califica tu dia del 1 al 10
consulta = "Como estuvo tu dia?"
respuesta = 10
print(consulta)
print("Mi dia estuvo de: ", respuesta)

# Ejercicio 2 // Libro
titulo = input("Proporciona el titulo: ")
autor = input ("Proporciona el autor: ")
print(titulo, "fue escrito por", autor)

