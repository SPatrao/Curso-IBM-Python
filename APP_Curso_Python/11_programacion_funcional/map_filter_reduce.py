# PROGRAMACIÓN FUNCIONAL: MAP, FILTER, REDUCE

# Se importa la función `reduce` desde el módulo functools. Esta función es parte de la programación funcional
# y permite aplicar una operación acumulativa sobre los elementos de un iterable.
from functools import reduce

# Uso de map()
# La función `map()` aplica una función a cada elemento de un iterable y devuelve un iterador con los resultados.

def cuadrado(x):
    """Función para elevar al cuadrado un número"""
    return x ** 2

def map_ejemplo():
    """Ejemplos de uso de map()"""

    # Definimos una lista de números
    numeros = [1, 2, 3, 4, 5]
    
    # Usamos `map()` con una función definida previamente para elevar al cuadrado cada número de la lista
    cuadrados = list(map(cuadrado, numeros))
    print("Cuadrados usando map():", cuadrados)
    
    # Usamos `map()` con una función lambda, que permite hacer operaciones sin necesidad de definir una función previamente.
    # En este caso, se calcula el cubo de cada número de la lista.
    cubos = list(map(lambda x: x ** 3, numeros))
    print("Cubos usando map():", cubos)

# Uso de filter()
# La función `filter()` filtra los elementos de un iterable según una función de predicado (una función que devuelve True o False).

def filter_ejemplo():
    """Ejemplos de uso de filter()"""
    
    # Definimos una lista de números
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Creamos una función llamada `es_par` que devuelve True si el número es par.
    def es_par(x):
        return x % 2 == 0
    
    # Usamos `filter()` con la función definida `es_par` para obtener solo los números pares de la lista
    pares = list(filter(es_par, numeros))
    print("Números pares usando filter():", pares)
    
    # Usamos `filter()` con una función lambda que filtra los números mayores que 5.
    mayores_cinco = list(filter(lambda x: x > 5, numeros))
    print("Números mayores que 5:", mayores_cinco)

# Uso de reduce()
# La función `reduce()` aplica una función acumulativa a los elementos de un iterable, reduciéndolo a un único valor.

def reduce_ejemplo():
    """Ejemplos de uso de reduce()"""
    
    # Definimos una lista de números
    numeros = [1, 2, 3, 4, 5]
    
    # Usamos `reduce()` para sumar todos los elementos de la lista.
    # La función lambda toma dos elementos y devuelve su suma.
    suma_total = reduce(lambda x, y: x + y, numeros)
    print("Suma total usando reduce():", suma_total)
    
    # Usamos `reduce()` para encontrar el valor máximo de la lista.
    # La función lambda compara dos valores y devuelve el mayor de los dos.
    maximo = reduce(lambda x, y: x if x > y else y, numeros)
    print("Máximo usando reduce():", maximo)

# Combinación de map, filter y reduce
# En este ejemplo, combinamos las funciones `map()`, `filter()` y `reduce()` para realizar una operación más compleja.
# Primero se aplica un `map()` para elevar al cuadrado los números de 1 a 10.
# Luego, se usa `filter()` para seleccionar solo los números pares.
# Finalmente, se usa `reduce()` para sumar los resultados.

def combinacion_funcional():
    """Ejemplo combinando funciones funcionales"""
    
    # Creamos un rango de números de 1 a 10
    numeros = range(1, 11)
    
    # Primero, usamos `map()` para elevar al cuadrado los números.
    # Luego, usamos `filter()` para obtener solo los números pares.
    # Finalmente, usamos `reduce()` para sumar los números resultantes.
    resultado = reduce(
        lambda x, y: x + y,  # Función de reducción: suma acumulativa
        filter(  # `filter()` filtra los números pares
            lambda x: x % 2 == 0,  # Predicado para filtrar pares
            map(lambda x: x ** 2, numeros)  # `map()` eleva al cuadrado cada número
        )
    )
    
    # Imprimimos el resultado final
    print("Suma de cuadrados de pares:", resultado)

# Bloque principal donde se ejecutan los ejemplos

if __name__ == "__main__":
    # Ejecutamos la función `map_ejemplo` para ver los ejemplos de uso de `map()`
    map_ejemplo()
    print()
    
    # Ejecutamos la función `filter_ejemplo` para ver los ejemplos de uso de `filter()`
    filter_ejemplo()
    print()
    
    # Ejecutamos la función `reduce_ejemplo` para ver los ejemplos de uso de `reduce()`
    reduce_ejemplo()
    print()
    
    # Ejecutamos la función `combinacion_funcional` para ver cómo combinar las tres funciones
    combinacion_funcional()

