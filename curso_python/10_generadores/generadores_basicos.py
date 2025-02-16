# GENERADORES BÁSICOS EN PYTHON

# Generador simple
def generador_numeros(n):
    """Genera números del 0 al n-1"""
    for i in range(n):
        yield i

# Generador de cuadrados
def generador_cuadrados(n):
    """Genera cuadrados de números"""
    for i in range(n):
        yield i ** 2

# Generador infinito
def generador_cuenta_infinita(inicio=0):
    """Generador que cuenta indefinidamente"""
    contador = inicio
    while True:
        yield contador
        contador += 1

# Generador con condición
def generador_pares(n):
    """Genera números pares hasta n"""
    for i in range(n):
        if i % 2 == 0:
            yield i

# Simulación de lectura de archivo grande
def lector_archivo_grande(ruta_archivo):
    """Generador para leer archivos grandes línea por línea"""
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            yield linea.strip()

if __name__ == "__main__":
    # Ejemplo de uso de generadores
    print("Generador de números:")
    for num in generador_numeros(5):
        print(num)

    print("\nGenerador de cuadrados:")
    cuadrados = list(generador_cuadrados(5))
    print(cuadrados)

    print("\nGenerador de pares:")
    pares = list(generador_pares(10))
    print(pares)

    # Generador infinito (limitar con islice)
    from itertools import islice
    print("\nPrimeros 5 números del generador infinito:")
    generador_infinito = generador_cuenta_infinita()
    primeros_5 = list(islice(generador_infinito, 5))
    print(primeros_5)

    # Ejemplo de memoria eficiente
    import sys
    
    # Comparación de memoria: lista vs generador
    lista_cuadrados = [x**2 for x in range(1000000)]
    generador_cuadrados = (x**2 for x in range(1000000))
    
    print("\nTamaño de lista de cuadrados:", sys.getsizeof(lista_cuadrados), "bytes")
    print("Tamaño de generador de cuadrados:", sys.getsizeof(generador_cuadrados), "bytes")

