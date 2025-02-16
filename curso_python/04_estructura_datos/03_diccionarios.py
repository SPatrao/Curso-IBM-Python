# DICCIONARIOS EN PYTHON

# Creación de diccionarios
# Los diccionarios en Python son colecciones de pares clave-valor. 
# Un diccionario vacío se crea con llaves vacías {}
diccionario_vacio = {}

# Un diccionario con algunos valores iniciales
persona = {
    "nombre": "Juan",  # Clave: "nombre", Valor: "Juan"
    "edad": 30,        # Clave: "edad", Valor: 30
    "ciudad": "Madrid" # Clave: "ciudad", Valor: "Madrid"
}

# Acceso a elementos
# Se puede acceder a los valores del diccionario usando las claves.
print(persona["nombre"])  # Acceso directo por clave: Imprime "Juan"
# El método get() también se puede usar, y es más seguro ya que no lanza un error si la clave no existe.
print(persona.get("edad"))  # Usamos el método get(), Imprime 30

# Modificación de diccionarios
# Se pueden agregar o modificar elementos directamente usando las claves.
persona["profesion"] = "Ingeniero"  # Añadir un nuevo par clave-valor
persona["edad"] = 31  # Modificar un valor existente, cambia "edad" de 30 a 31

# Eliminar elementos
# Para eliminar un par clave-valor, se puede usar 'del' o el método pop().
del persona["ciudad"]  # Elimina el par clave-valor con la clave "ciudad"
persona.pop("profesion")  # Elimina "profesion" y devuelve su valor ("Ingeniero")

# Métodos de diccionarios
# Con estos métodos podemos obtener información útil sobre el diccionario.
print(persona.keys())    # Devuelve todas las claves del diccionario: dict_keys(['nombre', 'edad'])
print(persona.values())  # Devuelve todos los valores del diccionario: dict_values(['Juan', 31])
print(persona.items())   # Devuelve todos los pares clave-valor: dict_items([('nombre', 'Juan'), ('edad', 31)])

# Diccionarios anidados
# Los diccionarios pueden contener otros diccionarios, creando estructuras más complejas.
estudiantes = {
    "Juan": {"edad": 25, "nota": 8.5},  # Diccionario dentro de otro diccionario
    "María": {"edad": 22, "nota": 9.0}  # Cada estudiante tiene su propio diccionario con edad y nota
}

# Podemos acceder a un valor en un diccionario anidado de esta forma:
print(estudiantes["Juan"]["edad"])  # Imprime 25, accede a la edad de Juan dentro del diccionario de Juan

# Comprensión de diccionarios
# Con la comprensión de diccionarios, podemos crear diccionarios de manera más compacta y eficiente.
# En este caso, estamos creando un diccionario con los cuadrados de los números del 0 al 5.
cuadrados = {x: x**2 for x in range(6)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Fusionar diccionarios (solo en Python 3.9+)
# En Python 3.9 y versiones posteriores, se puede fusionar diccionarios utilizando el operador '|'.
dict1 = {"a": 1, "b": 2}  # Diccionario 1
dict2 = {"c": 3, "d": 4}  # Diccionario 2
# Fusionamos ambos diccionarios en uno solo
dict_combinado = dict1 | dict2  # El resultado es {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Copiar diccionarios
# Si necesitamos una copia de un diccionario, podemos usar el método copy().
copia_dict = persona.copy()  # Copia el diccionario persona en copia_dict

# Crear diccionario desde claves y valores
# Si tienes una lista de claves y una lista de valores, puedes crear un diccionario combinando ambas listas.
claves = ["nombre", "edad", "ciudad"]  # Lista de claves
valores = ["Ana", 25, "Barcelona"]     # Lista de valores
# Utilizamos el método zip() para juntar las claves y los valores y luego creamos el diccionario con dict()
nuevo_dict = dict(zip(claves, valores))  # Resultado: {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Barcelona'}

# Valor por defecto
# Con defaultdict de la librería collections, podemos evitar que un KeyError se lance si no encontramos una clave.
from collections import defaultdict

# Creamos un diccionario que tendrá un valor por defecto si la clave no existe.
dict_defecto = defaultdict(int)  # El valor por defecto será 0 (int())
dict_defecto["a"] += 1  # Asigna el valor 1 a la clave "a", sin lanzar error, incluso si "a" no existía antes.
print(dict_defecto)  # Imprime defaultdict(<class 'int'>, {'a': 1})
