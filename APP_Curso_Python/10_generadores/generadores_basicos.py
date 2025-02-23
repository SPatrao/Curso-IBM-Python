# GENERADORES BÁSICOS EN PYTHON

# Generador simple
def generador_numeros(n):
    """Genera números del 0 al n-1"""
    # La función generador_numeros toma un argumento `n` y usa un ciclo `for` para iterar desde 0 hasta n-1.
    # En cada iteración, se usa `yield` para devolver el valor de i en lugar de retornar todos los valores de una vez.
    for i in range(n):
        yield i  # La palabra clave `yield` permite que el generador devuelva valores uno a uno.

# Generador de cuadrados
def generador_cuadrados(n):
    """Genera cuadrados de números"""
    # Similar al generador anterior, pero en lugar de devolver los números directamente, devuelve el cuadrado de cada número.
    for i in range(n):
        yield i ** 2  # Calcula el cuadrado de `i` y lo devuelve.

# Generador infinito
def generador_cuenta_infinita(inicio=0):
    """Generador que cuenta indefinidamente"""
    # Este generador comienza en un valor `inicio` y genera números consecutivos indefinidamente.
    # Utiliza un bucle `while True` para que el generador nunca termine de producir números.
    contador = inicio  # Inicializa el contador con el valor `inicio` (0 por defecto).
    while True:
        yield contador  # Devuelve el valor actual de `contador`.
        contador += 1  # Incrementa el contador en 1 en cada iteración.

# Generador con condición
def generador_pares(n):
    """Genera números pares hasta n"""
    # Este generador genera solo los números pares en el rango de 0 a n-1.
    # Usa una condición `if` dentro del ciclo para verificar si el número es par.
    for i in range(n):
        if i % 2 == 0:  # La condición `i % 2 == 0` verifica si el número es par.
            yield i  # Si es par, lo devuelve.

# Simulación de lectura de archivo grande
def lector_archivo_grande(ruta_archivo):
    """Generador para leer archivos grandes línea por línea"""
    # Este generador permite leer archivos grandes línea por línea de manera eficiente, sin cargar todo el archivo en memoria.
    # Usa `open` para abrir el archivo en modo lectura (`'r'`) y luego itera sobre las líneas del archivo.
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            yield linea.strip()  # La función `strip()` elimina cualquier espacio en blanco o salto de línea adicional.

if __name__ == "__main__":
    # Ejemplo de uso de generadores
    print("Generador de números:")
    for num in generador_numeros(5):
        print(num)  # Imprime los números generados por `generador_numeros(5)`, que serán del 0 al 4.

    print("\nGenerador de cuadrados:")
    cuadrados = list(generador_cuadrados(5))  # Convierte el generador en una lista para imprimir los cuadrados.
    print(cuadrados)  # Imprime la lista de cuadrados: [0, 1, 4, 9, 16].

    print("\nGenerador de pares:")
    pares = list(generador_pares(10))  # Convierte el generador de números pares en una lista.
    print(pares)  # Imprime los números pares hasta 10: [0, 2, 4, 6, 8].

    # Generador infinito (limitar con islice)
    from itertools import islice
    print("\nPrimeros 5 números del generador infinito:")
    generador_infinito = generador_cuenta_infinita()  # Crea un generador que cuenta infinitamente a partir de 0.
    primeros_5 = list(islice(generador_infinito, 5))  # Usa `islice` para tomar solo los primeros 5 números.
    print(primeros_5)  # Imprime los primeros 5 números del generador: [0, 1, 2, 3, 4].

    # Ejemplo de memoria eficiente
    import sys
    
    # Comparación de memoria: lista vs generador
    lista_cuadrados = [x**2 for x in range(1000000)]  # Crea una lista con los cuadrados de los primeros 1,000,000 de números.
    generador_cuadrados = (x**2 for x in range(1000000))  # Crea un generador que genera los cuadrados de los primeros 1,000,000 de números.
    
    # Se utiliza `sys.getsizeof()` para comparar el tamaño en memoria de ambos enfoques.
    print("\nTamaño de lista de cuadrados:", sys.getsizeof(lista_cuadrados), "bytes")  # Muestra el tamaño de la lista en bytes.
    print("Tamaño de generador de cuadrados:", sys.getsizeof(generador_cuadrados), "bytes")  # Muestra el tamaño del generador en bytes.
