class Persona:  # Creamos una clase

    def __init__(self, nombre, apellido,dni , edad, *args, **kwargs):  # Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):  # self es igual a this
        print(f'La Clase Persona tiene los siguientes datos:{self.nombre} {self.apellido}, Dni: {self._dni}, Edad: {self.edad}, direccion: {self.args}, datos importantes: {self.kwargs}')


persona1 = Persona('Facundo', 'Rojas', 40070094,24)  # Enviamos argumentos desde el cpnstructor
persona2 = Persona('Agustin', 'Martinez', 23321233, 24)

print(f'El Objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}, Edad {persona1.edad}')
print(f'El Objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}, Edad {persona2.edad}')

# Modificamos argumentos 1 a 1
persona1.nombre = 'Juan'
persona1.apellido = 'Carlos'
persona1.edad = 23
print(f'El Objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido}, Edad {persona1.edad}')

# Los atributos son: Caracteristicas
# Los metodos son: el comportamiento que van a tener los objetos (objetos)
persona1.mostrar_detalle()  # La referencia se pasa de forma automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia o dara error (pasamos objeto persona1) no se usa

persona1.telefono = '24433445'  # Hemos creado un atributo desde un objeto
print(f'Telefono de persona1:{persona1.nombre}, {persona1.telefono}')

# print(persona2.telefono) El pbjeto persona2 no tiene el atributo telefono, da error
persona3 = Persona('Rogelio', 'Romero', 33234432, 22, 'Telefono', '234452323', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo=2021)
persona3.mostrar_detalle()
# print(persona3._dni) El atributo esta encapsulado, no deberia poder ser llamado fuera de la clase, esto es una mala practica
# persona3.__nombre El atributo nombre esta totalmente encapsulado

