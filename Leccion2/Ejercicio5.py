# EJERCICIO5: Sistema de calificaciones
while True:
    try:
        calif = float(input("Escriba su nota: "))
    except:
        print("Debes escribir un número.")
        continue

    if calif < 0 or 10 < calif:
        print("Ingrese una nota válida.")
        continue
    else:
        break

if 9 <= calif <= 10:
    print(f'Nota {calif} = A')
elif 8 <= calif < 9:
    print(f'Nota {calif} = B')
elif 7 <= calif < 8:
    print(f'Nota {calif} = C')
elif 6 <= calif < 7:
    print(f'Nota {calif} = D')
elif 0 <= calif < 6:
    print(f'Nota {calif} = F')
else:
    print('El valor ingresado es incorrecto')
