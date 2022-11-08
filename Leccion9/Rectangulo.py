# Importamos las clases padre
from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):  # Dunder Init
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    # Metodos
    def calcular_area(self):
        return self.ancho * self.alto

    # Dunder STR
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
