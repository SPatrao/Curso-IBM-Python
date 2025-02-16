# HERENCIA EN PYTHON

# Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def descripcion(self):
        return f"{self.marca} {self.modelo}"
    
    def arrancar(self):
        return "El vehículo está arrancando"

# Clase derivada
class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        # Llamar al constructor de la clase padre
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
    
    # Sobrescritura de método
    def descripcion(self):
        return f"{super().descripcion()} - {self.num_puertas} puertas"
    
    # Método específico de la clase hija
    def acelerar(self):
        return "El coche está acelerando"

# Herencia múltiple
class Electrico:
    def __init__(self, bateria):
        self.bateria = bateria
    
    def cargar(self):
        return "Cargando batería"

class CocheElectrico(Coche, Electrico):
    def __init__(self, marca, modelo, num_puertas, bateria):
        Coche.__init__(self, marca, modelo, num_puertas)
        Electrico.__init__(self, bateria)
    
    # Método que combina funcionalidades
    def estado(self):
        return f"{self.descripcion()} - Batería: {self.bateria}%"

# Crear instancias
vehiculo = Vehiculo("Genérico", "Modelo Base")
coche = Coche("Toyota", "Corolla", 4)
coche_electrico = CocheElectrico("Tesla", "Model 3", 4, 85)

# Usar métodos
print(vehiculo.descripcion())
print(coche.descripcion())
print(coche.arrancar())
print(coche.acelerar())
print(coche_electrico.estado())
print(coche_electrico.cargar())

# Verificar herencia
print(isinstance(coche_electrico, Coche))  # True
print(isinstance(coche_electrico, Vehiculo))  # True
print(issubclass(CocheElectrico, Coche))  # True

