# Ejercicio1 : Sacar la raiz cuadrada de un numero positivo

import math # importa la clase math
n = int(input('Digite un numero positivo: ')) # Solicitamos el entero n

while n < 0:
    print('Se espera un numero positivo')
    n = int(input('Digite un numero positivo: '))
print(f'Raiz cuadrada de {n}: {math.sqrt(n):.2f}') # .2f limita la cantidad de decimales
