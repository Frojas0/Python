# Ejercicio 3: Funcion Recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas, puede ser cualquier valor positivo,
# por ejemplo, si pasamos el valor de 5 debe imprimir:
# 5
# 4
# 3
# 2
# 1
# si ingresa un numero negativo no imprimir nada.

def impresionDescendente(num):
    if num >= 1: # caso base
        print(num)
        impresionDescendente(num-1) #caso recursivo
    elif num == 0: # esto para que no nos largue el mensaje del siguiente elif al llegar a cero
        return
    elif num < 0:
        print('Se esperaba un positivo mayor de cero')

num = int(input('Digite un numero: '))
impresionDescendente(num)