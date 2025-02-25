# MÓDULOS NATIVOS DE PYTHON

# Los módulos nativos de Python son bibliotecas estándar que proporcionan funciones adicionales
# que puedes usar sin necesidad de instalar nada adicional. A continuación se explican varios
# de los módulos más utilizados para realizar operaciones comunes.

# Importamos el módulo matemático para realizar operaciones avanzadas
import math  # El módulo 'math' proporciona funciones matemáticas como cálculos de raíces, trigonometría, etc.

# Uso de funciones matemáticas
print("Funciones matemáticas:")

# math.pi devuelve la constante matemática pi, que es aproximadamente 3.141592...
print("Pi:", math.pi)  # Constante del número pi (3.141592...)
# math.sqrt calcula la raíz cuadrada de un número.
print("Raíz cuadrada de 16:", math.sqrt(16))  # Calcula la raíz cuadrada de 16
# abs devuelve el valor absoluto de un número, es decir, elimina el signo negativo.
print("Valor absoluto de -10:", abs(-10))  # Devuelve el valor absoluto de -10
# round redondea un número decimal al entero más cercano.
print("Redondeo de 3.7:", round(3.7))  # Redondea el número 3.7 al entero más cercano

# Importamos el módulo datetime para trabajar con fechas y horas
import datetime  # El módulo 'datetime' permite trabajar con fechas y horas de manera sencilla.

print("\nFecha y Hora:")

# datetime.datetime.now() obtiene la fecha y hora actual del sistema.
fecha_actual = datetime.datetime.now()  # Obtiene la fecha y hora actual del sistema
print("Fecha actual:", fecha_actual)  # Muestra la fecha y hora completa (incluye año, mes, día, hora, etc.)

# Podemos extraer partes específicas de la fecha actual.
print("Año:", fecha_actual.year)  # Extrae solo el año
print("Mes:", fecha_actual.month)  # Extrae solo el mes
print("Día:", fecha_actual.day)  # Extrae solo el día

# Importamos el módulo random para generar valores aleatorios
import random  # El módulo 'random' se usa para generar números aleatorios y realizar selecciones aleatorias.

print("\nFunciones aleatorias:")

# random.random() genera un número decimal aleatorio entre 0.0 y 1.0.
print("Número aleatorio entre 0 y 1:", random.random())  # Genera un flotante aleatorio entre 0 y 1
# random.randint(a, b) genera un número entero aleatorio entre los valores a y b, incluyendo ambos.
print("Entero aleatorio entre 1 y 10:", random.randint(1, 10))  # Genera un entero aleatorio entre 1 y 10
# random.choice() selecciona un elemento aleatorio de una lista.
print("Elemento aleatorio de una lista:", random.choice([1, 2, 3, 4, 5]))  # Selecciona un elemento al azar de la lista

# Importamos el módulo sys para obtener información del sistema
import sys  # El módulo 'sys' proporciona acceso a variables y funciones que interactúan con el entorno del sistema.

print("\nInformación del sistema:")

# sys.version nos da la versión de Python que estamos utilizando actualmente.
print("Versión de Python:", sys.version)  # Muestra la versión de Python en uso
# sys.platform nos da información sobre el sistema operativo en el que estamos ejecutando Python.
print("Plataforma:", sys.platform)  # Muestra el sistema operativo en el que se ejecuta Python

# Importamos el módulo time para manejar tiempos y pausas
import time  # El módulo 'time' proporciona funciones para medir el tiempo y realizar pausas en la ejecución del programa.

print("\nFunciones de tiempo:")

# time.time() devuelve el tiempo en segundos desde el 1 de enero de 1970 (la época UNIX).
print("Tiempo actual en segundos:", time.time())  # Muestra la hora actual en segundos desde la época UNIX

# Importamos el módulo os para realizar operaciones con el sistema operativo
import os  # El módulo 'os' proporciona funciones para interactuar con el sistema operativo, como la gestión de archivos y directorios.

print("\nOperaciones del sistema:")

# os.getcwd() devuelve la ruta del directorio actual en el que se está ejecutando el script de Python.
print("Directorio actual:", os.getcwd())  # Muestra el directorio de trabajo actual
# os.listdir() devuelve una lista con los nombres de los archivos y directorios en el directorio actual.
print("Contenido del directorio:", os.listdir())  # Lista el contenido del directorio actual
