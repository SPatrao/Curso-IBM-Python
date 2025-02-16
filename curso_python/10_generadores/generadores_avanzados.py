# GENERADORES AVANZADOS EN PYTHON

# Generador con múltiples yields
def generador_multipaso():
    """Generador con múltiples pasos"""
    yield "Inicio"
    yield "Paso intermedio"
    yield "Final"

# Generador con estado
class GeneradorEstado:
    def __init__(self, limite):
        self.limite = limite
        self.actual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual >= self.limite:
            raise StopIteration
        resultado = self.actual
        self.actual += 1
        return resultado

# Generador con send() y throw()
def generador_interactivo():
    """Generador que acepta valores y maneja excepciones"""
    try:
        while True:
            x = yield
            print("Valor recibido:", x)
    except GeneratorExit:
        print("Generador cerrado")

# Composición de generadores
def generador_fibonacci():
    """Generador de secuencia de Fibonacci"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def filtrar_pares(generador):
    """Filtrar números pares de un generador"""
    for numero in generador:
        if numero % 2 == 0:
            yield numero

# Generador con corrutinas
def corrutina_suma():
    """Corrutina que suma valores"""
    total = 0
    while True:
        valor = yield total
        if valor is None:
            break
        total += valor

if __name__ == "__main__":
    # Ejemplo de generador multipaso
    print("Generador multipaso:")
    for paso in generador_multipaso():
        print(paso)

    # Ejemplo de generador con estado
    print("\nGenerador con estado:")
    generador_estado = GeneradorEstado(5)
    print(list(generador_estado))

    # Ejemplo de generador interactivo
    print("\nGenerador interactivo:")
    gen = generador_interactivo()
    next(gen)  # Iniciar generador
    gen.send(10)
    gen.send(20)
    gen.close()

    # Composición de generadores
    print("\nFibonacci pares:")
    fib_gen = generador_fibonacci()
    pares_fib = list(filtrar_pares(fib_gen))[:10]
    print(pares_fib)

    # Corrutina de suma
    print("\nCorrutina de suma:")
    suma_cor = corrutina_suma()
    next(suma_cor)  # Iniciar corrutina
    print(suma_cor.send(10))
    print(suma_cor.send(20))
    print(suma_cor.send(30))
    suma_cor.close()

