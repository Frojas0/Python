# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10.
# Ejemplo: Si digita el 5 la lista tendra: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50.

lista = []
num = int(input('Digite el numero a multiplicar: '))
for i in range(1, 11):
   lista.append(num*i)
print(lista)