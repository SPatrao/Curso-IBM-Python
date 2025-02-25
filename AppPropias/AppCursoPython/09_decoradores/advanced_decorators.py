# DECORADORES AVANZADOS EN PYTHON

# Decorador con parámetros
def repetir(num_veces):
    """
    Este decorador recibe como parámetro el número de veces que se debe ejecutar la función.
    - num_veces: Número de veces que se ejecutará la función decorada.

    Devuelve un decorador que ejecutará la función la cantidad de veces especificada.
    """
    def decorador(funcion):
        """
        Función decoradora interna que se encarga de envolver la función original (funcion).
        """
        def wrapper(*args, **kwargs):
            """
            Función envolvente que llama a la función original repetidamente.
            - *args: Argumentos posicionales que se pasan a la función original.
            - **kwargs: Argumentos keyword que se pasan a la función original.
            
            Realiza la ejecución de la función decorada 'num_veces' veces.
            """
            for _ in range(num_veces):
                resultado = funcion(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

# Aplicamos el decorador @repetir con el argumento 3, indicando que la función saludo se ejecutará 3 veces
@repetir(3)
def saludo(nombre):
    """
    Función que saluda a la persona cuyo nombre se pasa como argumento.
    - nombre: El nombre de la persona que se va a saludar.
    """
    print(f"¡Hola, {nombre}!")

# Ejemplo de uso del decorador 'repetir'
# Esta llamada hará que la función saludo se ejecute 3 veces con el argumento "Python"
saludo("Python")

# Decorador de registro (logging)
import functools
import logging

# Configuramos el logger para que muestre mensajes a nivel INFO
logging.basicConfig(level=logging.INFO)

def log_llamadas(funcion):
    """
    Este decorador agrega funcionalidades de logging a cualquier función que decore.
    Registra la llamada a la función, los argumentos pasados y el resultado obtenido.
    
    - funcion: La función que está siendo decorada.
    
    Devuelve un 'wrapper' que maneja el registro (logging) de la ejecución de la función.
    """
    @functools.wraps(funcion)  # Usamos functools.wraps para preservar el nombre y la docstring de la función original
    def wrapper(*args, **kwargs):
        """
        Función envolvente que añade el registro antes y después de ejecutar la función.
        - *args: Argumentos posicionales para pasar a la función original.
        - **kwargs: Argumentos keyword para pasar a la función original.
        """
        # Log de la llamada a la función con los argumentos
        logging.info(f"Llamando a {funcion.__name__}")
        logging.info(f"Argumentos: {args}, {kwargs}")
        try:
            # Intentamos ejecutar la función original y capturamos el resultado
            resultado = funcion(*args, **kwargs)
            # Log del resultado de la función
            logging.info(f"Resultado: {resultado}")
            return resultado
        except Exception as e:
            # Si ocurre un error, lo registramos
            logging.error(f"Excepción en {funcion.__name__}: {e}")
            raise
    return wrapper

# Aplicamos el decorador @log_llamadas a la función dividir
@log_llamadas
def dividir(a, b):
    """
    Función que realiza una división entre 'a' y 'b'.
    - a: El numerador de la división.
    - b: El denominador de la división.
    """
    return a / b

# Ejemplo de uso del decorador 'log_llamadas'
# La primera llamada a dividir registrará la operación exitosa, la segunda generará un error por división entre 0.
try:
    dividir(10, 2)  # Operación exitosa
    dividir(10, 0)  # Esto generará un error de división por cero
except ZeroDivisionError:
    pass

# Decorador de caché (memoización)
def cache(funcion):
    """
    Este decorador almacena en caché los resultados de una función para evitar calcular lo mismo repetidamente.
    - funcion: La función que va a ser decorada.
    
    Devuelve un 'wrapper' que devuelve el resultado almacenado si ya fue calculado previamente.
    """
    cache_dict = {}  # Diccionario que guarda los resultados calculados para las entradas dadas
    @functools.wraps(funcion)
    def wrapper(*args):
        """
        Función envolvente que implementa el almacenamiento en caché.
        - *args: Argumentos posicionales para pasar a la función original.
        """
        if args not in cache_dict:
            # Si los argumentos no están en la caché, calculamos el resultado y lo almacenamos
            cache_dict[args] = funcion(*args)
        return cache_dict[args]  # Retorna el resultado ya almacenado
    return wrapper

# Aplicamos el decorador @cache a la función fibonacci_optimizado
@cache
def fibonacci_optimizado(n):
    """
    Función que calcula el n-ésimo número de Fibonacci de manera optimizada utilizando memoización.
    - n: El índice del número de Fibonacci que se desea calcular.
    
    Usando la recursión, se almacena el resultado para evitar cálculos repetidos.
    """
    if n <= 1:
        return n
    return fibonacci_optimizado(n-1) + fibonacci_optimizado(n-2)

# Ejemplo de uso del decorador 'cache'
# Este cálculo de Fibonacci estará optimizado debido a la memoización que evita cálculos repetidos
print("Fibonacci de 35:")
print(fibonacci_optimizado(35))  # El cálculo de Fibonacci de 35 será rápido debido a la caché

# Decorador de clase
def singleton(clase):
    """
    Este decorador asegura que solo haya una instancia de la clase decorada, implementando el patrón Singleton.
    - clase: La clase que se va a decorar.
    
    Devuelve una función que asegura que siempre se devuelva la misma instancia de la clase.
    """
    instancias = {}  # Diccionario que guarda las instancias de la clase
    def obtener_instancia(*args, **kwargs):
        """
        Función envolvente que controla la creación de la instancia de la clase.
        Si la instancia ya existe, se devuelve la existente; si no, se crea una nueva.
        """
        if clase not in instancias:
            # Si no hay ninguna instancia de esta clase, la creamos
            instancias[clase] = clase(*args, **kwargs)
        return instancias[clase]  # Devuelve siempre la misma instancia
    return obtener_instancia

# Aplicamos el decorador @singleton a la clase ClaseSingleton
@singleton
class ClaseSingleton:
    """
    Esta clase implementa el patrón Singleton, lo que asegura que solo haya una instancia de ella.
    """
    def __init__(self):
        """
        Constructor de la clase, inicializa el valor en None.
        """
        self.valor = None

# Ejemplo de uso del decorador 'singleton'
# Ambos objetos deberían ser la misma instancia, ya que el patrón Singleton asegura una única instancia.
instancia1 = ClaseSingleton()
instancia2 = ClaseSingleton()

# Verificamos si ambas instancias son la misma
print("¿Son la misma instancia?", instancia1 is instancia2)

