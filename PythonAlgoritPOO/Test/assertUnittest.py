# Este archivo contiene ejemplos detallados sobre excepciones y declaraciones assert en Python.
# Cada ejemplo está completamente comentado para facilitar la comprensión.

# --------------------------------------------------------------------------------
# Introducción a las Excepciones y Declaraciones Assert
# --------------------------------------------------------------------------------

# Las declaraciones `assert` son una forma sencilla de realizar pruebas en Python.
# Si la condición evaluada es False, se lanza una excepción AssertionError.
# Esto es útil para validar condiciones críticas en el código.

# Ejemplo básico:
# assert condición, mensaje_de_error  # Si la condición es False, se muestra el mensaje_de_error.

# --------------------------------------------------------------------------------
# Ejemplo 1: Uso Básico de Assert
# --------------------------------------------------------------------------------

def dividir(a, b):
    """
    Divide dos números y asegura que el divisor no sea cero.

    Argumentos:
        a (float): Numerador.
        b (float): Denominador.

    Retorna:
        float: Resultado de la división.

    Lanza:
        AssertionError: Si el denominador es cero.
    """
    # Aseguramos que el denominador no sea cero antes de realizar la división.
    assert b != 0, "El denominador no puede ser cero."  # Si b es cero, se lanza una excepción.
    return a / b


# Testeo interactivo:
# print(dividir(10, 2))  # Funciona correctamente.
# print(dividir(10, 0))  # Lanza una excepción AssertionError con el mensaje personalizado.

# --------------------------------------------------------------------------------
# Ejemplo 2: Tipos de Comparaciones con Assert
# --------------------------------------------------------------------------------

# 1. Igualdad o Desigualdad
assert 5 == 5, "Los valores deben ser iguales."  # Éxito si los valores son iguales.
assert 5 != 3, "Los valores deben ser diferentes."  # Éxito si los valores son diferentes.

# 2. Tipo de Dato
x = 10
assert type(x) is int, "La variable x debe ser un entero."  # Verifica que x sea un entero.
assert isinstance(x, int), "La variable x debe ser un entero."  # Otra forma de verificar el tipo.

# 3. Contención en Iterables
lista = [1, 2, 3, 4]
assert 3 in lista, "El valor 3 debe estar en la lista."  # Verifica que 3 esté en la lista.
assert 5 not in lista, "El valor 5 no debe estar en la lista."  # Verifica que 5 no esté en la lista.

# 4. Comparaciones Numéricas
assert 5 > 4, "5 debe ser mayor que 4."
assert 2 < 4, "2 debe ser menor que 4."

# 5. Módulo
assert 4 % 2 == 0, "4 debe ser divisible entre 2."

# --------------------------------------------------------------------------------
# Ejemplo 3: Uso de Funciones any() y all()
# --------------------------------------------------------------------------------

# La función any() devuelve True si al menos uno de los elementos es verdadero.
numeros = [0, 1, 2, 3]
assert any(numeros), "Al menos un elemento en la lista debe ser verdadero."

# La función all() devuelve True solo si todos los elementos son verdaderos.
booleanos = [True, True, True]
assert all(booleanos), "Todos los elementos en la lista deben ser verdaderos."

# --------------------------------------------------------------------------------
# Ejemplo 4: Combinación de Condiciones con and/or
# --------------------------------------------------------------------------------

# Combinación de múltiples condiciones usando and/or.
condicion1 = 5 == 5
condicion2 = 10 == 10
assert condicion1 and condicion2, "Ambas condiciones deben ser verdaderas."

condicion3 = 5 == 3
assert condicion1 or condicion3, "Al menos una de las condiciones debe ser verdadera."

# --------------------------------------------------------------------------------
# Ejemplo 5: Validación de Objetos Personalizados
# --------------------------------------------------------------------------------

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear una instancia de Persona.
persona = Persona("Juan", 30)

# Validar que el objeto sea de tipo Persona.
assert type(persona).__name__ == "Persona", "El objeto debe ser una instancia de Persona."

# Validar atributos del objeto.
assert persona.nombre == "Juan", "El nombre debe ser 'Juan'."
assert persona.edad > 0, "La edad debe ser mayor que cero."

# --------------------------------------------------------------------------------
# Ejemplo 6: Validación de Iterables
# --------------------------------------------------------------------------------

from collections.abc import Iterable

# Verificar si una variable es iterable.
iterable = [1, 2, 3]
assert isinstance(iterable, Iterable), "La variable debe ser iterable."

no_iterable = 123
assert not isinstance(no_iterable, Iterable), "La variable no debe ser iterable."

# --------------------------------------------------------------------------------
# Ejemplo 7: Pruebas con UnitTest
# --------------------------------------------------------------------------------

import unittest

class TestEjemplos(unittest.TestCase):
    def test_division(self):
        """Testea la función de división."""
        self.assertEqual(dividir(10, 2), 5)  # Verifica que 10 / 2 sea igual a 5.
        with self.assertRaises(AssertionError):  # Verifica que se lance una excepción cuando b es 0.
            dividir(10, 0)

    def test_tipos(self):
        """Testea comparaciones de tipos."""
        x = 10
        self.assertIsInstance(x, int)  # Verifica que x sea un entero.
        self.assertNotIsInstance(x, str)  # Verifica que x no sea una cadena.

    def test_contencion(self):
        """Testea contención en iterables."""
        lista = [1, 2, 3, 4]
        self.assertIn(3, lista)  # Verifica que 3 esté en la lista.
        self.assertNotIn(5, lista)  # Verifica que 5 no esté en la lista.

    def test_numeros(self):
        """Testea comparaciones numéricas."""
        self.assertGreater(5, 4)  # Verifica que 5 sea mayor que 4.
        self.assertLess(2, 4)  # Verifica que 2 sea menor que 4.

if __name__ == "__main__":
    unittest.main()