# Ejercicio 5Ñ Factorial de un numero positivo
# Hacer un programa para calcular el factorial de un numero positivo

num = int(input('Digite un numero positivo: '))
while num < 0:
    num = int(input('Digite un numero positivo: '))

fac = 1
for i in range(1, num+1):
    fac *= i

if num != 0:
    print(f'Factorial de {num}: {fac}')
else:
    print(f'Factorial de {num}: 0')
