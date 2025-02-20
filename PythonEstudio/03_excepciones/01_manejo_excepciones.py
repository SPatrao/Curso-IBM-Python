# MANEJO DE EXCEPCIONES EN PYTHON
# ======================================
# Objetivo: Proporcionar una guía completa sobre el manejo de excepciones en Python.
# Este archivo cubre el uso de bloques try-except y la captura de excepciones
# para mejorar la robustez del código.

# 1. Bloque try-except básico
# Las excepciones son errores que ocurren durante la ejecución del programa.
# Usamos el bloque 'try' para intentar ejecutar un código potencialmente problemático,
# y el bloque 'except' para manejar cualquier error que surja.
try:
    x = 10 / 0  # Intentamos dividir 10 entre 0, generando un ZeroDivisionError
except ZeroDivisionError:  # Capturamos específicamente el error de división por cero
    print("No se puede dividir por cero.")  # Mensaje que se muestra si ocurre el error

# 2. Múltiples excepciones
# Se pueden capturar diferentes tipos de excepciones usando múltiples bloques except.
try:
    numero = int(input("🔹 Ingresa un número: "))  # Pedimos al usuario que ingrese un número
    resultado = 10 / numero  # Intentamos dividir 10 entre el número ingresado
except ValueError:  # Capturamos si se ingresa un valor que no se puede convertir a int
    print("Entrada inválida. Debes ingresar un número.")
except ZeroDivisionError:  # Capturamos si se intenta dividir por cero
    print("No se puede dividir por cero.")

# 3. Capturar cualquier excepción
# Capturamos cualquier tipo de error general usando Exception como clase base.
try:
    valor = int("texto")  # Intentamos convertir una cadena no numérica
except Exception as error:  # Capturamos cualquier excepción en 'error'
    print(f"Ocurrió un error: {error}")  # Mostramos el mensaje del error

# 4. Bloque else
# El bloque 'else' se ejecuta si no ocurrió ninguna excepción en el bloque 'try'.
try:
    numero = int(input("🔹 Ingresa un número: "))  # Solicitamos un número al usuario
except ValueError:  # Si el usuario ingresa un valor no numérico
    print("Entrada inválida.")  # Mensaje de error
else:  # Se ejecuta si no hay excepciones
    print(f"El número ingresado es: {numero}")  # Imprimimos el número

# 5. Bloque finally
# El bloque 'finally' se ejecuta siempre, independientemente de errores o no.
archivo = None  # Inicializamos la variable para manejar el archivo
try:
    archivo = open("ejemplo.txt", "r")  # Intentamos abrir un archivo para lectura
    contenido = archivo.read()  # Leemos el contenido del archivo
except FileNotFoundError:  # Capturamos si el archivo no se encuentra
    print("El archivo no existe.")  # Mensaje informativo
finally:
    if archivo:  # Si el archivo se abrió con éxito
        archivo.close()  # Cerramos el archivo para liberar recursos

# EJERCICIOS FINALES
# ======================================
print("\n🔹 Ejercicios Finales:")

# Ejercicio 1: Capturar errores de entrada con un bloque try-except.
try:
    numero = int(input("Ingresa un número para la división: "))  # Solicita un número
    resultado_division = 10 / numero  # Realiza la división
    print(f"El resultado de dividir 10 entre {numero} es: {resultado_division}")  # Imprime el resultado
except ZeroDivisionError:
    print("No se puede dividir por cero.")  # Mensaje de error
except ValueError:
    print("Entrada inválida. Debes ingresar un número entero.")  # Mensaje para entrada no válida

# Ejercicio 2: Pedir una lista de números y calcular la media, manejando las excepciones adecuadamente.
try:
    lista_numeros = input("Ingresa una lista de números separados por comas: ")  # Solicita la lista
    lista_numeros = [float(num) for num in lista_numeros.split(',')]  # Convierte cada número a float
    media = sum(lista_numeros) / len(lista_numeros)  # Calcula la media
    print(f"La media de los números ingresados es: {media}")  # Imprime la media
except ValueError:
    print("Entrada inválida. Asegúrate de ingresar solo números separados por comas.")  # Mensaje para error
except ZeroDivisionError:
    print("No se puede calcular la media de una lista vacía.")  # Mensaje para lista vacía

