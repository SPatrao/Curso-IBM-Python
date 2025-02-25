# TIPOS DE DATOS EN PYTHON

# 1. Números enteros
# Los números enteros (int) son números sin decimales.
x = 10  # Un número entero positivo
y = -5  # Un número entero negativo
z = 0   # El número entero cero

# 2. Números de punto flotante
# Los números de punto flotante (float) son números con decimales.
a = 3.14  # Un número de punto flotante positivo
b = -2.5  # Un número de punto flotante negativo
c = 2.0   # Un número de punto flotante positivo (con la notación decimal explícita)

# 3. Números complejos
# Los números complejos tienen una parte real y una parte imaginaria.
# Se representan con 'j' para la parte imaginaria.
numero_complejo = 3 + 5j  # El número complejo tiene una parte real 3 y una parte imaginaria 5j.

# 4. Cadenas de texto
# Las cadenas (str) son secuencias de caracteres, y se pueden escribir entre comillas dobles o simples.
texto1 = "Hola, mundo"  # Una cadena de texto con comillas dobles
texto2 = 'Python es genial'  # Una cadena de texto con comillas simples
# También puedes usar comillas triples para cadenas de texto que ocupan varias líneas:
texto_multilinea = """
Esto es un texto
que ocupa
varias líneas
"""  # Una cadena de texto de varias líneas

# 5. Listas
# Las listas (list) son colecciones ordenadas de elementos, y pueden contener diferentes tipos de datos.
# Se crean usando corchetes [].
lista_numeros = [1, 2, 3, 4, 5]  # Una lista de números enteros
lista_mixta = [1, "texto", 3.14, True]  # Una lista con elementos de diferentes tipos (números, cadena y booleano)

# 6. Tuplas (inmutables)
# Las tuplas (tuple) son similares a las listas, pero son inmutables, es decir, no se pueden modificar después de crearlas.
# Se crean usando paréntesis ().
tupla_numeros = (1, 2, 3, 4, 5)  # Una tupla de números enteros
tupla_mixta = (1, "texto", 3.14)  # Una tupla con elementos de diferentes tipos

# 7. Diccionarios
# Los diccionarios (dict) son colecciones de pares clave-valor. Se crean usando llaves {}.
persona = {
    "nombre": "Juan",   # Clave 'nombre' con valor 'Juan'
    "edad": 30,         # Clave 'edad' con valor 30
    "ciudad": "Madrid"  # Clave 'ciudad' con valor 'Madrid'
}

# 8. Conjuntos (sets)
# Los conjuntos (set) son colecciones de elementos únicos y no ordenados.
# Se crean usando llaves {} o la función set().
conjunto1 = {1, 2, 3, 4, 5}  # Un conjunto de números
conjunto2 = set([4, 5, 6, 7, 8])  # Un conjunto creado a partir de una lista

# 9. Booleanos
# Los valores booleanos (bool) representan dos estados posibles: True (verdadero) o False (falso).
verdadero = True  # Un valor booleano verdadero
falso = False     # Un valor booleano falso

# 10. None (valor nulo)
# None es un valor especial que representa la ausencia de un valor.
valor_nulo = None  # Representa un valor nulo o vacío

# 11. Conversión entre tipos
# Python permite convertir entre diferentes tipos de datos.

# Convertir un número entero a un número de punto flotante
entero = 10
flotante = float(entero)  # Convierte el entero 10 a flotante (10.0)
print(f"Entero a flotante: {flotante}")  # Imprime: 10.0

# Convertir un número de punto flotante a un número entero
flotante = 3.14
entero = int(flotante)  # Convierte el flotante 3.14 a entero (3)
print(f"Flotante a entero: {entero}")  # Imprime: 3

# Convertir una lista a una tupla
lista = [1, 2, 3]
tupla = tuple(lista)  # Convierte la lista [1, 2, 3] a una tupla (1, 2, 3)
print(f"Lista a tupla: {tupla}")  # Imprime: (1, 2, 3)

# Convertir una tupla a una lista
tupla = (1, 2, 3)
lista = list(tupla)  # Convierte la tupla (1, 2, 3) a una lista [1, 2, 3]
print(f"Tupla a lista: {lista}")  # Imprime: [1, 2, 3]

# 12. Funciones útiles

# Verificar el tipo de una variable
print(type(x))  # Muestra el tipo de la variable 'x'. En este caso, 'x' es un número entero (int).
# Resultado esperado: <class 'int'>

# Verificar si una variable es de un tipo específico
print(isinstance(x, int))  # Verifica si 'x' es una instancia de la clase 'int' (número entero).
# Resultado esperado: True, porque 'x' es un número entero.

