"""
Guía de pruebas en Python con múltiples herramientas

Este archivo contiene ejemplos de pruebas usando varias bibliotecas de testing en Python:
- Unittest
- PyTest
- Doctest
- Nose2
"""

# Importamos las bibliotecas necesarias para cada tipo de prueba
import unittest  # Para pruebas con unittest
import doctest    # Para pruebas con doctest
import pytest     # Para pruebas con pytest
import nose2      # Para pruebas con nose2
from math import pi  # Para cálculos matemáticos


# -----------------------------------------------------------------------------
# FUNCIÓN PARA CALCULAR EL ÁREA DE UN CÍRCULO
# -----------------------------------------------------------------------------
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
    if not isinstance(r, (int, float)) or isinstance(r, bool):  # Validación del tipo
        raise TypeError("Solo números enteros o de coma flotante son válidos.")
    if r < 0:  # Validación del valor
        raise ValueError("No se permiten valores negativos.")
    
    return pi * (r ** 2)


# -----------------------------------------------------------------------------
# PRUEBAS CON UNITTEST
# -----------------------------------------------------------------------------
class TestArea(unittest.TestCase):
    """
    Clase de prueba para la función `area` utilizando unittest.
    """

    def test_area_con_valores_conocidos(self):
        """Verifica los resultados de área con valores conocidos."""
        self.assertAlmostEqual(area(1), pi)  # Radio = 1
        self.assertAlmostEqual(area(0), 0)   # Radio = 0
        self.assertAlmostEqual(area(3), pi * (3 ** 2))  # Radio = 3

    def test_negativos(self):
        """Verifica que se lance una excepción ValueError con radios negativos."""
        with self.assertRaises(ValueError):
            area(-1)

    def test_tipos_incompatibles(self):
        """Verifica que se lance una excepción TypeError con tipos incompatibles."""
        with self.assertRaises(TypeError):
            area(True)      # Booleano
        with self.assertRaises(TypeError):
            area('hola')    # Cadena
        with self.assertRaises(TypeError):
            area(2 + 3j)    # Número complejo


# -----------------------------------------------------------------------------
# PRUEBAS CON PYTEST
# -----------------------------------------------------------------------------
def suma(a, b):
    """Función simple para sumar dos números."""
    return a + b

def test_suma_pytest():
    """Prueba con pytest."""
    assert suma(2, 3) == 5  # Verifica que 2 + 3 sea igual a 5


# -----------------------------------------------------------------------------
# PRUEBAS CON DOCTEST
# -----------------------------------------------------------------------------
def cuadrado(n):
    """
    Calcula el cuadrado de un número.

    >>> cuadrado(2)
    4
    >>> cuadrado(3)
    9
    """
    return n * n


# Para ejecutar los doctests, usa: python -m doctest <nombre_del_archivo>.py


# -----------------------------------------------------------------------------
# PRUEBAS CON NOSE2
# -----------------------------------------------------------------------------
def test_suma_nose2():
    """Prueba usando Nose2."""
    assert suma(2, 3) == 5


# -----------------------------------------------------------------------------
# EJECUCIÓN DE LAS PRUEBAS
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    print("Ejecutando pruebas...")

    # Ejecutar pruebas con unittest
    print("\n--- Pruebas con unittest ---")
    unittest.main(exit=False)

    # Ejecutar pruebas con pytest
    print("\n--- Pruebas con pytest ---")
    pytest.main(['-v'])

    # Ejecutar pruebas con doctest
    print("\n--- Pruebas con doctest ---")
    doctest.testmod()

    # Ejecutar pruebas con nose2
    print("\n--- Pruebas con nose2 ---")
    nose2.main()

    print("\nTodas las pruebas han sido ejecutadas.")

