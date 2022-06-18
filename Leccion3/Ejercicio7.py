# EJERCICIO7: Calcular la suma de 'n' primeros numeros

n = int(input('Digite la cantidad de numeros a sumarse: '))
suma = 0
i = 0
while i <= n:
    suma = suma + i
    i += 1
print(f'La suma es: {suma}')
