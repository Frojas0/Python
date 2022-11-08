class FiguraGeometrica:  # Clase Padre
    def __init__(self, ancho, alto):  # Inicializado con InitDunder
        self._ancho = ancho
        self._alto = alto

    # Getter
    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto

    # Setter
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    # Dunder STR
    def __str__(self):
        return f'Figura Geometrica [Ancho: {self._ancho}, Alto: {self._alto}]'
