# FUNCIONES LAMBDA (FUNCIONES ANÓNIMAS)

# 1. Lambda simple
# Las funciones lambda son una forma concisa de escribir funciones pequeñas y anónimas. Se definen usando la palabra clave 'lambda'.
# La sintaxis es: lambda argumentos: expresión
# En este caso, la función lambda toma dos parámetros 'x' y 'y', y devuelve la suma de ellos.
suma = lambda x, y: x + y  # Esta función toma 'x' y 'y' y devuelve 'x + y'
print(suma(5, 3))  # 8
# Aquí estamos llamando a la función lambda 'suma' con los valores 5 y 3.
# El resultado de sumar 5 + 3 es 8, por lo tanto se imprime 8.

# 2. Uso con funciones integradas
# Las funciones lambda se pueden usar con funciones integradas como map(), filter() y sorted().
# Aquí usamos 'map()' junto con una función lambda para aplicar una operación a cada elemento de una lista.
# La función 'map()' toma una función y un iterable, y aplica esa función a cada elemento del iterable.
numeros = [1, 2, 3, 4, 5]
# 'map()' aplica la función lambda a cada elemento de la lista 'numeros'.
# La función lambda toma cada número 'x' y devuelve su cuadrado 'x**2'.
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]
# Aquí, 'map()' calcula el cuadrado de cada número en la lista 'numeros' y lo convierte en una nueva lista.
# El resultado es la lista [1, 4, 9, 16, 25], que se imprime.

# 3. Filtrado con lambda
# Usamos 'filter()' para filtrar elementos de una lista basándonos en una condición.
# 'filter()' toma una función y un iterable, y devuelve los elementos del iterable que hacen que la función devuelva True.
# En este caso, queremos filtrar los números pares (es decir, aquellos que son divisibles por 2).
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]
# La función lambda toma cada número 'x' y devuelve True si 'x' es divisible por 2 (es decir, si es un número par).
# 'filter()' devuelve solo los números que cumplen esta condición, en este caso, [2, 4].

# 4. Lambda con sorted()
# 'sorted()' ordena los elementos de un iterable. También acepta un argumento 'key' que especifica una función de clave para ordenar.
# Aquí usamos una función lambda para ordenar una lista de diccionarios por la clave 'nota'.
estudiantes = [
    {'nombre': 'Juan', 'nota': 85},
    {'nombre': 'María', 'nota': 90},
    {'nombre': 'Pedro', 'nota': 75}
]
# 'sorted()' ordena la lista de estudiantes por la 'nota' de cada diccionario.
# La función lambda toma cada diccionario 'x' y devuelve el valor de la clave 'nota' (x['nota']) para usarlo como criterio de ordenación.
estudiantes_ordenados = sorted(estudiantes, key=lambda x: x['nota'])
print(estudiantes_ordenados)
# Esto ordenará los estudiantes de menor a mayor nota.
# El resultado será: [{'nombre': 'Pedro', 'nota': 75}, {'nombre': 'Juan', 'nota': 85}, {'nombre': 'María', 'nota': 90}]

# 5. Operaciones más complejas
# Las funciones lambda también pueden incluir operaciones más complejas, como condicionales (if/else).
# En este caso, usamos una expresión lambda que realiza una operación diferente dependiendo de la comparación entre 'x' y 'y'.
operacion = lambda x, y: x * y if x > y else x + y
# La lambda recibe dos argumentos 'x' y 'y'.
# Si 'x' es mayor que 'y', devuelve el producto de 'x' e 'y'.
# De lo contrario, devuelve la suma de 'x' y 'y'.
print(operacion(5, 3))   # 15
# En este caso, 5 > 3, por lo que la función lambda devuelve 5 * 3 = 15, y eso es lo que se imprime.

print(operacion(2, 5))   # 7
# Aquí, 2 no es mayor que 5, por lo que la función lambda devuelve 2 + 5 = 7, y eso es lo que se imprime.
