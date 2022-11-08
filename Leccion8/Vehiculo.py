"""
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Auto y Bicicleta, las cuales heredan de la
    clase padre Vehiculo. La clase padre debe tener los siguientes atributos y metodos:
    Vehiculo (clase padre)
    -Atributos(color, ruedas)
    -Metodos(__init__(color, ruedas) y __str())

    Auto(clase hija de Vehiculo)
    -Atributos(velocidad (Km/hr))
    -Metodos(__init__(color, ruedas, velocidad) y __str__())

    Bicicleta (Clase hija de Vehiculo)
    -Atributos(tipo(urbana/montaña/etc.)
    -metodos(__init__(color, ruedas, tipo) y __str__())

    Crear un objeto de cada clase
"""


# CREACION DE CLASES
class Vehiculo:  # Clase padre
    def __init__(self, color, ruedas):  # Metodo InitDunder
        self.color = color
        self.ruedas = ruedas

    def __str__(self):  # Metodo Dunderstr, Override / Sobreescribir
        return f'Color: {self.color}, Ruedas: {self.ruedas}'


class Auto(Vehiculo):  # Clase hija
    def __init__(self, color, ruedas, velocidad):  # Metodo InitDunder
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):  # Metodo Dunderstr, Override / Sobreescribir
        return f'Auto = Velocidad: {self.velocidad}km/h {super().__str__()}'


class Bicicleta(Vehiculo):  # Clase hija
    def __init__(self, color, ruedas, tipo):  # Metodo InitDunder
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):  # Metodo Dunderstr, Override / Sobreescribir
        return f'Bicicleta = Tipo: {self.tipo}, {super().__str__()}'


# CREACION DE OBJETOS Y ASIGNACION DE DATOS
# Objeto de la clase Vehiculo
vehiculo1 = Vehiculo('-', '-')  # los datos los asigno en las clases Auto/Bicicleta

# Objetos de la clase Auto
vehiculo2 = Auto("Azul", 4, 120)
vehiculo3 = Auto("Negro", 4, 200)
vehiculo4 = Auto("Celeste", 4, 160)
vehiculo5 = Auto("Amarillo", 4, 145)

# Objetos de la clase Bicicleta
vehiculo6 = Bicicleta("Gris", 2, "Todo terreno")
vehiculo7 = Bicicleta("Cyan", 2, "Ciudad")
vehiculo8 = Bicicleta("Violeta", 2, "BMX")
vehiculo9 = Bicicleta("Bordo", 2, "Descenso")

# MUESTRA DE DATOS
print(vehiculo1)
print()
print(vehiculo2)
print(vehiculo3)
print(vehiculo4)
print(vehiculo5)
print()
print(vehiculo6)
print(vehiculo7)
print(vehiculo8)
print(vehiculo9)
