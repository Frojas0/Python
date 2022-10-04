# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa

def deCaF(celcius): # de Celcius a Fahrenheit
    return (celcius * 9/5) + 32


def deFaC(fahrenheit): # de Fahrenheit a Celcius
    return (fahrenheit - 32) * 5/9

# pido argumentos
celcius = (int(input('Digite grados C° a transformar: ')))
fahrenheit = (int(input('Digite grados F° a transformar: ')))

# llamo a las funciones con los argumentos dados
print(f'''
{celcius}C° = {deCaF(celcius)}F°
{fahrenheit}F° = {deFaC(fahrenheit)}C°
''')