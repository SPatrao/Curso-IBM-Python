# encapsulacion.py

class Coche:
    """
    Clase que simula la encapsulación en Python para representar un coche.

    Atributos:
        __largo (int): Largo del coche (privado).
        __ancho (int): Ancho del coche (privado).
        __ruedas (int): Número de ruedas del coche (privado).
        __peso (int): Peso del coche (privado).
        __color (str): Color del coche (privado).
        __is_enMarcha (bool): Indica si el coche está en marcha (privado).

    Métodos:
        __init__(self): Constructor de la clase.
        arrancar(self): Arranca el coche (simula modificar un atributo privado).
        estado(self): Devuelve el estado del coche.
    """
    def __init__(self):
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__peso = 900
        self.__color = "rojo"
        self.__is_enMarcha = False

    def arrancar(self):
        self.__is_enMarcha = True

    def estado(self):
        if self.__is_enMarcha:
            return "El coche está arrancado"
        else:
            return "El coche está parado"


if __name__ == "__main__":
    # Ejemplo de uso
    mi_coche = Coche()
    print(mi_coche.estado())
    mi_coche.arrancar()
    print(mi_coche.estado())