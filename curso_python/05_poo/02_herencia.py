# HERENCIA EN PYTHON

# Clase base (superclase)
class Vehiculo:
    """
    Clase base que representa un vehículo genérico.
    """
    def __init__(self, marca, modelo):
        """
        Constructor de la clase Vehiculo.
        :param marca: Marca del vehículo.
        :param modelo: Modelo del vehículo.
        """
        self.marca = marca
        self.modelo = modelo
    
    def descripcion(self):
        """
        Devuelve una descripción del vehículo.
        """
        return f"{self.marca} {self.modelo}"
    
    def arrancar(self):
        """
        Simula el arranque del vehículo.
        """
        return "El vehículo está arrancando"

# Clase derivada (subclase) que hereda de Vehiculo
class Coche(Vehiculo):
    """
    Clase Coche que hereda de Vehiculo e incorpora nuevas funcionalidades.
    """
    def __init__(self, marca, modelo, num_puertas):
        """
        Constructor de la clase Coche.
        :param marca: Marca del coche.
        :param modelo: Modelo del coche.
        :param num_puertas: Número de puertas del coche.
        """
        super().__init__(marca, modelo)  # Llamamos al constructor de la clase padre
        self.num_puertas = num_puertas
    
    def descripcion(self):
        """
        Sobrescribe el método descripcion de la clase padre para incluir el número de puertas.
        """
        return f"{super().descripcion()} - {self.num_puertas} puertas"
    
    def acelerar(self):
        """
        Simula la aceleración del coche.
        """
        return "El coche está acelerando"

# Clase Electrico para herencia múltiple
class Electrico:
    """
    Clase que representa vehículos eléctricos.
    """
    def __init__(self, bateria):
        """
        Constructor de la clase Electrico.
        :param bateria: Nivel de batería en porcentaje.
        """
        self.bateria = bateria
    
    def cargar(self):
        """
        Simula la carga de la batería del vehículo eléctrico.
        """
        return "Cargando batería"

# Clase CocheElectrico que hereda de Coche y Electrico (herencia múltiple)
class CocheElectrico(Coche, Electrico):
    """
    Clase que combina las funcionalidades de un coche y un vehículo eléctrico.
    """
    def __init__(self, marca, modelo, num_puertas, bateria):
        """
        Constructor de la clase CocheElectrico.
        :param marca: Marca del coche eléctrico.
        :param modelo: Modelo del coche eléctrico.
        :param num_puertas: Número de puertas del coche eléctrico.
        :param bateria: Nivel de batería en porcentaje.
        """
        Coche.__init__(self, marca, modelo, num_puertas)  # Inicializamos la parte de coche
        Electrico.__init__(self, bateria)  # Inicializamos la parte eléctrica
    
    def estado(self):
        """
        Devuelve una descripción completa del coche eléctrico incluyendo la batería.
        """
        return f"{self.descripcion()} - Batería: {self.bateria}%"

# Crear instancias de las clases
vehiculo = Vehiculo("Genérico", "Modelo Base")
coche = Coche("Toyota", "Corolla", 4)
coche_electrico = CocheElectrico("Tesla", "Model 3", 4, 85)

# Usar métodos de las clases y mostrar resultados
print(vehiculo.descripcion())  # "Genérico Modelo Base"
print(coche.descripcion())  # "Toyota Corolla - 4 puertas"
print(coche.arrancar())  # "El vehículo está arrancando"
print(coche.acelerar())  # "El coche está acelerando"
print(coche_electrico.estado())  # "Tesla Model 3 - 4 puertas - Batería: 85%"
print(coche_electrico.cargar())  # "Cargando batería"

# Verificar relaciones de herencia con isinstance e issubclass
print(isinstance(coche_electrico, Coche))  # True, porque CocheElectrico hereda de Coche
print(isinstance(coche_electrico, Vehiculo))  # True, porque CocheElectrico también hereda de Vehiculo
print(issubclass(CocheElectrico, Coche))  # True, porque es una subclase de Coche
