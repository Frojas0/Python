# Ejercicio 01: Crear una funcion para sumar los valores recibidos de tipo numericos, utilizando argumentos variables
# *args como parametro de la funcion, y agregar como resultado la suma de todos los valores pasados como argumentos.

def suma(*args):  # Recibimos una cantidad de parametros indefinidos
    resultado = 0
    # iteramos cada elemento
    for i in args:
        resultado += i
    return resultado


# Llamamos a la funcion
print(suma(3, 2, 1, 4, 2, 1)) # harcodeo argumentos
