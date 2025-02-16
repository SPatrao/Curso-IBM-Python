# DEFINICIÓN DE FUNCIONES EN PYTHON

# 1. Función simple sin parámetros
# Una función simple es aquella que no requiere argumentos o parámetros para ejecutarse.
def saludar():
    print("Hola, mundo!")  # La función imprime un mensaje en la consola.

# Llamamos a la función 'saludar' para ejecutar el código dentro de ella.
saludar()  # Esto imprime "Hola, mundo!" en la consola.

# 2. Función con parámetros
# Las funciones pueden tomar valores de entrada llamados "parámetros".
# En este caso, la función 'saludo_personalizado' toma un parámetro llamado 'nombre'.
def saludo_personalizado(nombre):
    print(f"Hola, {nombre}!")  # La función utiliza el parámetro 'nombre' para imprimir un mensaje.

# Llamamos a la función y pasamos el valor "Juan" como argumento para el parámetro 'nombre'.
saludo_personalizado("Juan")  # Esto imprimirá "Hola, Juan!" en la consola.

# 3. Función con múltiples parámetros
# Una función puede tener más de un parámetro. Aquí la función 'suma' toma dos parámetros: 'a' y 'b'.
def suma(a, b):
    return a + b  # La función retorna la suma de los dos parámetros.

# Llamamos a la función 'suma' con los valores 5 y 3 como argumentos.
resultado = suma(5, 3)  # La función devuelve 8, que es la suma de 5 y 3.
print(resultado)  # Imprime el valor de 'resultado', que es 8.

# 4. Función con parámetros por defecto
# Puedes definir valores predeterminados para los parámetros de una función.
# Si no se proporciona un valor al llamar a la función, se usará el valor por defecto.
def potencia(base, exponente=2):  # 'exponente' tiene un valor por defecto de 2.
    return base ** exponente  # La función retorna 'base' elevada a la potencia 'exponente'.

# Llamamos a la función 'potencia' pasando solo el argumento 'base', por lo que 'exponente' usará su valor por defecto (2).
print(potencia(4))     # 16 (4^2), ya que el valor por defecto de 'exponente' es 2.

# Llamamos a la función 'potencia' pasando tanto 'base' como 'exponente', por lo que el valor de 'exponente' será 3.
print(potencia(4, 3))  # 64 (4^3), ya que hemos cambiado el valor del 'exponente' a 3.

# 5. Función con número variable de argumentos (*args)
# En Python, puedes usar *args para pasar un número variable de argumentos a una función.
# 'args' es una tupla que contiene todos los argumentos que se pasan a la función.
def suma_multiple(*args):
    total = 0  # Inicializamos la variable 'total' en 0.
    for numero in args:  # Iteramos sobre todos los números en 'args'.
        total += numero  # Sumamos cada número a 'total'.
    return total  # La función devuelve la suma de todos los números pasados.

# Llamamos a la función 'suma_multiple' pasando varios números como argumentos.
print(suma_multiple(1, 2, 3, 4, 5))  # 15 (1 + 2 + 3 + 4 + 5)

# 6. Función con argumentos nominales (**kwargs)
# También puedes usar **kwargs para pasar un número variable de argumentos nombrados (key-value).
# 'kwargs' es un diccionario que contiene los nombres de los parámetros y sus valores asociados.
def informacion_persona(**kwargs):
    # Usamos un ciclo 'for' para iterar sobre los elementos del diccionario 'kwargs'.
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")  # Imprimimos el nombre del parámetro (clave) y su valor.

# Llamamos a la función 'informacion_persona' pasando varios argumentos nombrados.
informacion_persona(nombre="Juan", edad=30, ciudad="Madrid")
# Esto imprimirá:
# nombre: Juan
# edad: 30
# ciudad: Madrid
