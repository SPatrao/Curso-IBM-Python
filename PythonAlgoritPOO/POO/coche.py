# coche.py

class Coche:
    """
    Clase que representa un coche con atributos como largo, ancho, ruedas, peso, color e is_enMarcha.
    Incluye métodos para arrancar y mostrar el estado del coche.

    Atributos:
        largo (int): La longitud del coche en cm.
        ancho (int): El ancho del coche en cm.
        ruedas (int): El número de ruedas del coche.
        peso (int): El peso del coche en kg.
        color (str): El color del coche.
        is_enMarcha (bool): Indica si el coche está en marcha o no.

    Métodos:
        __init__(self): Constructor de la clase con valores predeterminados.
        arrancar(self): Cambia el estado del coche a "en marcha".
        estado(self): Retorna un mensaje indicando si el coche está arrancado o parado.
    """
    def __init__(self, largo=250, ancho=120, ruedas=4, peso=900, color="rojo", is_enMarcha=False):
        self.largo = largo
        self.ancho = ancho
        self.ruedas = ruedas
        self.peso = peso
        self.color = color
        self.is_enMarcha = is_enMarcha

    def arrancar(self):
        self.is_enMarcha = True

    def estado(self):
        if self.is_enMarcha:
            return "El coche está arrancado"
        else:
            return "El coche está parado"


if __name__ == "__main__":
    # Ejemplo de uso
    coche_1 = Coche()
    print(coche_1.estado())
    coche_1.arrancar()
    print(coche_1.estado())

    # Coche con parámetros personalizados
    coche_2 = Coche(largo=400, ancho=160, ruedas=4, peso=1200, color="amarillo", is_enMarcha=True)
    print(coche_2.estado())