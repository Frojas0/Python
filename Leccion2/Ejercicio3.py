# EJERCICIO 3: Calcular estacion del año
mes = int(input('Ingrese un mes del año 1-12: '))
if mes == 1 or mes == 2 or mes == 3:
    estacion = 'Verano'
elif mes == 4 or mes == 5 or mes == 6:
    estacion = 'Otoño'
elif mes == 7 or mes == 8 or mes == 9:
    estacion = 'Invieno'
elif mes == 10 or mes == 11 or mes == 12:
    estacion = 'Primavera'
else:
    estacion = 'Valor ingresado fuera de rango'

print(f'Estacion: {estacion}')
