# CLASE8: Ciclo While (mientras)
"""
contador = 0
while contador < 8:
    print('Ejecutamos nuestro ciclo while ', + contador)
    contador += 1
else:
    print('Fin del ciclo while')
"""

# EJERCICIO: Contador con while
"""
maximo = 5
contador = 0
while contador <= maximo:
    print(f'Valor actual {contador}')
    contador += 1
else:
    print(f'EL contador llego a {contador}, fin del ciclo')
"""

# EJERCICIO: Contador decreciente con while
"""
minimo = 1
contador = 5
while contador >= minimo:
    print(f'Valor actual {contador}')
    contador -= 1
else:
    print(f'El valor llego a {contador}, fin del ciclo')
"""

# Ciclo for (para)
"""
cadena = 'Hello'
for letra in cadena:
    print(letra)
else:
    print('Fin del ciclo for')
"""

# Palabra reservada: break
"""
for letra in 'Alemania':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('FIn del ciclo for')
"""
# Palabra reservada: continue
"""
for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')
"""