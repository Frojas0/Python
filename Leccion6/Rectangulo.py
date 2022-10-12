class Rectangulo:  # Creacion de la clase
    '''
    Crear una clase llamada Rectangulo, Debe tener 2 atributos: altura y base
    El nombre del metodo sera calcular_area utilizando la formula (area = base * altura), la base y la altura deben ser
    ingresadas por el usuario y los objetos deben ser 3.
    '''

    def __init__(self, base, altura):  # Metodo InitDunder
        self.base = base
        self.altura = altura

    def calcular_area(self):  # Creacion del metodo
        return self.base * self.altura


# Creacion de los Objetos y asignacion de Argumentos
print("Primer Rectangulo: ")
area1 = Rectangulo(int(input("Digite la base: ")), int(input("Digite la altura: ")))
print("Segundo Rectangulo: ")
area2 = Rectangulo(int(input("Digite la base: ")), int(input("Digite la altura: ")))
print("Tercer Rectangulo: ")
area3 = Rectangulo(int(input("Digite la base: ")), int(input("Digite la altura: ")))

# Llamada del metodo con parametros asignados a los 3 objetos
print(f'''
Area del Primer Rectangulo: {area1.calcular_area()}
Area del Segundo Rectangulo: {area2.calcular_area()}
Area del Tercer Rectangulo: {area3.calcular_area()}
''')