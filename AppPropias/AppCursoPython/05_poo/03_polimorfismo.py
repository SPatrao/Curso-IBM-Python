# POLIMORFISMO EN PYTHON

# Importamos el módulo abc para definir clases abstractas y el módulo math para cálculos matemáticos
from abc import ABC, abstractmethod
import math

# Definición de una clase abstracta "Figura"
# Esta clase sirve como base para cualquier figura geométrica y contiene métodos abstractos.
class Figura(ABC):
    """
    Clase base abstracta que define la interfaz común para figuras geométricas.
    Contiene métodos abstractos que deben ser implementados por las subclases.
    """
    
    @abstractmethod
    def area(self):
        """Método abstracto para calcular el área de la figura."""
        pass

    @abstractmethod
    def perimetro(self):
        """Método abstracto para calcular el perímetro de la figura."""
        pass

# Clases derivadas que implementan la clase base "Figura"
class Rectangulo(Figura):
    """
    Clase que representa un rectángulo.
    Hereda de Figura e implementa los métodos de cálculo de área y perímetro.
    """
    
    def __init__(self, ancho, alto):
        """
        Constructor de la clase Rectangulo.
        :param ancho: Ancho del rectángulo.
        :param alto: Alto del rectángulo.
        """
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        """Calcula el área del rectángulo (base * altura)."""
        return self.ancho * self.alto
    
    def perimetro(self):
        """Calcula el perímetro del rectángulo (2 * (base + altura))."""
        return 2 * (self.ancho + self.alto)

class Circulo(Figura):
    """
    Clase que representa un círculo.
    Hereda de Figura e implementa los métodos de cálculo de área y perímetro.
    """
    
    def __init__(self, radio):
        """
        Constructor de la clase Circulo.
        :param radio: Radio del círculo.
        """
        self.radio = radio
    
    def area(self):
        """Calcula el área del círculo (π * radio^2)."""
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        """Calcula el perímetro del círculo (2 * π * radio)."""
        return 2 * math.pi * self.radio

# Función polimórfica
# Recibe un objeto que implemente los métodos `area` y `perimetro`
def imprimir_info_figura(figura):
    """
    Función que imprime el área y el perímetro de cualquier figura geométrica.
    :param figura: Objeto que debe implementar los métodos area() y perimetro().
    """
    print(f"Área: {figura.area()}")
    print(f"Perímetro: {figura.perimetro()}")

# Creación de instancias de las figuras
figuras = [Rectangulo(5, 3), Circulo(4)]

# Demostración del polimorfismo con la función imprimir_info_figura
for figura in figuras:
    imprimir_info_figura(figura)

# POLIMORFISMO CON DUCK TYPING
# En Python, no se necesita una jerarquía de clases para aplicar polimorfismo.
# Basta con que los objetos tengan los métodos esperados.
class Pato:
    """
    Clase que representa un pato con un método hablar().
    """
    def hablar(self):
        return "Cuack"

class Perro:
    """
    Clase que representa un perro con un método hablar().
    """
    def hablar(self):
        return "Guau"

# Función que utiliza duck typing
def hacer_hablar(animal):
    """
    Función polimórfica que llama al método hablar() de cualquier objeto.
    :param animal: Objeto que debe tener un método hablar().
    """
    print(animal.hablar())

# Creación de instancias de clases no relacionadas pero con el mismo método
hacer_hablar(Pato())   # "Cuack"
hacer_hablar(Perro())  # "Guau"

# POLIMORFISMO CON MÉTODOS ESPECIALES (__str__)
# Se puede aplicar polimorfismo sobrescribiendo métodos especiales de Python.
class Producto:
    """
    Clase que representa un producto con nombre y precio.
    Sobrescribe el método especial __str__ para personalizar su representación en texto.
    """
    
    def __init__(self, nombre, precio):
        """
        Constructor de la clase Producto.
        :param nombre: Nombre del producto.
        :param precio: Precio del producto.
        """
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        """
        Método especial que devuelve una representación en texto del objeto Producto.
        """
        return f"Producto: {self.nombre}, Precio: {self.precio}€"

# Creación de una instancia de Producto y demostración de __str__
print(Producto("Laptop", 1000))  # "Producto: Laptop, Precio: 1000€"
