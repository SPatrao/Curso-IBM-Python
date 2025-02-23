# CLASES Y OBJETOS EN PYTHON

# Definición de clase básica
class Persona:
    """
    Esta clase representa a una persona con atributos como nombre y edad.
    También incluye métodos para interactuar con los datos de la persona.
    """
    
    # Atributo de clase (compartido por todas las instancias de la clase)
    especie = "Homo Sapiens"
    
    # Constructor (__init__)
    def __init__(self, nombre, edad):
        """
        Método especial que se ejecuta al crear una nueva instancia de la clase.
        :param nombre: Nombre de la persona (str)
        :param edad: Edad de la persona (int)
        """
        
        # Atributos de instancia (únicos para cada objeto)
        self.nombre = nombre  # Nombre de la persona
        self.edad = edad  # Edad de la persona
        
        # Atributo privado (convención: _documento indica que no debe accederse directamente)
        self._documento = None
    
    # Método de instancia (requiere un objeto para ser llamado)
    def presentarse(self):
        """
        Retorna una cadena con la presentación de la persona.
        :return: str
        """
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    
    # Método getter para obtener el documento privado
    @property
    def documento(self):
        """
        Método getter para acceder al documento privado.
        :return: str o None
        """
        return self._documento
    
    # Método setter para modificar el documento privado con validación
    @documento.setter
    def documento(self, valor):
        """
        Método setter para asignar un valor al documento privado.
        Solo acepta valores con exactamente 9 caracteres.
        :param valor: str
        """
        if len(str(valor)) == 9:
            self._documento = valor  # Asigna el valor si cumple la condición
        else:
            raise ValueError("Documento inválido")  # Lanza un error si el valor no es válido
    
    # Método de clase (opera sobre la clase en sí y no sobre instancias individuales)
    @classmethod
    def crear_anonimo(cls):
        """
        Método de clase que devuelve una instancia de Persona con nombre "Anónimo" y edad 0.
        :return: Persona
        """
        return cls("Anónimo", 0)  # Crea una persona con valores predeterminados
    
    # Método estático (no requiere acceso a la instancia ni a la clase)
    @staticmethod
    def es_mayor_edad(edad):
        """
        Método estático para verificar si una edad es de un adulto.
        :param edad: int
        :return: bool (True si es mayor de edad, False en caso contrario)
        """
        return edad >= 18  # Retorna True si la edad es 18 o más

# Crear instancias de la clase Persona
persona1 = Persona("Juan", 30)  # Se crea un objeto de la clase Persona con nombre "Juan" y edad 30
persona2 = Persona("María", 25)  # Se crea otro objeto con nombre "María" y edad 25

# Acceder a los atributos y métodos de instancia
print(persona1.nombre)  # Imprime el nombre de la persona1: "Juan"
print(persona1.presentarse())  # Llama al método presentarse(): "Hola, soy Juan y tengo 30 años"

# Uso del método de clase para crear una persona anónima
persona_anonima = Persona.crear_anonimo()
print(persona_anonima.presentarse())  # Imprime: "Hola, soy Anónimo y tengo 0 años"

# Uso del método estático
print(Persona.es_mayor_edad(20))  # True, porque 20 es mayor de edad
print(Persona.es_mayor_edad(15))  # False, porque 15 es menor de edad

# Acceder a un atributo de clase (compartido por todas las instancias)
print(persona1.especie)  # Imprime "Homo Sapiens"
print(persona2.especie)  # También imprime "Homo Sapiens"

# Modificar y acceder a un atributo privado a través del setter y getter
persona1.documento = "123456789"  # Asigna un documento válido (9 caracteres)
print(persona1.documento)  # Imprime el documento asignado: "123456789"

# Intentar asignar un documento inválido (menos de 9 caracteres) provocará un error
# persona1.documento = "12345"  # Esto generaría un ValueError: "Documento inválido"
