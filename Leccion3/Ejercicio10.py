# EJERCICIO 10: Calcular el factorial de un numero mayor o igual a 0
i = 0
num = -1
while num < i:
    num = int(input('Digite un numero: '))
i = 1
factorial = 1
while i <= num:
    factorial *= i
    i += 1
print(f'El factorial de {num} es: {factorial}')
