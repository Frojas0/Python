# Ejercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos. Crear un diccionario donde la clave sea el nombre del usuario
# y el valor sea el telefono, el programa tendra el siguiente menu de opciones:
#   1. Nuevo contacto
#   2. Borrar contacto
#   3. Ver contactos existentes
#   4. Salir


agenda = {} # Creo un diccionario llamado agenda
def menu():  # Creo el menu de opciones
    print(f'1. Nuevo contacto'
          f'\n2. Borrar contacto'
          f'\n3. Ver contactos existentes'
          f'\n4. Salir')


while True:
    menu()
    opcion = int(input('Digite una opcion: '))

    if opcion == 1:
        nombre = input('Digite nombre del contacto: ') # nombre sera la clave en el diccionario
        telefono = input('Digite el numero telefonico: ') # telefono sera el valor en el diccionario
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente')
        else:
            print('El contacto ya existe')

    elif opcion == 2:
        nombre = input('Digite el nombre del contacto: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Contacto eliminado exitosamente')
        else:
            print('El contaco no existe en la agenda')

    elif opcion == 3:
        print('Agenda de contactos')

        for i, j in agenda.items():  # i=clave; j=valor
            print(f'Nombre: {i}, Telefono: {j}')

    elif opcion == 4:
        print('Saliendo...')
        break
    else:
        print('Opcion digitada no valida')
    print()