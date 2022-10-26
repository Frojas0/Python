"""
Tarea: encapsular los atributos y agregar los metodos getters and setters
Crear otro objeto, pasar los datos para nombre, edad y sueldo
Mostrar estos datos, luego modificar y mostrarlos nuevamente
"""


class Persona:  # Esta clase hereda de la clase Object
    def __init__(self, nombre, edad):  # Metodo Init Dunder
        self._nombre = nombre
        self._edad = edad

    def __str__(self):  # Override = Sobreescribir
        return f'Persona: [nombre: {self._nombre}, edad: {self._edad}]'

    # Metodo GETTER
    @property  # decorador
    def nombre(self):
        return self._nombre

    @property  # decorador
    def edad(self):
        return self._edad

    # Metodo SETTER
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad


class Empleado(Persona):  # Esta clase es hija de la clase persona
    def __init__(self, nombre, edad, sueldo):  # Metodo Init Dunder
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: [sueldo: {self._sueldo}] {super().__str__()}'

    # Metodo GETTER
    @property  # decorador
    def sueldo(self):
        return self._sueldo

    # Metodo SETTER
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo


# Creacion de objetos y asignacion de datos
empleado1 = Empleado('Facundo', 24, 75000)
empleado2 = Empleado('Agustin', 25, 500)

# Muestra de datos con metodo GET
print(f'Empleado1: {empleado1.nombre, empleado1.edad, empleado1.sueldo}')
print(f'Empleado2: {empleado2.nombre, empleado2.edad, empleado2.sueldo}')

# Modificacion de datos con el metodo SET
empleado1.nombre = 'Jose'
empleado2.nombre = 'Juancarlos'

empleado1.edad = 22
empleado2.edad = 26

empleado1.sueldo = 67000
empleado2.sueldo = 74567

# Muestra de datos con metodo GET
print(f'Empleado1 modificado: {empleado1.nombre, empleado1.edad, empleado1.sueldo}')
print(f'Empleado2 modificado: {empleado2.nombre, empleado2.edad, empleado2.sueldo}')
