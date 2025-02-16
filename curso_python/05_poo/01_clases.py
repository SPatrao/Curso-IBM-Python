# CLASES Y OBJETOS EN PYTHON

# Definición de clase básica
class Persona:
    # Atributo de clase
    especie = "Homo Sapiens"
    
    # Constructor
    def __init__(self, nombre, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
        # Atributo privado
        self._documento = None
    
    # Método de instancia
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    
    # Método getter
    @property
    def documento(self):
        return self._documento
    
    # Método setter
    @documento.setter
    def documento(self, valor):
        if len(str(valor)) == 9:
            self._documento = valor
        else:
            raise ValueError("Documento inválido")
    
    # Método de clase
    @classmethod
    def crear_anonimo(cls):
        return cls("Anónimo", 0)
    
    # Método estático
    @staticmethod
    def es_mayor_edad(edad):
        return edad >= 18

# Crear instancias
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Acceder a atributos y métodos
print(persona1.nombre)
print(persona1.presentarse())

# Usar método de clase
persona_anonima = Persona.crear_anonimo()

# Usar método estático
print(Persona.es_mayor_edad(20))  # True

# Herencia de atributos de clase
print(persona1.especie)  # "Homo Sapiens"

# Manejo de atributos privados
persona1.documento = "123456789"
print(persona1.documento)

