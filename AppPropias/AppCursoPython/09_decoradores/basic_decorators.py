# DECORADORES BÁSICOS EN PYTHON

# Decorador simple
# Un decorador es una función que toma otra función como argumento y la envuelve
# con comportamiento adicional sin modificar su código original.
# En este caso, `mi_decorador` es un decorador simple que imprime un mensaje antes y después de ejecutar la función decorada.

def mi_decorador(funcion):
    # La función `wrapper` envuelve la ejecución de la función decorada.
    def wrapper():
        print("Antes de la función")  # Se ejecuta antes de llamar a la función decorada.
        funcion()  # Se llama a la función original.
        print("Después de la función")  # Se ejecuta después de la función decorada.
    return wrapper  # Retornamos la función `wrapper` que es la versión decorada de la función original.

@mi_decorador  # Usamos el decorador `mi_decorador` para envolver la función `saludo`.
def saludo():
    print("¡Hola, mundo!")  # Esta es la función que será decorada.

# Decorador con argumentos
# Este decorador toma una función como argumento, pero también puede aceptar 
# argumentos adicionales que la función decorada podría requerir.

def decorador_con_argumentos(funcion):
    # La función `wrapper` permite que se pase cualquier argumento a la función decorada.
    def wrapper(*args, **kwargs):
        # Imprimimos el nombre de la función y sus argumentos antes de ejecutarla.
        print(f"Llamando a la función {funcion.__name__}")
        print(f"Argumentos: {args}")
        # Llamamos a la función original con los argumentos pasados.
        resultado = funcion(*args, **kwargs)
        print("Función completada")  # Mensaje después de la ejecución de la función.
        return resultado  # Retornamos el resultado de la función decorada.
    return wrapper  # Retornamos la función `wrapper`, que ahora es la versión decorada.

@decorador_con_argumentos  # Usamos el decorador `decorador_con_argumentos` para envolver la función `suma`.
def suma(a, b):
    return a + b  # Función que devuelve la suma de dos números.

# Decorador de tiempo de ejecución
# Este decorador mide el tiempo que tarda en ejecutarse una función.

import time  # Importamos el módulo `time` para medir el tiempo de ejecución.

def medir_tiempo(funcion):
    # La función `wrapper` envolviendo la función original.
    def wrapper(*args, **kwargs):
        # Guardamos el tiempo de inicio antes de ejecutar la función.
        inicio = time.time()
        # Llamamos a la función original.
        resultado = funcion(*args, **kwargs)
        # Guardamos el tiempo de finalización después de ejecutar la función.
        fin = time.time()
        # Imprimimos el tiempo de ejecución.
        print(f"Tiempo de ejecución de {funcion.__name__}: {fin - inicio} segundos")
        return resultado  # Retornamos el resultado de la función.
    return wrapper  # Retornamos la versión decorada de la función.

@medir_tiempo  # Usamos el decorador `medir_tiempo` para medir el tiempo que tarda en ejecutarse la función `fibonacci`.
def fibonacci(n):
    if n <= 1:  # Caso base para la secuencia de Fibonacci.
        return n
    # Llamada recursiva para calcular el número de Fibonacci en posición `n`.
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    # Ejemplo de decorador simple
    saludo()  # Llamamos a la función `saludo`, que imprimirá los mensajes antes y después de la función original.

    # Ejemplo de decorador con argumentos
    resultado = suma(5, 3)  # Llamamos a la función `suma`, que imprimirá sus argumentos y el mensaje de "función completada".
    print("Resultado de la suma:", resultado)  # Imprimimos el resultado de la suma.

    # Ejemplo de medición de tiempo
    print("Fibonacci de 30:")  # Imprimimos un mensaje antes de calcular el número de Fibonacci.
    fibonacci(30)  # Llamamos a la función `fibonacci` y se medirá su tiempo de ejecución.
