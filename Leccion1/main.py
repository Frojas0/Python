'''
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
'''  # Triple comilla para comentario extenso

"""
# Operadores aritmeticos
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("Resultado de la suma: ", suma)
print(f'El resultado de la suma es: {suma}') # Imprimiendo con Format (INTERPOLACION)

resta = operandoA - operandoB
print(f'El resultado de la resta es: {resta}')

multiplicacion = operandoA * operandoB
print(f'EL resultado de la multiplicacion es: {multiplicacion}')

division = operandoA / operandoB
print(f'El resultado de la division es: {division}')
division = operandoA //operandoB # TRUNCADO
print(f'El resultado de la division es: {division}')

modulo = operandoA % operandoB
print(f'El resultado del modulo es: {modulo}')

exponente = operandoA ** operandoB
print(f'El resultado del exponente es: {exponente}')

a = int(input('Escribe el valor de a'))
"""
"""
# EJERCICIO: Calcular area y perimetro de un rectangulo

alto = int(input("Ingrese la altura del Rectangulo: "))
ancho = int(input("Ingrese el ancho del Rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f'''
Altura proporcionada: {alto}
Ancho proporcionado: {ancho}
Area del rectangulo: {area}
Perimetro del rectangulo: {perimetro}
''')
"""
"""
miVariable3 = 10
print(miVariable3)

# Operadores de reasignacion

miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 +=  1 # Incremento
print(miVariable3)

miVariable3 -= 2 # Decremento
print(miVariable3)

miVariable3 *= 3 # Producto
print(miVariable3)

miVariable3 /= 2 # Division
print(miVariable3)

# Operadores de comparacion

d = 4
b = 2
resultado = d == b # Comprobamos igualdad
print(resultado)

resultado = d != b # Comprobamos desigualdad
print(resultado)

resultado = d > b # Operador mayor que
print(resultado)

resultado = d < b # Operador menor que
print(resultado)

resultado = d <= b # Operador menor o igual que
print(resultado)

resultado = d >= b # Operador mayor o igual que
print(resultado)
"""
"""
# EJERCICIO 1: Numero par o impar
variable = int(input("Ingrese un numero: "))
if variable % 2 == 0:
    print(f"El numero {variable} es PAR")
else:
    print(f"El numero {variable} es IMPAR")

# EJERCICIO 2: Determinar si es mayor de edad
edad = int(input("Ingrese su edad"))
if edad >= 18:
    print(f"Tu edad es: {edad}años, eres mayor de edad")
else:
    print(f"Tu edad es: {edad}años, eres menor de edad")
"""
"""
# Operadores Logicos

a = False
b= True
resultado = a and b # and (operador binario)
print(resultado)

resultado = a or b # or (operador binario)
print(resultado)

resultado = not a # not (operador unario)
print(resultado)
"""

"""
# EJERCICIO: Valor dentro de un rango

valor = int(input("Ingrese un numero: "))
if 0 <= valor <= 5: # es lo mismo que decir (valor >= 0 and valor <=5)
    print(f"El valor {valor} esta dentro del rango")
else:
    print(f"El valor {valor} no esta dentro del rango")
"""
"""
# EJERCICIO: Operador or
vacaciones = True
diaLibre = False
if vacaciones or diaLibre:
    print("Puede asistir al juego")
else:
    print("Tiene trabajo que hacer")
"""
"""
# EJERCICIO: Rango entre edades
edad = int(input("Digite su edad"))

# se deben respetar los tabulados en bloques de codigo (identacion)
if (20<= edad <30) or (30<= edad <40):
    print(f"Tienes {edad} Estas en el rango de 20'30")
else:
    print(f"Tienes {edad} estas fuera del rango de los 20/30")
"""
"""
# EJERCICIO1: El mayor de dos numeros
num1 = int(input("Digite el valor para el numero1: "))
num2 = int(input("Digite el valor para el numero2: "))
if num1 > num2:
    print(f"El numero mayor es: {num1}")
else:
    print(f"El numero mayor es: {num2}")
"""
"""
# EJERCICIO: Tienda de libros
nombre = input("Digite el nombre del libro: ")
id = input("Digite el ID del libro: ")
precio = float(input("Digite el precio del libro: "))
envio = input("Envio gratis? (True/False): ")

if envio == "True":
    envio = "El envio es Gratuito"
elif envio == "False":
    envio = "El envio No es gratuito"
else:
    envio = "Valor incorrecto, ingrese: True/False"

print(f"""
#Nombre: {nombre}
#ID: {id}
#Precio: ${precio}
#{envio}
""")
"""
