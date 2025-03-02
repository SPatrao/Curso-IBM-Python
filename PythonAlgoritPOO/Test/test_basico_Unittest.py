import unittest
from funciones import area
from math import pi

class TestArea(unittest.TestCase):
    """
    Clase de prueba para la función `area`.
    
    Utiliza el módulo unittest para verificar la correcta
    implementación de la función area al recibir varios inputs.
    """

    def test_area_con_valores_conocidos(self):
        """
        Verifica los resultados de área con valores de entrada conocidos.

        Se asegura de que el área calculada sea la esperada para 
        radios específicos.
        """
        # Comprobamos que el área para un radio de 1 sea igual a π
        self.assertAlmostEqual(area(1), pi)
        # Comprobamos que el área para un radio de 0 sea igual a 0
        self.assertAlmostEqual(area(0), 0)
        # Comprobamos que el área para un radio de 3 sea igual a π * (3^2)
        self.assertAlmostEqual(area(3), pi * (3 ** 2))
    
    def test_negativos(self):
        """
        Verifica que se lance una excepción ValueError al 
        intentar calcular el área con un radio negativo.
        """
        with self.assertRaises(ValueError):
            area(-1)
    
    def test_tipos_incompatibles(self):
        """
        Verifica que se lance una excepción TypeError al 
        intentar calcular el área con tipos de datos que no son 
        números.
        """
        with self.assertRaises(TypeError):
            area(True)      # Verifica un booleano
        with self.assertRaises(TypeError):
            area('hola')    # Verifica una cadena
        with self.assertRaises(TypeError):
            area(2 + 3j)    # Verifica un número complejo

# Para ejecutar las pruebas de este archivo
if __name__ == '__main__':
    unittest.main()

