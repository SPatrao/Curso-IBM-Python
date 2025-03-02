# vehiculo.py

class Vehiculo:
    """
    Clase padre que representa un vehículo genérico.

    Atributos:
        marca (str): Marca del vehículo.
        modelo (str): Modelo del vehículo.
        color (str): Color del vehículo.
        arrancado (bool): Indica si el vehículo está arrancado.

    Métodos:
        __init__(self, marca, modelo): Constructor de la clase.
        arrancar(self): Arranca el vehículo.
        parar(self): Para el vehículo.
        resumen(self): Imprime un resumen de la información del vehículo.
    """
    def __init__(self, marca, modelo, color="negro"):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.arrancado = False

    def arrancar(self):
        self.arrancado = True

    def parar(self):
        self.arrancado = False

    def resumen(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\nArrancado: {self.arrancado}")


class Moto(Vehiculo):
    """
    Clase hija que representa una moto, heredando de la clase Vehiculo.

    Atributos adicionales:
        is_carenado (bool): Indica si la moto tiene carenado.

    Métodos adicionales:
        poner_carenado(self): Añade carenado a la moto.
    """
    def __init__(self, marca, modelo, color="negro", is_carenado=False):
        super().__init__(marca, modelo, color)
        self.is_carenado = is_carenado

    def poner_carenado(self):
        self.is_carenado = True

    def resumen(self):
        super().resumen()
        print(f"Tiene carenado: {self.is_carenado}")


class Kwad(Moto):
    """
    Clase nieta que representa un kwad, heredando de la clase Moto.
    """
    pass


class Coche(Vehiculo):
    """
    Clase hija que representa un coche, heredando de la clase Vehiculo.

    Atributos adicionales:
        velocidad (int): Velocidad del coche en km/hr.

    Métodos adicionales:
        __init__(self, color, ruedas, velocidad): Constructor de la clase.
        __str__(self): Devuelve una representación en cadena del objeto.
    """
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f"{super().__str__()}, Velocidad: {self.velocidad} km/hr"


class Bicicleta(Vehiculo):
    """
    Clase hija que representa una bicicleta, heredando de la clase Vehiculo.

    Atributos adicionales:
        tipo (str): Tipo de bicicleta (urbana/montaña/etc).

    Métodos adicionales:
        __init__(self, color, ruedas, tipo): Constructor de la clase.
        __str__(self): Devuelve una representación en cadena del objeto.
    """
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.tipo}"

if __name__ == "__main__":
    # Ejemplo de uso
    mi_coche = Vehiculo("Renault", "Megane")
    mi_coche.arrancar()
    mi_coche.resumen()

    mi_moto = Moto("Kawasaki", "Ninja", "rojo")
    mi_moto.poner_carenado()
    mi_moto.resumen()

    mi_kwad = Kwad("Linhai", "LH 500", "azul")
    mi_kwad.resumen()

    # Ejemplo de uso
    mi_coche = Coche("rojo", 4, 120)
    print(mi_coche)

    mi_bicicleta = Bicicleta("azul", 2, "montaña")
    print(mi_bicicleta)