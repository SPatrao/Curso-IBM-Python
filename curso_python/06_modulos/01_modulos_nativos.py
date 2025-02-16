# MÓDULOS NATIVOS DE PYTHON

# Módulo matemático
import math

print("Funciones matemáticas:")
print("Pi:", math.pi)
print("Raíz cuadrada de 16:", math.sqrt(16))
print("Valor absoluto de -10:", abs(-10))
print("Redondeo de 3.7:", round(3.7))

# Módulo de fecha y hora
import datetime

print("\nFecha y Hora:")
fecha_actual = datetime.datetime.now()
print("Fecha actual:", fecha_actual)
print("Año:", fecha_actual.year)
print("Mes:", fecha_actual.month)
print("Día:", fecha_actual.day)

# Módulo random
import random

print("\nFunciones aleatorias:")
print("Número aleatorio entre 0 y 1:", random.random())
print("Entero aleatorio entre 1 y 10:", random.randint(1, 10))
print("Elemento aleatorio de una lista:", random.choice([1, 2, 3, 4, 5]))

# Módulo de sistema
import sys

print("\nInformación del sistema:")
print("Versión de Python:", sys.version)
print("Plataforma:", sys.platform)

# Módulo de tiempo
import time

print("\nFunciones de tiempo:")
print("Tiempo actual en segundos:", time.time())

# Módulo de sistema operativo
import os

print("\nOperaciones del sistema:")
print("Directorio actual:", os.getcwd())
print("Contenido del directorio:", os.listdir())

