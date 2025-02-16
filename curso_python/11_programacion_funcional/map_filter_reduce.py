# PROGRAMACIÓN FUNCIONAL: MAP, FILTER, REDUCE

from functools import reduce

# Uso de map()
def cuadrado(x):
    """Función para elevar al cuadrado"""
    return x ** 2

def map_ejemplo():
    """Ejemplos de uso de map()"""
    numeros = [1, 2, 3, 4, 5]
    
    # Map con función definida
    cuadrados = list(map(cuadrado, numeros))
    print("Cuadrados usando map():", cuadrados)
    
    # Map con función lambda
    cubos = list(map(lambda x: x ** 3, numeros))
    print("Cubos usando map():", cubos)

# Uso de filter()
def filter_ejemplo():
    """Ejemplos de uso de filter()"""
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Filter con función definida
    def es_par(x):
        return x % 2 == 0
    
    pares = list(filter(es_par, numeros))
    print("Números pares usando filter():", pares)
    
    # Filter con función lambda
    mayores_cinco = list(filter(lambda x: x > 5, numeros))
    print("Números mayores que 5:", mayores_cinco)

# Uso de reduce()
def reduce_ejemplo():
    """Ejemplos de uso de reduce()"""
    numeros = [1, 2, 3, 4, 5]
    
    # Suma de todos los elementos
    suma_total = reduce(lambda x, y: x + y, numeros)
    print("Suma total usando reduce():", suma_total)
    
    # Encontrar el máximo
    maximo = reduce(lambda x, y: x if x > y else y, numeros)
    print("Máximo usando reduce():", maximo)

# Combinación de map, filter y reduce
def combinacion_funcional():
    """Ejemplo combinando funciones funcionales"""
    numeros = range(1, 11)
    
    resultado = reduce(
        lambda x, y: x + y, 
        filter(
            lambda x: x % 2 == 0, 
            map(lambda x: x ** 2, numeros)
        )
    )
    
    print("Suma de cuadrados de pares:", resultado)

if __name__ == "__main__":
    map_ejemplo()
    print()
    filter_ejemplo()
    print()
    reduce_ejemplo()
    print()
    combinacion_funcional()

