# EJERCICIO2: Determinar la solucion logica
a = int(input('Ingrese el valor de a: '))
b = int(input('Ingrese el valor de b: '))
var = ((3 + 5 * 8) < 3 and ((-6 / 3 * 4) + 2 < 2)) or (a > b)
print('Solucion: Verdadera') if var else print('Solucion: Falsa')

# EJERCICIO3: Intercambiar el valor de dos variables
a = 10
b = 5
if a == 10:
    a = 5
if b == 5:
    b = 10
print(f'Valor de a: {a} ; Valor de b: {b}')

# EJERCICIO4: Area y longitud de un circulo
import math

pi = math.pi
radio = float(input('Ingrese el radio de un circulo: '))
area = pi * (radio ** 2)
longitud = 2 * pi * radio

print(f'''
Radio: {radio}
Area: {area}
Longitud: {longitud}
Pi: {pi}
''')
