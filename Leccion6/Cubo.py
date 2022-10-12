class Cubo:  # Creacion de la clase
    """
    Crear la clase Cubo con los atributos: ancho, alto y profundidad
    con el metodo: calcular_volumen utilizando la formula(volumen = ancho * altura * profundidad)
    el usuario debera ingresar los valores.
    """

    def __init__(self, ancho, altura, profundidad):  # Metodo InitDunder
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):  # Creacion del metodo
        return self.ancho * self.altura * self.profundidad


# Creacion de el objeto
volumen1 = Cubo(int(input("Digite el ancho: ")), int(input("Digite el alto: ")), int(input("Digite la profundidad: ")))

# Llamada del metodo con parametros asignados a el objeto volumen1
print(f"Volumen del cubo 1: {volumen1.calcular_volumen()}m3")