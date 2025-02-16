# DECORADORES AVANZADOS EN PYTHON

# Decorador con parámetros
def repetir(num_veces):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            for _ in range(num_veces):
                resultado = funcion(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir(3)
def saludo(nombre):
    print(f"¡Hola, {nombre}!")

# Decorador de registro (logging)
import functools
import logging

logging.basicConfig(level=logging.INFO)

def log_llamadas(funcion):
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        logging.info(f"Llamando a {funcion.__name__}")
        logging.info(f"Argumentos: {args}, {kwargs}")
        try:
            resultado = funcion(*args, **kwargs)
            logging.info(f"Resultado: {resultado}")
            return resultado
        except Exception as e:
            logging.error(f"Excepción en {funcion.__name__}: {e}")
            raise
    return wrapper

@log_llamadas
def dividir(a, b):
    return a / b

# Decorador de caché (memoización)
def cache(funcion):
    cache_dict = {}
    @functools.wraps(funcion)
    def wrapper(*args):
        if args not in cache_dict:
            cache_dict[args] = funcion(*args)
        return cache_dict[args]
    return wrapper

@cache
def fibonacci_optimizado(n):
    if n <= 1:
        return n
    return fibonacci_optimizado(n-1) + fibonacci_optimizado(n-2)

# Decorador de clase
def singleton(clase):
    instancias = {}
    def obtener_instancia(*args, **kwargs):
        if clase not in instancias:
            instancias[clase] = clase(*args, **kwargs)
        return instancias[clase]
    return obtener_instancia

@singleton
class ClaseSingleton:
    def __init__(self):
        self.valor = None

if __name__ == "__main__":
    # Ejemplo de decorador con parámetros
    saludo("Python")

    # Ejemplo de logging
    try:
        dividir(10, 2)
        dividir(10, 0)  # Generará un error
    except ZeroDivisionError:
        pass

    # Ejemplo de caché (memoización)
    print("Fibonacci de 35:")
    print(fibonacci_optimizado(35))

    # Ejemplo de singleton
    instancia1 = ClaseSingleton()
    instancia2 = ClaseSingleton()
    print("¿Son la misma instancia?", instancia1 is instancia2)

