class Aritmetica:  # Creamos la clase
    """
    Esto es un comentario tipo: DocString
    esta es documentacion de la clase en python
    Vamos a hacer en esta clase algunas operaciones de: suma, resta, multiplicacion y mas
    """

    def __init__(self, operadorA, operadorB):  # Metodo InitDunder
        self.operadorA = operadorA
        self.operadorB = operadorB

    # Metodo para sumar
    def sumar(self):
        return self.operadorA + self.operadorB

    # Metodo para restar
    def restar(self):
        return self.operadorA - self.operadorB

    # Metodo para multiplicar
    def multiplicar(self):
        return self.operadorA * self.operadorB

    # Metodo para dividir
    def dividir(self):
        return self.operadorA / self.operadorB


# Creamos el objeto y le pasamos los argumentos
aritmetica1 = Aritmetica(7, 5)

# Llamamos a los metodos con los parametros del objeto aritmetica1

print(f'La suma de los numeros es: {aritmetica1.sumar()}')
print(f'La resta los numeros es: {aritmetica1.restar()}')
print(f'La multiplicacion de los numeros es: {aritmetica1.multiplicar()}')
print(f'La division de los numeros es: {aritmetica1.dividir():.2f}')  # :.2f trunca a 2 decimales
