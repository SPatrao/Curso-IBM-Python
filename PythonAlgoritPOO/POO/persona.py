# persona.py

class Persona:
    """
    Clase que representa a una persona.

    Atributos:
        nombre (str): Nombre de la persona.
        edad (int): Edad de la persona.
        lugar (str): Lugar de origen de la persona.

    Métodos:
        __init__(self, nombre, edad, lugar): Constructor de la clase.
        descripcion(self): Imprime una descripción de la persona.
    """
    def __init__(self, nombre, edad, lugar):
        self.nombre = nombre
        self.edad = edad
        self.lugar = lugar

    def descripcion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Lugar: {self.lugar}")


class Empleado(Persona):
    """
    Clase que representa a un empleado, heredando de la clase Persona.

    Atributos adicionales:
        salario (float): Salario del empleado.
        antiguedad (int): Antigüedad del empleado.

    Métodos adicionales:
        __init__(self, salario, antiguedad, nombre, edad, lugar): Constructor de la clase.
        descripcion(self): Imprime una descripción del empleado, incluyendo la información de la clase padre.
    """
    def __init__(self, salario, antiguedad, nombre, edad, lugar):
        super().__init__(nombre, edad, lugar)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print(f"Salario: {self.salario}, Antigüedad: {self.antiguedad}")


if __name__ == "__main__":
    # Ejemplo de uso
    angel = Persona("Angel", 43, "Málaga")
    angel.descripcion()

    empleado1 = Empleado(2000, 5, "Manolo", 33, "Madrid")
    empleado1.descripcion()