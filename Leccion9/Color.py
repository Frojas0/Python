class Color:  # Clase Padre
    def __init__(self, color):  # Inicializado con InitDunder
        self._color = color

    # Getter
    @property
    def color(self):
        return self._color

    # Setter
    @color.setter
    def color(self, color):
        self._color = color

    # Dunder STR
    def __str__(self):
        return f'Color [Color: {self._color}]'