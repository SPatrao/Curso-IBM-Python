# GENERADORES AVANZADOS EN PYTHON

# Generador con múltiples yields
# Un generador es una función que utiliza la palabra clave `yield` para devolver un valor
# en lugar de usar `return`. Esto permite que el generador produzca una secuencia de valores
# a lo largo del tiempo, en lugar de generar todos los valores de inmediato.
# Aquí se utiliza el generador `generador_multipaso`, que produce una secuencia con tres pasos distintos.

def generador_multipaso():
    """Generador con múltiples pasos"""
    yield "Inicio"  # Primer valor que se genera en el generador.
    yield "Paso intermedio"  # Segundo valor que se genera.
    yield "Final"  # Último valor que se genera.

# Generador con estado
# En este caso, estamos creando una clase `GeneradorEstado` que funciona como un generador,
# pero tiene un estado interno que se mantiene entre las iteraciones. La clase también define
# los métodos especiales `__iter__` y `__next__`, lo que permite que la clase sea iterable como un generador.

class GeneradorEstado:
    def __init__(self, limite):
        self.limite = limite  # Establece un límite hasta el cual se generarán los valores.
        self.actual = 0  # Inicializa el estado del generador.

    def __iter__(self):
        return self  # El método __iter__ devuelve la propia instancia como iterable.

    def __next__(self):
        if self.actual >= self.limite:  # Cuando el valor actual es igual o mayor que el límite, se lanza StopIteration.
            raise StopIteration  # Excepción que indica que el generador ha finalizado.
        resultado = self.actual  # El valor actual se devuelve.
        self.actual += 1  # Se incrementa el valor actual.
        return resultado  # Retorna el valor generado.

# Generador con send() y throw()
# Este generador es interactivo, ya que puede recibir valores a través de `send()`.
# También maneja excepciones usando `throw()`, lo que lo convierte en un generador más avanzado.

def generador_interactivo():
    """Generador que acepta valores y maneja excepciones"""
    try:
        while True:
            x = yield  # Espera que se le envíe un valor con send().
            print("Valor recibido:", x)  # Imprime el valor recibido.
    except GeneratorExit:
        print("Generador cerrado")  # Mensaje cuando el generador se cierra.

# Composición de generadores
# Los generadores pueden ser combinados entre sí. Un generador puede ser usado como entrada
# para otro generador, formando una cadena de procesamiento.

def generador_fibonacci():
    """Generador de secuencia de Fibonacci"""
    a, b = 0, 1  # Inicializa los dos primeros valores de la secuencia de Fibonacci.
    while True:  # El generador produce valores indefinidamente.
        yield a  # Retorna el valor actual de la secuencia.
        a, b = b, a + b  # Actualiza los valores de `a` y `b` para la siguiente iteración.

def filtrar_pares(generador):
    """Filtrar números pares de un generador"""
    for numero in generador:  # Itera sobre los valores generados por otro generador.
        if numero % 2 == 0:  # Si el número es par.
            yield numero  # Retorna el número par.

# Generador con corrutinas
# Una corrutina es similar a un generador, pero se utiliza para realizar tareas como
# la suma de valores de manera continua. Se puede enviar y recibir valores, lo que la
# hace útil para situaciones donde el control del flujo es más flexible.

def corrutina_suma():
    """Corrutina que suma valores"""
    total = 0  # Inicializa la variable para mantener la suma total.
    while True:  # La corrutina seguirá corriendo hasta que se cierre.
        valor = yield total  # Espera un valor para agregar a la suma.
        if valor is None:  # Si el valor es None, la corrutina se detendrá.
            break
        total += valor  # Suma el valor recibido al total.

if __name__ == "__main__":
    # Ejemplo de generador multipaso
    print("Generador multipaso:")
    for paso in generador_multipaso():
        print(paso)  # Imprime cada valor producido por el generador `generador_multipaso`.

    # Ejemplo de generador con estado
    print("\nGenerador con estado:")
    generador_estado = GeneradorEstado(5)  # Crea una instancia de `GeneradorEstado` con un límite de 5.
    print(list(generador_estado))  # Convierte el generador en una lista e imprime los valores generados.

    # Ejemplo de generador interactivo
    print("\nGenerador interactivo:")
    gen = generador_interactivo()  # Crea una instancia del generador interactivo.
    next(gen)  # Inicia el generador. `yield` se encuentra y el generador espera un valor.
    gen.send(10)  # Envía el valor 10 al generador.
    gen.send(20)  # Envía el valor 20 al generador.
    gen.close()  # Cierra el generador y se maneja la excepción `GeneratorExit`.

    # Composición de generadores
    print("\nFibonacci pares:")
    fib_gen = generador_fibonacci()  # Crea un generador de Fibonacci.
    pares_fib = list(filtrar_pares(fib_gen))[:10]  # Filtra los primeros 10 números pares de Fibonacci.
    print(pares_fib)  # Imprime los primeros 10 números pares de la secuencia de Fibonacci.

    # Corrutina de suma
    print("\nCorrutina de suma:")
    suma_cor = corrutina_suma()  # Crea una instancia de la corrutina.
    next(suma_cor)  # Inicia la corrutina.
    print(suma_cor.send(10))  # Envía 10 a la corrutina y obtiene la suma parcial.
    print(suma_cor.send(20))  # Envía 20 a la corrutina y obtiene la suma parcial.
    print(suma_cor.send(30))  # Envía 30 a la corrutina y obtiene la suma total.
    suma_cor.close()  # Cierra la corrutina.
