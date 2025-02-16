# FUNCIONES DE ORDEN SUPERIOR

# Función que devuelve otra función
def crear_multiplicador(factor):
    """Esta función toma un argumento 'factor' y devuelve una nueva función 
    que multiplica su argumento por ese 'factor'. Esta es una función de orden superior 
    porque devuelve otra función.

    Ejemplo:
        doble = crear_multiplicador(2)  # Crea una función que multiplica por 2
        doble(5)  # Devuelve 10
    """
    # Definimos una función interna 'multiplicar' que usará el 'factor' de la función externa.
    def multiplicar(x):
        return x * factor
    # Retornamos la función 'multiplicar' para que pueda ser utilizada
    return multiplicar

# Función que acepta funciones como argumentos
def aplicar_operacion(funcion, lista):
    """Esta función acepta una función y una lista, y aplica la función a cada 
    elemento de la lista. La función es pasada como argumento y se aplica a todos 
    los elementos de la lista utilizando una comprensión de listas.

    Ejemplo:
        aplicar_operacion(lambda x: x**2, [1, 2, 3])  # Devuelve [1, 4, 9]
    """
    return [funcion(x) for x in lista]  # Aplica la función a cada elemento de la lista

# Ejemplo de clasificación personalizada
def ordenar_personalizado():
    """Demuestra cómo utilizar la función 'sorted' con el parámetro 'key' para ordenar 
    listas según una propiedad personalizada. En este caso, se ordena una lista de 
    diccionarios primero por la nota y luego por la longitud del nombre.

    Ejemplo:
        ordenar_personalizado()  # Muestra estudiantes ordenados por nota y longitud de nombre
    """
    estudiantes = [
        {"nombre": "Ana", "nota": 85},
        {"nombre": "Juan", "nota": 92},
        {"nombre": "María", "nota": 78}
    ]
    
    # Ordenar por la nota de los estudiantes
    print("Ordenados por nota:")
    print(sorted(estudiantes, key=lambda x: x['nota']))
    
    # Ordenar por la longitud del nombre de los estudiantes
    print("\nOrdenados por longitud de nombre:")
    print(sorted(estudiantes, key=lambda x: len(x['nombre'])))

# Decorador como función de orden superior
def registrar_llamada(funcion):
    """Un decorador es una función que modifica el comportamiento de otra función. 
    Este decorador cuenta cuántas veces ha sido llamada una función y muestra un mensaje
    cada vez que se ejecuta.

    Ejemplo:
        @registrar_llamada
        def sumar(a, b):  # Esta función será decorada
            return a + b
    """
    contador = 0  # Inicializamos un contador para las llamadas
    def wrapper(*args, **kwargs):
        """Función envolvente que se ejecuta cada vez que la función original es llamada"""
        nonlocal contador  # Utilizamos 'nonlocal' para modificar la variable 'contador' externa
        contador += 1
        print(f"Llamada {contador} a {funcion.__name__}")  # Imprimimos cuántas veces se ha llamado
        return funcion(*args, **kwargs)  # Llamamos a la función original con los argumentos dados
    return wrapper  # Devolvemos la función envolvente

# Decoramos la función 'sumar' con el decorador 'registrar_llamada'
@registrar_llamada
def sumar(a, b):
    """Función que devuelve la suma de dos números"""
    return a + b

# Función que genera funciones
def crear_contador():
    """Esta función crea y devuelve una función que actúa como un contador. 
    Cada vez que se llama, incrementa un contador interno y devuelve su valor actualizado.

    Ejemplo:
        contador = crear_contador()
        contador()  # Devuelve 1
        contador()  # Devuelve 2
    """
    contador = 0  # Inicializamos un contador local
    def incrementar():
        """Incrementa el contador y devuelve su valor"""
        nonlocal contador  # Modificamos la variable 'contador' de la función externa
        contador += 1
        return contador  # Devolvemos el nuevo valor del contador
    return incrementar  # Devolvemos la función 'incrementar', que ahora actúa como un contador

if __name__ == "__main__":
    # Demostración del uso de 'crear_multiplicador'
    doble = crear_multiplicador(2)  # Creamos una función que multiplica por 2
    triple = crear_multiplicador(3)  # Creamos una función que multiplica por 3
    print("Doble de 5:", doble(5))  # Muestra 10
    print("Triple de 5:", triple(5))  # Muestra 15

    # Aplicar operación (cuadrados) a una lista de números
    numeros = [1, 2, 3, 4, 5]
    cuadrados = aplicar_operacion(lambda x: x**2, numeros)  # Cuadrados de los números
    print("\nCuadrados:", cuadrados)  # Muestra [1, 4, 9, 16, 25]

    # Ordenar estudiantes por nota y longitud de nombre
    ordenar_personalizado()  # Muestra estudiantes ordenados por sus notas y longitud de nombre

    # Ejemplo de función decorada
    print("\nLlamadas a la función sumar:")
    sumar(2, 3)  # Llamada 1 a la función 'sumar'
    sumar(4, 5)  # Llamada 2 a la función 'sumar'
    sumar(6, 7)  # Llamada 3 a la función 'sumar'

    # Ejemplo de contador
    print("\nContador:")
    contador = crear_contador()  # Creamos una nueva instancia de contador
    print(contador())  # Devuelve 1
    print(contador())  # Devuelve 2
    print(contador())  # Devuelve 3
