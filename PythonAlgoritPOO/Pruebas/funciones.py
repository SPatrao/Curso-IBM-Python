from math import pi

def area(r):
    """
    Calcula el área de un círculo dado su radio.

    Args:
        r (int o float): El radio del círculo.

    Returns:
        float: El área del círculo.

    Raises:
        ValueError: Si el radio es un número negativo.
        TypeError: Si el tipo del radio no es un número entero o de punto flotante.
    
    Ejemplos:
        >>> area(0)
        0.0
        >>> area(1)
        3.141592653589793
        >>> area(2)
        12.566370614359172
    """
    # Verificamos si el tipo de r es correcto
    if type(r) not in [float, int]:
        raise TypeError("Solo números enteros o de coma flotante.")
    # Verificamos si el radio es negativo
    if r < 0:
        raise ValueError("No se permiten valores negativos")
    
    # Cálculo del área usando la fórmula: área = π * r^2
    areaC = pi * (r ** 2)
    return areaC

