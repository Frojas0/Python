# Ejercicio 8: Menu interactivo - Cajero automatico
# Hacer un programa que simule un cajero automatico con un saldo inicial de $1000, tendra el siguiente menu de opciones
#       1. Ingresar dinero en la cuenta
#       2. Retirar dinero de la cuenta
#       3. Mostrar dinero disponible
#       4. Salir
import time

saldo = 1000
def menu(): # Crea el menu como una funcion
    print(f'1. Ingresar dinero en la cuenta'
        f'\n2. Retirar dinero de la cuenta'
        f'\n3. Mostrar dinero disponible'
        f'\n4. Salir')
menu()
condicion = int(input('Seleccione una opcion: '))

while condicion not in range(1,5): # Asegura valor entre [1;4]
    condicion = int(input('Seleccione una opcion: '))

while condicion != 4:
    if condicion == 1:
        ingreso = int(input('Cuanto dinero desea ingresar?: '))
        saldo += ingreso
        menu()
        condicion = int(input('Seleccione una opcion: '))

    elif condicion == 2:
        retiro = int(input('Cuanto dinero desea retirar?: '))
        if retiro <= saldo:
            saldo -= retiro
        else:
            print('Saldo insuficiente:')
        menu()
        condicion = int(input('Seleccione una opcion: '))

    elif condicion == 3:
        print(f'Dinero disponible: {saldo}')
        time.sleep(2) # Espera 2 segundos
        menu()
        condicion = int(input('Seleccione una opcion: '))