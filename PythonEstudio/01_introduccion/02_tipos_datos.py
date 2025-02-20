# TIPOS DE DATOS EN PYTHON
# ======================================
# Objetivo: Proporcionar una guía completa sobre los tipos de datos en Python.
# Este archivo cubre los tipos básicos de datos, sus conversiones y algunas funciones útiles.

# 1. Números enteros (int)
# Los números enteros son valores sin decimales, pueden ser positivos, negativos o cero.
x = 10  # Un número entero positivo
y = -5  # Un número entero negativo
z = 0   # El número entero cero

print(f"Ejemplo de números enteros: x = {x}, y = {y}, z = {z}")

# 2. Números de punto flotante (float)
# Los números de punto flotante son valores que contienen decimales.
a = 3.14  # Un número de punto flotante positivo
b = -2.5  # Un número de punto flotante negativo
c = 2.0   # Un número de punto flotante positivo (con la notación decimal explícita)

print(f"Ejemplo de números flotantes: a = {a}, b = {b}, c = {c}")

# 3. Números complejos
# Los números complejos tienen una parte real y una parte imaginaria.
numero_complejo = 3 + 5j  # Parte real: 3, Parte imaginaria: 5j
print(f"Número complejo: {numero_complejo}")  # Imprime el número complejo

# 4. Cadenas de texto (str)
# Las cadenas son secuencias de caracteres, se pueden definir con comillas dobles o simples.
texto1 = "Hola, mundo"  # Cadena con comillas dobles
texto2 = 'Python es genial'  # Cadena con comillas simples
# También se pueden crear cadenas multilineales usando comillas triples.
texto_multilinea = """Esto es un texto
que ocupa
varias líneas"""  # Cadena de texto de varias líneas

print(f"Ejemplo de cadenas:\n{texto1}\n{texto2}\n{texto_multilinea}")

# 5. Listas (list)
# Las listas son colecciones ordenadas de elementos que pueden ser de diferentes tipos.
lista_numeros = [1, 2, 3, 4, 5]  # Lista de números enteros
lista_mixta = [1, "texto", 3.14, True]  # Lista con elementos de diferentes tipos

print(f"Ejemplos de listas:\nNúmeros: {lista_numeros}\nMixta: {lista_mixta}")

# 6. Tuplas (tuple)
# Las tuplas son similares a las listas, pero son inmutables (no se pueden modificar una vez creadas).
tupla_numeros = (1, 2, 3, 4, 5)  # Tupla de números enteros
tupla_mixta = (1, "texto", 3.14)  # Tupla con elementos de diferentes tipos

print(f"Ejemplos de tuplas:\nNúmeros: {tupla_numeros}\nMixta: {tupla_mixta}")

# 7. Diccionarios (dict)
# Los diccionarios son colecciones de pares clave-valor, creados utilizando llaves {}.
persona = {
    "nombre": "Juan",   # Clave: 'nombre', Valor: 'Juan'
    "edad": 30,         # Clave: 'edad', Valor: 30
    "ciudad": "Madrid"  # Clave: 'ciudad', Valor: 'Madrid'
}

print(f"Diccionario de persona: {persona}")

# 8. Conjuntos (set)
# Los conjuntos son colecciones de elementos únicos y no ordenados.
conjunto1 = {1, 2, 3, 4, 5}  # Un conjunto de números
conjunto2 = set([4, 5, 6, 7, 8])  # Un conjunto creado a partir de una lista

print(f"Ejemplos de conjuntos:\nConjunto 1: {conjunto1}\nConjunto 2: {conjunto2}")

# 9. Booleanos (bool)
# Los valores booleanos representan dos estados posibles: True (verdadero) o False (falso).
verdadero = True  # Un valor booleano verdadero
falso = False     # Un valor booleano falso

print(f"Ejemplos de booleanos:\nVerdadero: {verdadero}\nFalso: {falso}")

# 10. None (valor nulo)
# None es un valor especial que representa la ausencia de un valor.
valor_nulo = None  # Representa un valor nulo o vacío
print(f"Valor nulo: {valor_nulo}")

# 11. Conversión entre tipos
# Python permite convertir entre diferentes tipos de datos utilizando funciones de conversión.

# Convertir un número entero a un número de punto flotante.
entero = 10
flotante = float(entero)  # Convierte el entero 10 a flotante (10.0)
print(f"Entero a flotante: {flotante}")  # Imprime: 10.0

# Convertir un número de punto flotante a un número entero.
flotante = 3.14
entero = int(flotante)  # Convierte el flotante 3.14 a entero (3)
print(f"Flotante a entero: {entero}")  # Imprime: 3

# Convertir una lista a una tupla.
lista = [1, 2, 3]
tupla = tuple(lista)  # Convierte la lista [1, 2, 3] a una tupla (1, 2, 3)
print(f"Lista a tupla: {tupla}")  # Imprime: (1, 2, 3)

# Convertir una tupla a una lista.
tupla = (1, 2, 3)
lista = list(tupla)  # Convierte la tupla (1, 2, 3) a una lista [1, 2, 3]
print(f"Tupla a lista: {lista}")  # Imprime: [1, 2, 3]

# 12. Funciones útiles
# -------------------------------------------
# Verificar el tipo de una variable
print(f"Tipo de 'x': {type(x)}")  # Muestra el tipo de la variable 'x', que es int.
# Resultado esperado: <class 'int'>

# Verificar si una variable es de un tipo específico
print(f"¿'x' es un entero? {isinstance(x, int)}")  # Verifica si 'x' es una instancia de 'int'.
# Resultado esperado: True, porque 'x' es un número entero.

# EJERCICIOS FINALES
# ======================================
print("\n🔹 Ejercicios Finales:")

# Ejercicio 1: Implementar un programa que pida al usuario que ingrese su edad y determine si es mayor o menor de edad.
edad_usuario = int(input("Ingresa tu edad: "))
if edad_usuario >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Ejercicio 2: Solicitamos al usuario que ingrese un número y comprobamos si es positivo, negativo o cero.
numero_usuario = float(input("Ingresa un número: "))
if numero_usuario > 0:
    print("El número es positivo.")
elif numero_usuario < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# GLOSARIO
# ======================================
print("""
📖 Glosario:
- Tipo de dato: Especifica el tipo de valor que puede almacenar una variable (int, float, str, etc.).
- Conversión: Proceso de cambiar un tipo de dato a otro.
- Función: Bloque de código que realiza una tarea específica.
- Inmutable: Un objeto cuyo contenido no puede cambiar después de haber sido creado (como las tuplas).
""")

