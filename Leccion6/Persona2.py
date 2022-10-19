class Persona2:  # Creamos la clase

    def __init__(self, nombre, apellido, edad):  # Creamos metodo Init Dunder
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):  # Creamos metodo
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    # Metodo GETTER
    @property  # decorador
    def nombre(self):  # Metodo getter
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    # Metodo SETTER
    @nombre.setter
    def nombre(self, nombre):  # Metodo setter
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):  # Metodo setter
        self._apellido = apellido

    @edad.setter
    def edad(self, edad):  # Metodo setter
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')


if __name__ == '__main__':
    persona1 = Persona2('Facundo', 'Rojas', 24)
    # persona1._nombre Acceder a un parametro encapsulado sin metodo getter es mala practica

    # LLamamos al metodo GET
    print(persona1.nombre)
    print(persona1.apellido)
    print(persona1.edad)

    # Utilizamos el metodo SET
    persona1.nombre = 'Juancarlo'
    persona1.apellido = 'Chupetin'
    persona1.edad = 244

    # Llamamos al metodo GET
    print(persona1.nombre)

    # Verificamos los datos
    print(persona1.mostrar_detalle())

    # Actividad:
    # Crear 3 objetos mas utilizando los metodos getter and setter
    persona2 = Persona2('aaa', 'aaa', 1)
    persona3 = Persona2('bbb', 'bbb', 2)
    persona4 = Persona2('ccc', 'ccc', 3)

    # Metodo GET
    # muestro valores
    print(persona2.nombre, persona2.apellido, persona2.edad)
    print(persona3.nombre, persona3.apellido, persona3.edad)
    print(persona3.nombre, persona3.apellido, persona3.edad)

    # Metodo SET
    persona2.nombre = 'Agustin'
    persona3.nombre = 'Gino'
    persona4.nombre = 'Critiancritian'

    persona2.apellido = 'Ramirez'
    persona3.apellido = 'Mazorca'
    persona4.apellido = 'Setecapoelpesho'

    persona2.edad = 25
    persona3.edad = 26
    persona4.edad = 26

    # Muestro Modificaciones

    print(persona2.mostrar_detalle())
    print(persona3.mostrar_detalle())
    print(persona4.mostrar_detalle())

    print(__name__)
