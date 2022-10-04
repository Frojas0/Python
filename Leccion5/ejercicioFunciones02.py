# Ejercicio02: Funcion con *args para multiplocar
# Crear una funcion para multiplicar los valores recibidos de tipo numerico, utilizando argumentos variables *args como
# parametro de la funcion y regresar como resultado la multiplicacion de todos los valores pasados como argumento.

def multiplicacion (*args): # Creo funcion con numero de argumentos indefinidos
    resultado = 1 # Inicio con uno por que con cero nos dara siempre un resultado igual a cero
    for i in args:
        resultado *= i
    return resultado

print(multiplicacion(2,2,3)) # Imprimo la funcion con argumentos hardcodeados