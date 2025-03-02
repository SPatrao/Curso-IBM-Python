# polimorfismo.py

class Empleado:
    """
    Clase que representa a un empleado genérico.

    Atributos:
        nombre (str): Nombre del empleado.
        sueldo (float): Sueldo del empleado.

    Métodos:
        __init__(self, nombre, sueldo): Constructor de la clase.
        mostrar_detalles(self): Devuelve los detalles del empleado.
    """
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f"Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]"

    def mostrar_detalles(self):
        return self.__str__()


class Gerente(Empleado):
    """
    Clase que representa a un gerente, heredando de la clase Empleado.

    Atributos adicionales:
        departamento (str): Departamento del gerente.

    Métodos adicionales:
        __init__(self, nombre, sueldo, departamento): Constructor de la clase.
        __str__(self): Devuelve una representación en cadena del objeto.
    """
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f"Gerente [Departamento: {self.departamento}] {super().__str__()}"


def imprimir_detalles(objeto):
    print(type(objeto))
    print(objeto.mostrar_detalles())


if __name__ == "__main__":
    # Ejemplo de uso
    empleado = Empleado("Juan", 5000)
    imprimir_detalles(empleado)

    gerente = Gerente("Karla", 6000, "Sistemas")
    imprimir_detalles(gerente)