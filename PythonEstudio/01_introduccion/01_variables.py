# 01_variables.py
# ========================
# Objetivo: Introducir el concepto de variables y su uso en Python.
# Este archivo proporciona una guía completa sobre los tipos de variables, 
# así como ejemplos prácticos y ejercicios para ayudar a los principiantes.

# VARIABLES EN PYTHON
# ------------------------------
# Guía completa de declaración y uso

# Introducción a los tipos básicos de variables
print("\n📌 TIPOS BÁSICOS DE VARIABLES")

# **1. Números enteros (int)**: Son números enteros, positivos o negativos.
print("\n🔹 Variables de tipo entero (int):")
edad = 25  # Una variable llamada 'edad' que guarda el valor 25 (entero)
print(f"Edad (int): {edad}")  # Mostramos la variable 'edad'
contador = -10  # Un número entero negativo
print(f"Contador (int): {contador}")  # Mostramos la variable 'contador'

# **2. Números de punto flotante (float)**: Son números con decimales.
print("\n🔹 Variables de tipo flotante (float):")
altura = 1.75  # Una variable de tipo flotante que guarda el valor 1.75
temperatura = -5.6  # Otro número flotante negativo
print(f"Altura (float): {altura}")  # Mostramos la variable 'altura'
print(f"Temperatura (float): {temperatura}")  # Mostramos la variable 'temperatura'

# **3. Cadenas de texto (str)**: Son secuencias de caracteres.
print("\n🔹 Variables de tipo cadena de texto (str):")
nombre = "Juan Pérez"  # Una cadena de texto con un nombre
mensaje = 'Hola, mundo'  # Una cadena de texto con un saludo
multilinea = """Este es un texto
que ocupa varias líneas"""  # Cadena de texto que ocupa varias líneas
print(f"Nombre (str): {nombre}")  # Mostramos el nombre
print(f"Mensaje (str): {mensaje}")  # Mostramos el mensaje
print(f"Texto Multilínea (str): {multilinea}")  # Mostramos el texto multilínea

# **4. Booleanos (bool)**: Son valores que pueden ser True (verdadero) o False (falso).
print("\n🔹 Variables de tipo booleano (bool):")
es_estudiante = True  # La variable 'es_estudiante' es True (verdadero)
tiene_trabajo = False  # La variable 'tiene_trabajo' es False (falso)
print(f"Es estudiante (bool): {es_estudiante}")  # Mostramos si es estudiante
print(f"Tiene trabajo (bool): {tiene_trabajo}")  # Mostramos si tiene trabajo

# **5. Declaración múltiple**: Se pueden declarar varias variables en una sola línea.
print("\n🔹 Declaración de múltiples variables en una sola línea:")
x, y, z = 1, 2, 3  # Asignamos 1 a x, 2 a y y 3 a z en una sola línea
print(f"x: {x}, y: {y}, z: {z}")  # Mostramos las variables x, y, z

# CONVERSIÓN DE TIPOS (CASTING)
# ---------------------------------------
print("\n📌 CONVERSIÓN DE TIPOS (CASTING)")

# **1. str a int**: Convertir una cadena de texto en un número entero
print("\n🔹 Convertir cadena a entero (str → int):")
edad_str = "30"  # La cadena de texto "30"
edad_int = int(edad_str)  # Convertimos la cadena "30" a un número entero
print(f"Edad como entero: {edad_int}")  # Mostramos la edad como entero

# **2. int a float**: Convertir un número entero en un flotante
print("\n🔹 Convertir entero a flotante (int → float):")
edad_float = float(edad)  # Convertimos la variable 'edad' (que es un entero) a un flotante
print(f"Edad como flotante: {edad_float}")  # Mostramos la edad como flotante

# **3. float a int**: Convertir un número flotante en un entero
print("\n🔹 Convertir flotante a entero (float → int):")
altura_int = int(altura)  # Convertimos el número flotante 'altura' a entero (se pierde la parte decimal)
print(f"Altura como entero: {altura_int}")  # Mostramos la altura como entero

# FUNCIONES ÚTILES
# ---------------------------------------
print("\n📌 FUNCIONES ÚTILES")
# **Verificar el tipo de una variable usando type()**
print("\n🔹 Verificar el tipo de una variable con type():")
print(f"Tipo de edad: {type(edad)}")  # Muestra el tipo de la variable 'edad', que es int
print(f"Tipo de nombre: {type(nombre)}")  # Muestra el tipo de la variable 'nombre', que es str

# BUENAS PRÁCTICAS EN PYTHON
# ---------------------------------------
print("\n📌 BUENAS PRÁCTICAS EN PYTHON")
print("- Usar nombres descriptivos y en snake_case para variables.")
print("- Documenta el código con comentarios claros.")
print("- Asegúrate de validar entradas de usuario.")
print("- Usa f-strings para imprimir valores: f'...' es más limpio y fácil de leer.")

# EJERCICIO FINAL
# ---------------------------------------
print("\n🔹 Ejercicio Final:")
try:
    edad_usuario = int(input("Por favor, ingresa tu edad: "))
    print(f"Tienes {edad_usuario} años.")
except ValueError:
    print("❌ Error: ¡Por favor, ingresa un número válido!")

# GLOSARIO
# ---------------------------------------
print("""
📖 Glosario:
- Variable: Espacio en memoria donde se almacena información.
- Tipo de dato: Clasificación de los valores (int, float, str, bool).
- Casting: Conversión de un tipo de dato a otro.
""")