# FUNCIONES DE ORDEN SUPERIOR

# Función que devuelve otra función
def crear_multiplicador(factor):
    """Crear una función de multiplicación"""
    def multiplicar(x):
        return x * factor
    return multiplicar

# Función que acepta funciones como argumentos
def aplicar_operacion(funcion, lista):
    """Aplicar una función a todos los elementos de una lista"""
    return [funcion(x) for x in lista]

# Ejemplo de clasificación personalizada
def ordenar_personalizado():
    """Demostrar ordenamiento con función key"""
    estudiantes = [
        {"nombre": "Ana", "nota": 85},
        {"nombre": "Juan", "nota": 92},
        {"nombre": "María", "nota": 78}
    ]
    
    # Ordenar por nota
    print("Ordenados por nota:")
    print(sorted(estudiantes, key=lambda x: x['nota']))
    
    # Ordenar por longitud de nombre
    print("\nOrdenados por longitud de nombre:")
    print(sorted(estudiantes, key=lambda x: len(x['nombre'])))

# Decorador como función de orden superior
def registrar_llamada(funcion):
    """Decorador que cuenta llamadas a una función"""
    contador = 0
    def wrapper(*args, **kwargs):
        nonlocal contador
        contador += 1
        print(f"Llamada {contador} a {funcion.__name__}")
        return funcion(*args, **kwargs)
    return wrapper

@registrar_llamada
def sumar(a, b):
    """Función de suma simple"""
    return a + b

# Función que genera funciones
def crear_contador():
    """Crear una función de contador"""
    contador = 0
    def incrementar():
        nonlocal contador
        contador += 1
        return contador
    return incrementar

if __name__ == "__main__":
    # Demostrar multiplicador
    doble = crear_multiplicador(2)
    triple = crear_multiplicador(3)
    print("Doble de 5:", doble(5))
    print("Triple de 5:", triple(5))

    # Aplicar operación a lista
    numeros = [1, 2, 3, 4, 5]
    cuadrados = aplicar_operacion(lambda x: x**2, numeros)
    print("\nCuadrados:", cuadrados)

    # Ordenamiento personalizado
    ordenar_personalizado()

    # Decorador de conteo de llamadas
    print("\nLlamadas a la función sumar:")
    sumar(2, 3)
    sumar(4, 5)
    sumar(6, 7)

    # Contador
    print("\nContador:")
    contador = crear_contador()
    print(contador())  # 1
    print(contador())  # 2
    print(contador())  # 3

