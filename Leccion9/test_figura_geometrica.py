from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

# Creacion de objetos
cuadrado1 = Cuadrado(5, 'Azul')
cuadrado2 = Cuadrado(2, 'Verde')
cuadrado3 = Cuadrado(11, 'Rosado')

rectangulo1 = Rectangulo(2, 3, 'Gris')
rectangulo2 = Rectangulo(3, 1, 'Naranja')
rectangulo3 = Rectangulo(3, 3, 'Morao')

print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'Calculo del area: {cuadrado1.calcular_area()}')

# MRO = Method Resolution Order
print(Cuadrado.mro())

# Impresion objetos
print(cuadrado1)
print(cuadrado2)
print(cuadrado3)
print()
print(rectangulo1)
print(rectangulo2)
print(rectangulo3)
print()

# Calculo de Area
print(f'Calculo del area cuadrado1: {cuadrado1.calcular_area()}')
print(f'Calculo del area cuadrado2: {cuadrado2.calcular_area()}')
print(f'Calculo del area cuadrado3: {cuadrado3.calcular_area()}')
print()
print(f'Calculo del area rectangulo1: {rectangulo1.calcular_area()}')
print(f'Calculo del area rectangulo2: {rectangulo2.calcular_area()}')
print(f'Calculo del area rectangulo3: {rectangulo3.calcular_area()}')