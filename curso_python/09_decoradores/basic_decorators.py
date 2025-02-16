# DECORADORES BÁSICOS EN PYTHON

# Decorador simple
def mi_decorador(funcion):
    def wrapper():
        print("Antes de la función")
        funcion()
        print("Después de la función")
    return wrapper

@mi_decorador
def saludo():
    print("¡Hola, mundo!")

# Decorador con argumentos
def decorador_con_argumentos(funcion):
    def wrapper(*args, **kwargs):
        print(f"Llamando a la función {funcion.__name__}")
        print(f"Argumentos: {args}")
        resultado = funcion(*args, **kwargs)
        print("Función completada")
        return resultado
    return wrapper

@decorador_con_argumentos
def suma(a, b):
    return a + b

# Decorador de tiempo de ejecución
import time

def medir_tiempo(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución de {funcion.__name__}: {fin - inicio} segundos")
        return resultado
    return wrapper

@medir_tiempo
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    # Ejemplo de decorador simple
    saludo()

    # Ejemplo de decorador con argumentos
    resultado = suma(5, 3)
    print("Resultado de la suma:", resultado)

    # Ejemplo de medición de tiempo
    print("Fibonacci de 30:")
    fibonacci(30)

