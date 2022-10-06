class Persona:  # Creamos una clase

    def __init__(self, nombre, apellido, edad):  # Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido}, Edad: {self.edad}')


persona1 = Persona('Facundo', 'Rojas', 24)  # Enviamos argumentos desde el cpnstructor
persona2 = Persona('Agustin', 'Martinez', 24)

print(f'El Objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}, Edad {persona1.edad}')
print(f'El Objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}, Edad {persona2.edad}')

# Modificamos argumentos 1 a 1
persona1.nombre = 'Juan'
persona1.apellido = 'Carlos'
persona1.edad = 23
print(f'El Objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido}, Edad {persona1.edad}')

# Los atributos son: Caracteristicas
# Los metodos son: el comportamiento que van a tener los objetos (objetos)
persona1.mostrar_detalle()
persona2.mostrar_detalle()