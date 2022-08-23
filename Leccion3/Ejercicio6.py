# EJERCICIO6: Año bisiesto?

print('Comprobamos que año es bisiesto')
opcion = 0
while opcion != 1:
    anio = int(input('Ingrese un año: '))
    if ((anio % 4 == 0) and (anio % 100 != 0)) or (anio % 400 == 0):
        print('EL año es bisiesto')
    else:
        print('El año no es bisiesto')
    opcion = int(input(f'''
    0: Para continuar
    1: Para salir
    Digite una opcion: '''))
