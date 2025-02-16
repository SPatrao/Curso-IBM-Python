# POLIMORFISMO EN PYTHON

# Clase base
class Figura:
    def area(self):
        pass
    
    def perimetro(self):
        pass

# Clases derivadas
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        import math
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        import math
        return 2 * math.pi * self.radio

# Función que demuestra polimorfismo
def imprimir_info_figura(figura):
    print(f"Área: {figura.area()}")
    print(f"Perímetro: {figura.perimetro()}")

# Crear instancias
rectangulo = Rectangulo(5, 3)
circulo = Circulo(4)

# Polimorfismo en acción
figuras = [rectangulo, circulo]

for figura in figuras:
    imprimir_info_figura(figura)

# Polimorfismo con duck typing
class Pato:
    def hablar(self):
        return "Cuack"

class Perro:
    def hablar(self):
        return "Guau"

def hacer_hablar(animal):
    print(animal.hablar())

# Usar duck typing
pato = Pato()
perro = Perro()

hacer_hablar(pato)   # "Cuack"
hacer_hablar(perro)  # "Guau"

# Método especial __str__
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}€"

producto = Producto("Laptop", 1000)
print(producto)  # Usa el método __str__

