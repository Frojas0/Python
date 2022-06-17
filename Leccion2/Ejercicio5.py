# EJERCICIO5: Sistema de calificaciones
calif = float(input('Ingrese una nota del 0 al 10: '))

if 9 <= calif <= 10:
    print(f'Nota {calif} = A')
if 8 <= calif < 9:
    print(f'Nota {calif} = B')
if 7 <= calif < 8:
    print(f'Nota {calif} = C')
if 6 <= calif < 7:
    print(f'Nota {calif} = D')
if 0 <= calif < 6:
    print(f'Nota {calif} = F')
else:
    print('El valor ingresado es incorrecto')
