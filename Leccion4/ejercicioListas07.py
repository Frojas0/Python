# Ejercicio 7: Juego adivina el numero
# Realizar un juego para adivinar un numero aleatoreo [1;100], pedir numeros e indicar si es mayor o menor segun sea
# el numero ingresado, mostrar el numero de intentos al acertar el numero correcto.

import random

aleat = random.randint(1, 100)
print(aleat)
num = int(input('Digite el numero: '))
cont = 1

while aleat != num:
    if aleat < num:
        print('El numero ingresado es mayor al Aleatoreo')
    if aleat > num:
        print('El numero ingresado es menor al Aleatoreo')
    num = int(input('Digite el numero: '))
    cont += 1
print(f'Felicidades, el numero era: {aleat}'
      f'\nCantidad de intentos: {cont}')

