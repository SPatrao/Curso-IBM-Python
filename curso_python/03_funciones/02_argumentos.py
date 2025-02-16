# TIPOS DE ARGUMENTOS EN FUNCIONES

# 1. Argumentos posicionales
# Los argumentos posicionales son aquellos que se pasan a la función en un orden específico.
# El orden en que se pasan es crucial para que la función los reciba correctamente.
def resta(a, b):
    # La función toma dos argumentos, 'a' y 'b', y devuelve la resta de 'a' - 'b'.
    return a - b

# Llamamos a la función 'resta' y pasamos los valores 10 y 5 como argumentos.
print(resta(10, 5))  # El resultado es 5 (10 - 5)

# 2. Argumentos nominales (también conocidos como keyword arguments)
# Los argumentos nominales se pasan a la función mediante el nombre del parámetro.
# Esto permite que no sea necesario seguir el orden de los parámetros, sino que puedes especificar el nombre de cada uno.
def division(dividendo, divisor):
    # La función toma dos argumentos llamados 'dividendo' y 'divisor',
    # y devuelve el resultado de dividir 'dividendo' entre 'divisor'.
    return dividendo / divisor

# Aquí llamamos a la función 'division', pero pasamos los argumentos por nombre, no por posición.
print(division(dividendo=10, divisor=2))  # El resultado es 5 (10 / 2)
print(division(divisor=2, dividendo=10))  # También 5, ya que el orden de los argumentos no importa.

# 3. Combinación de argumentos
# Las funciones pueden combinar diferentes tipos de argumentos, como posicionales, con valores predeterminados, 
# argumentos variables, y argumentos nominales.
# En este caso, combinamos todos esos tipos en una misma función.
def funcion_mixta(a, b, c=10, *args, **kwargs):
    # 'a' y 'b' son argumentos posicionales.
    # 'c' es un argumento con un valor predeterminado de 10.
    # '*args' permite pasar un número variable de argumentos posicionales adicionales (se almacenan como una tupla).
    # '**kwargs' permite pasar un número variable de argumentos nombrados (se almacenan como un diccionario).
    
    print(f"a: {a}")  # Imprime el valor de 'a'.
    print(f"b: {b}")  # Imprime el valor de 'b'.
    print(f"c: {c}")  # Imprime el valor de 'c'. Si no se pasa, usa el valor por defecto (10).
    print(f"args: {args}")  # Imprime los valores adicionales pasados a través de '*args'.
    print(f"kwargs: {kwargs}")  # Imprime los valores adicionales pasados a través de '**kwargs'.

# Llamamos a la función pasando 1 y 2 como 'a' y 'b', luego 3 como 'c', 
# y pasamos 4, 5 como argumentos adicionales posicionales (en 'args') y x=6, y=7 como argumentos nombrados (en 'kwargs').
funcion_mixta(1, 2, 3, 4, 5, x=6, y=7)

# 4. Desempaquetado de listas/tuplas
# El desempaquetado de listas o tuplas se refiere a la capacidad de pasar los elementos de una lista o tupla
# como argumentos individuales a la función. Usamos el operador '*' para desempaquetar una lista o tupla.
def suma_tres(x, y, z):
    # La función toma tres parámetros y devuelve su suma.
    return x + y + z

# Creamos una lista llamada 'numeros' con los valores [1, 2, 3].
numeros = [1, 2, 3]

# Usamos el operador '*' para desempaquetar la lista 'numeros' y pasar sus elementos como argumentos.
print(suma_tres(*numeros))  # El resultado es 6 (1 + 2 + 3), ya que estamos pasando los tres elementos de 'numeros' como 'x', 'y', 'z'.

# 5. Desempaquetado de diccionarios
# Similar al desempaquetado de listas, podemos desempaquetar diccionarios usando el operador '**'.
# Esto pasa las claves del diccionario como nombres de parámetros y los valores como sus respectivos valores.
def datos_persona(nombre, edad, ciudad):
    # La función toma tres parámetros: 'nombre', 'edad', y 'ciudad', y los imprime en formato de frase.
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

# Creamos un diccionario llamado 'persona' con las claves 'nombre', 'edad', y 'ciudad'.
persona = {"nombre": "María", "edad": 25, "ciudad": "Barcelona"}

# Usamos el operador '**' para desempaquetar el diccionario 'persona' y pasar sus claves y valores como argumentos nombrados.
datos_persona(**persona)
# Esto imprimirá: "María tiene 25 años y vive en Barcelona", ya que 'nombre', 'edad', y 'ciudad' son pasados como argumentos por nombre.
