# Importamos Clases Padre
from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):  # Inicializado con el metodo DunderInit
        # super().__init__(lado) No lo utilizaremos para herencias de padres multiples
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    # Metodos
    def calcular_area(self):
        return self.alto * self.ancho

    # Dunder STR
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
