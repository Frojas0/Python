# EJERCICIO9: Calificacion promedio y mas baja
suma = 0
calificacionBaja = 99999

for i in range(0, 10):
    # este condicional nos obliga a ingresar una nota valida
    while True:
        try:
            calificacion = float(input(f"Digite una calificación  {i + 1}: "))
        except   :
            print("Debes escribir un número.")
            continue

        if calificacion < 0 or 10 < calificacion:
            print("Ingrese una nota válida.")
            continue
        else:
            break

    suma = suma + calificacion
    if calificacion < calificacionBaja:
        calificacionBaja = calificacion

calificacioPromedio = suma / 10
print(f"""
La calificación promedio es: {calificacioPromedio}
La calificacion mas baja es: {calificacionBaja}
""")
