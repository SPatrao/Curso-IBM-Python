# GUÍA DE ESTUDIO DE PYTHON: CONCEPTOS BÁSICOS Y SINTAXISang

# 1. Introducción:
# Python es un lenguaje de programación multiparadigma, interpretado, y de tipado dinámico.
# Su sintaxis es clara y legible, lo que facilita el aprendizaje y desarrollo.

# 2. Tipos de Datos Básicos (Built-ins)
# Los tipos de datos son fundamentales en cualquier lenguaje de programación.
# Python ofrece varios tipos básicos:

#  a. Números:
#    - Enteros (int): Números sin decimales.
edad = 30  # Ejemplo de un entero
#    - Flotantes (float): Números con decimales.
pi = 3.14159  # Ejemplo de un flotante
#    - Complejos (complex): Números con parte real e imaginaria.
complejo = 2 + 3j  # Ejemplo de un número complejo

#  b. Cadenas (Strings):
#    - Secuencias de caracteres. Se definen con comillas simples o dobles.
nombre = "Juan Pérez"  # Ejemplo de una cadena
saludo = 'Hola, Mundo!'  # Otro ejemplo de cadena
#   - Operaciones comunes: concatenación, slicing, etc.
nombre_completo = nombre + " " + saludo  # Concatenación
primer_nombre = nombre[0:4]  # Slicing (extrae "Juan")

#  c. Booleanos:
#    - Representan valores de verdad: True o False.
es_mayor_de_edad = edad >= 18  # Ejemplo de booleano
#    - Útiles para control de flujo (condicionales y bucles).

#  d. Listas:
#    - Colecciones ordenadas y mutables de elementos.
frutas = ["manzana", "banana", "cereza"]
#   - Operaciones: añadir, eliminar, modificar elementos, etc.
frutas.append("naranja")  # Añade "naranja" al final
frutas[1] = "plátano"  # Modifica el segundo elemento
#   - Acceso por índice
print(frutas[0]) #imprimirá "manzana"
print(frutas[-1])#imprimirá "naranja"

#  e. Tuplas:
#    - Colecciones ordenadas e inmutables de elementos.
coordenadas = (4.5, 7.2)
#   - Útiles para representar datos que no deben cambiar.

#  f. Diccionarios:
#    - Colecciones de pares clave-valor.
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
#   - Acceso por clave:
print(persona["nombre"]) #imprimirá Ana

#  g. Sets (Conjuntos):
#    - Colecciones no ordenadas de elementos únicos.
numeros = {1, 2, 3, 4, 5}
#   - Útiles para eliminar duplicados y realizar operaciones de conjuntos (unión, intersección, etc.).

# 3. Sintaxis Básica

#  a. Variables:
#    - Nombres que referencian objetos en memoria.
#    - No es necesario declarar el tipo de dato.
nombre = "Carlos"
edad = 28

#  b. Comentarios:
#    - Líneas que no son ejecutadas por el intérprete.
#    - Se utilizan para documentar el código.
# Este es un comentario de una sola línea.
"""
Este es un comentario
de varias líneas.
"""

#  c. Operadores:
#    - Aritméticos: +, -, *, /, // (división entera), % (módulo), ** (potencia).
x = 10 + 5
y = 20 // 3  # División entera (resultado: 6)
#    - Comparación: ==, !=, >, <, >=, <=.
es_igual = (x == y)
#    - Lógicos: and, or, not.
es_verdadero = (es_mayor_de_edad and es_igual)

#  d. Entrada y Salida:
#    - `input()`: Lee datos desde la entrada estándar (teclado).
nombre = input("Ingrese su nombre: ")  # Descomentar para probar
#    - `print()`: Muestra datos en la salida estándar (consola).
print("Hola,", nombre)  # Descomentar para probar

#  e. Identación:
#    - Python utiliza la indentación para definir bloques de código.
#    - Es fundamental para la estructura del programa.
#    - Se recomienda usar 4 espacios por nivel de indentación.

# 4. Control de Flujo

#  a. Condicionales (if, elif, else):
edad = 15
if edad >= 18:
    print("Es mayor de edad.")
elif edad >= 16:
    print("Puede obtener un permiso.")
else:
    print("Es menor de edad.")

#  b. Bucles:
#    - `for`: Itera sobre una secuencia (lista, tupla, cadena, etc.).
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
#    - `while`: Ejecuta un bloque de código mientras una condición sea verdadera.
contador = 0
while contador < 5:
    print(contador)
    contador += 1

#  c. Sentencias de control de bucles:
#    - `break`: Termina la ejecución del bucle.
for numero in range(10):
    if numero == 5:
        break  # Sale del bucle cuando numero es 5
    print(numero)
#    - `continue`: Salta a la siguiente iteración del bucle.
for numero in range(10):
    if numero % 2 == 0:
        continue  # Salta los números pares
    print(numero)

# 5. Funciones
#  a. Definición:
#    - Bloques de código reutilizables que realizan una tarea específica.
#    - Se definen con la palabra clave `def`.
def saludar(nombre):
    """Esta función saluda a la persona que recibe como parámetro.""" # Docstring
    print("Hola,", nombre)

#  b. Llamada:
#    - Para ejecutar una función, se debe llamar por su nombre.
saludar("María")

#  c. Parámetros y argumentos:
#    - Parámetros: Variables que se definen en la definición de la función.
#    - Argumentos: Valores que se pasan a la función cuando se llama.
def sumar(a, b): # a y b son parámetros
    return a + b

resultado = sumar(5, 3)  # 5 y 3 son argumentos

#  d. Valor de retorno:
#    - Las funciones pueden devolver un valor con la palabra clave `return`.
#    - Si no se especifica un valor de retorno, la función devuelve `None`.

#  e. Ámbito de las variables (LEGB):
#    - Local: Definidas dentro de la función.
#    - Enclosing: Definidas en una función que contiene a otra.
#    - Global: Definidas fuera de cualquier función.
#    - Built-in: Nombres predefinidos en Python.

# 6. Excepciones
#  a. Manejo de excepciones:
#    - Se utiliza el bloque `try...except` para capturar y manejar errores.
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero.")


#  c. La sentencia `assert`:
#    - Se utiliza para verificar una condición y lanzar una excepción si es falsa.
temperatura = 30
assert temperatura < 40, "La temperatura es demasiado alta."

# 7. Iteradores
#  a. Iterables e iteradores:
#    - Un iterable es un objeto que puede ser recorrido (listas, tuplas, cadenas, etc.).
#    - Un iterador es un objeto que produce valores uno a la vez.
#  b. Protocolo de iteración:
#    - Se utilizan las funciones `iter()` para obtener un iterador y `next()` para obtener el siguiente valor.
frutas = ["manzana", "banana", "cereza"]
iterador = iter(frutas)
print(next(iterador))
print(next(iterador))
print(next(iterador))
try:
    print(next(iterador)) #provocará un error
except StopIteration:
    print("No hay más frutas.")

print("¡Fin de la guía!")

#  b. Lanzamiento de excepciones:
#    - Se utiliza la palabra clave `raise` para lanzar una excepción.
edad = -5
if edad < 0:
    raise ValueError("La edad no puede ser negativa.")





