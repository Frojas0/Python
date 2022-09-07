# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los elementos del 1 al 10, luego modificar los elementos de la lista multiplicandolos
# por un valor ingresado por el usuario

i = 1
lista = []
n = float(input('Digite un numero multiplicador: '))
while i <= 10:
    lista.append(i * n)
    i += 1
print(f'Lista original: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n'
      f'Multiplicada por {n}: {lista}')

# Metodo dado en clases
lista = list(range(1, 11))
print('lista Original')
for i in lista:
    print(i, end='-')
valor = int(input('Digite un valor a multiplicar: '))

# Multiplicamnos los elementos de la lista
for i, j in enumerate(lista):  # modifica los indices de la lista
    lista[i] *= valor
    print(i, j)

print(f'Lista final con los elementos multiplicados por {valor}')
for i in lista:
    print(i, end='-')
