# Ejercicio 4: Sumar numeros pares dentro de un rango
# Hacer un programa para sumar numeros pares dentro de un rango.
# Ejemplo: suma de numero pares del 2 al 30; suma = 240

ini = int(input('Digite el valor inicial del rango: '))
fin = int(input('Digite el valor final del rango: '))
sum = 0
lista = list(range(ini, fin+1))
for i in lista:
    if i % 2 == 0:
        sum += i
print(f'Rango de la lista: [{ini};{fin}]\n'
      f'La suma de pares dentro de la lista es: {sum}')


