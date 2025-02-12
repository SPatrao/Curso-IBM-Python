# -*- coding: utf-8 -*-
"""
Guía de Estudio de Python: Conceptos Básicos y Sintaxis

Este código proporciona ejemplos comentados de los conceptos clave
abordados en las guías de estudio, sirviendo como referencia
y herramienta de aprendizaje.
"""

# ---------------------------------------------------------------------
# 1. Tipos de datos básicos y su sintaxis
# ---------------------------------------------------------------------

print("\n--- 1. Tipos de datos básicos ---")

# Números (enteros, flotantes)
entero = 10
flotante = 3.14
print(f"Entero: {entero}, tipo: {type(entero)}")  # Imprime el valor y el tipo
print(f"Flotante: {flotante}, tipo: {type(flotante)}")

# Strings (cadenas de texto)
cadena = "Hola, mundo!"
print(f"Cadena: {cadena}, tipo: {type(cadena)}")

# Booleanos (True o False)
booleano = True
print(f"Booleano: {booleano}, tipo: {type(booleano)}")

#Casting (convertir entre tipos de datos)
cadena_numero = "42"
entero_convertido = int(cadena_numero)
print(f"Cadena original: {cadena_numero}, tipo: {type(cadena_numero)}")
print(f"Entero convertido: {entero_convertido}, tipo: {type(entero_convertido)}")

# ---------------------------------------------------------------------
# 2. Entrada y salida de datos
# ---------------------------------------------------------------------

print("\n--- 2. Entrada y salida de datos ---")

# Entrada de datos desde el usuario (siempre devuelve un string)
nombre = input("Por favor, introduce tu nombre: ")
print(f"Hola, {nombre}!")  # Salida formateada

# ---------------------------------------------------------------------
# 3. Operadores
# ---------------------------------------------------------------------


print("\n--- 3. Operadores ---")


a = 15
b = 7

# Operadores aritméticos
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b  # División siempre devuelve un flotante
division_entera = a // b  # División entera (trunca el resultado)
modulo = a % b  # Resto de la división
potencia = a ** b  # Exponenciación

print(f"Suma: {suma}, Resta: {resta}")
print(f"Multiplicación: {multiplicacion}, División: {division}")
print(f"División entera: {division_entera}, Módulo: {modulo}, Potencia: {potencia}")

# Operadores de comparación (devuelven booleanos)
es_igual = (a == b)
es_diferente = (a != b)
es_mayor = (a > b)
es_menor = (a < b)
es_mayor_o_igual = (a >= b)
es_menor_o_igual = (a <= b)

print(f"Es igual: {es_igual}, Es diferente: {es_diferente}")
print(f"Es mayor: {es_mayor}, Es menor: {es_menor}")
print(f"Es mayor o igual: {es_mayor_o_igual}, Es menor o igual: {es_menor_o_igual}")

# Operadores lógicos (and, or, not)
condicion1 = True
condicion2 = False

y_logico = condicion1 and condicion2  # Devuelve True solo si ambas son True
o_logico = condicion1 or condicion2   # Devuelve True si al menos una es True
no_logico = not condicion1           # Invierte el valor booleano

print(f"AND: {y_logico}, OR: {o_logico}, NOT: {no_logico}")

# ---------------------------------------------------------------------
# 4. Estructuras de control
# ---------------------------------------------------------------------

print("\n--- 4. Estructuras de control ---")

# Condicionales (if, elif, else)
edad = int(input("Introduce tu edad: "))

if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad < 65:
    print("Eres adulto.")
else:
    print("Eres un adulto mayor.")

# Operador ternario (forma concisa de un if-else)
estado = "aprobado" if edad >= 18 else "rechazado"
print(f"Estado: {estado}")

# Bucles (for)
print("\nBucle for:")
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:  # Itera sobre cada elemento de la lista
    print(fruta)

print("\nBucle for con range():")
for i in range(5):  # Itera 5 veces (de 0 a 4)
    print(i)

# Bucle (while)
print("\nBucle while:")
contador = 0
while contador < 3:  # Mientras la condición sea True
    print(contador)
    contador += 1

# Sentencias break, continue, pass
print("\nSentencias break, continue, pass:")
for numero in range(10):
    if numero == 3:
        continue  # Salta esta iteración
    if numero == 7:
        break  # Sale del bucle
    if numero % 2 == 0:
        pass  # No hace nada
    print(numero)

# ---------------------------------------------------------------------
# 5. Colecciones
# ---------------------------------------------------------------------

print("\n--- 5. Colecciones ---")

# Listas (mutables, ordenadas)
mi_lista = [1, "dos", True]
print(f"Lista original: {mi_lista}, tipo: {type(mi_lista)}")
mi_lista.append("nuevo elemento")  # Añade al final
mi_lista[0] = 42  # Modifica un elemento
print(f"Lista modificada: {mi_lista}")

# Tuplas (inmutables, ordenadas)
mi_tupla = (1, "dos", True)
print(f"Tupla: {mi_tupla}, tipo: {type(mi_tupla)}")
# mi_tupla[0] = 42  # Esto daría un error (inmutable)

# Diccionarios (mutables, pares clave-valor)
mi_diccionario = {"clave1": "valor1", "clave2": 2}
print(f"Diccionario: {mi_diccionario}, tipo: {type(mi_diccionario)}")
print(f"Valor de clave1: {mi_diccionario['clave1']}")
mi_diccionario["clave3"] = "nuevo valor"  # Añade un par clave-valor
print(f"Diccionario modificado: {mi_diccionario}")

# Sets (mutables, no ordenados, sin duplicados)
mi_set = {1, 2, 2, 3}  # El duplicado se elimina
print(f"Set: {mi_set}, tipo: {type(mi_set)}")
mi_set.add(4)
print(f"Set modificado: {mi_set}")

# ---------------------------------------------------------------------
# 6. Funciones
# ---------------------------------------------------------------------

print("\n--- 6. Funciones ---")

# Definición de una función
def saludar(nombre="Invitado"):  # Parámetro con valor por defecto
    """Esta función saluda a alguien."""  # Docstring (documentación)
    return f"¡Hola, {nombre}!"

# Llamada a la función
saludo = saludar("Ana")
print(saludo)
saludo_anonimo = saludar()  # Usa el valor por defecto
print(saludo_anonimo)

# Funciones con argumentos variables (*args, **kwargs)
def sumar_varios(*args):  # Recibe un número variable de argumentos posicionales en una tupla
    """Suma todos los argumentos numéricos."""
    total = 0
    for numero in args:
        total += numero
    return total

suma_total = sumar_varios(1, 2, 3, 4)
print(f"Suma total: {suma_total}")

def mostrar_info(**kwargs):  # Recibe argumentos con nombre en un diccionario
    """Muestra la información recibida."""
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Juan", edad=30, ciudad="Madrid")

# Funciones recursivas (se llaman a sí mismas)
def factorial_recursivo(n):
    """Calcula el factorial de un número de forma recursiva."""
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n-1)

factorial_5 = factorial_recursivo(5)
print(f"Factorial de 5: {factorial_5}")

# ---------------------------------------------------------------------
# 7. Excepciones
# ---------------------------------------------------------------------

print("\n--- 7. Excepciones ---")

try:
    # Código que puede lanzar una excepción
    numero_str = input("Introduce un número: ")
    numero = int(numero_str)
    resultado = 10 / numero
    print(f"Resultado: {resultado}")

except ValueError:
    # Manejo de la excepción ValueError (error al convertir)
    print("Error: Debes introducir un número entero válido.")

except ZeroDivisionError:
    # Manejo de la excepción ZeroDivisionError
    print("Error: No se puede dividir por cero.")

except Exception as e:
    # Manejo de cualquier otra excepción (más general)
    print(f"Ocurrió un error inesperado: {e}")

finally:
    # Código que se ejecuta siempre (haya o no excepción)
    print("Fin del bloque try-except.")

# Lanzar una excepción manualmente (raise)
def verificar_edad(edad):
    """Verifica si la edad es válida (mayor o igual a 0)."""
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    print("Edad válida.")

try:
    edad = int(input("Introduce tu edad: "))
    verificar_edad(edad)

except ValueError as e:
    print(f"Error: {e}")

# Afirmaciones (assert)
def calcular_raiz_cuadrada(numero):
    """Calcula la raíz cuadrada de un número. Lanza excepción si número < 0"""
    assert numero >= 0, "No se puede calcular la raíz cuadrada de un número negativo."
    return numero ** 0.5

try:
    numero = float(input("Introduce un número para calcular su raíz cuadrada: "))
    raiz = calcular_raiz_cuadrada(numero)
    print(f"La raíz cuadrada de {numero} es: {raiz}")

except AssertionError as e:
    print(f"Error: {e}")
# ---------------------------------------------------------------------
# 8. Iteradores e Iterables
# ---------------------------------------------------------------------

print("\n--- 8. Iteradores e Iterables ---")

# Iterable (ejemplo: una lista)
mi_lista = [1, 2, 3]

# Obtener un iterador a partir del iterable
iterador = iter(mi_lista)

# Iterar manualmente usando next()
print(next(iterador))  # Imprime 1
print(next(iterador))  # Imprime 2
print(next(iterador))  # Imprime 3

#Intentar seguir iterando lanza una excepción StopIteration
#print(next(iterador))  # Lanza StopIteration

# Iterar con un bucle for (automáticamente gestiona el iterador)
print("\nIteración con bucle for:")
for elemento in mi_lista:
    print(elemento)

#Creación de un iterador personalizado
class IteradorDePotencias:
    def __init__(self, maximo):
        self.maximo = maximo
        self.numero = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.numero <= self.maximo:
            resultado = self.numero ** 2
            self.numero += 1
            return resultado
        else:
            raise StopIteration

#Uso del iterador personalizado
potencias = IteradorDePotencias(5)
print("\nIterador personalizado:")
for potencia in potencias:
    print(potencia)

# ---------------------------------------------------------------------
# 9. List Comprehensions y Generator Expressions
# ---------------------------------------------------------------------

print("\n--- 9. List Comprehensions y Generator Expressions ---")

# List Comprehension (crea una nueva lista)
cuadrados = [x**2 for x in range(10)]  # Cuadrados de 0 a 9
print(f"List comprehension: {cuadrados}")

# Generator Expression (crea un iterador, no almacena la lista en memoria)
cuadrados_generador = (x**2 for x in range(10))
print(f"Generator expression: {cuadrados_generador}") #imprime la referencia al objeto generador
print("\nGenerator Expression iterando:")
for cuadrado in cuadrados_generador:
    print(cuadrado)