# Este archivo contiene tres ejemplos completos con explicaciones detalladas.
# Los tres ejemplos son: Binario a Decimal, Camel Case y Reciclaje.
# Se han agregado comentarios para que sea útil tanto para principiantes como para usuarios avanzados.

# --------------------------------------------------------------------------------
# Ejemplo 1: Binario a Decimal
# --------------------------------------------------------------------------------

def decimal(binary_str):
    """
    Convierte una cadena binaria (compuesta solo por 0s y 1s) en su equivalente decimal.
    Si la cadena contiene caracteres distintos de 0 y 1, lanza un ValueError.

    Argumentos:
        binary_str (str): Cadena binaria a convertir.

    Retorna:
        int: Valor decimal equivalente.

    Ejemplo:
        >>> decimal('101')
        5
    """
    # Elimina todos los '0' y '1' de la cadena. Si queda algo, significa que hay caracteres inválidos.
    remove_0_and_1 = binary_str.replace('0', '').replace('1', '')
    if len(remove_0_and_1) > 0:
        raise ValueError('La cadena binaria de entrada solo puede contener 0 y 1')

    # Inicializa variables para calcular el valor decimal.
    place = 1  # Representa la posición actual en la cadena binaria (comienza desde 2^0).
    dec = 0    # Variable para almacenar el resultado decimal.

    # Itera sobre la cadena binaria desde el final hasta el principio.
    for bit in binary_str[::-1]:
        if bit == '1':  # Si el dígito es '1', suma el valor posicional.
            dec += place
        place *= 2  # Multiplica la posición por 2 para el siguiente valor de posición.

    return dec


# Testeo del ejemplo 1 usando unittest
import unittest

class TestBinaryToDecimal(unittest.TestCase):
    def test_binario_decimal_con_entradas_validas(self):
        """Testea conversiones válidas de binario a decimal."""
        for d in range(100):  # Testea números del 0 al 99.
            binary = bin(d)[2:]  # Convierte a binario sin el prefijo '0b'.
            dec_output = decimal(binary)
            self.assertEqual(d, dec_output)

    def test_binario_decimal_con_entradas_invalidas(self):
        """Testea entradas inválidas que deben lanzar ValueError."""
        invalid_inputs = ['123456', '101010012', 'abc', '@#$%$%^%^&']
        for invalid_input in invalid_inputs:
            with self.assertRaises(ValueError):
                decimal(invalid_input)


# --------------------------------------------------------------------------------
# Ejemplo 2: Camel Case
# --------------------------------------------------------------------------------

import re

def capitalize(word):
    """
    Convierte una palabra para que tenga la primera letra en mayúscula y el resto en minúsculas.

    Argumentos:
        word (str): Palabra a capitalizar.

    Retorna:
        str: Palabra capitalizada.

    Ejemplo:
        >>> capitalize('hola')
        'Hola'
    """
    return word[0:1].upper() + word[1:].lower()

def lowercase(word):
    """
    Convierte una palabra a minúsculas.

    Argumentos:
        word (str): Palabra a convertir.

    Retorna:
        str: Palabra en minúsculas.

    Ejemplo:
        >>> lowercase('HOLA')
        'hola'
    """
    return word.lower()

def camel_case(sentence):
    """
    Convierte una frase en formato "camelCase".

    Argumentos:
        sentence (str): Frase a convertir.

    Retorna:
        str: Frase en formato camelCase.

    Ejemplo:
        >>> camel_case('hola mundo')
        'holaMundo'
    """
    # Elimina espacios múltiples y espacios alrededor.
    remove_multiple_spaces = re.sub(r'\s+', '', sentence)
    remove_surrounding_space = remove_multiple_spaces.strip()

    words = remove_surrounding_space.split(' ')  # Divide la frase en palabras.
    first_word = lowercase(words[0])  # Pasa la primera palabra a minúsculas.
    capitalized_words = [capitalize(word) for word in words[1:]]  # Capitaliza las demás palabras.

    camel_cased_words = [first_word] + capitalized_words  # Une todas las palabras.
    camel_cased_sentence = ''.join(camel_cased_words)  # Convierte la lista en una cadena.

    return camel_cased_sentence

def main():
    """Función principal para interactuar con el usuario."""
    sentence = input('Introduzca la frase:')
    camelcased = camel_case(sentence)
    print(camelcased)


# Testeo del ejemplo 2 usando unittest
class TestCamelCase(unittest.TestCase):
    def test_capitalize(self):
        """Testea la función capitalize."""
        input_words = ['abc', 'ABC', 'aBC', 'ABc']
        capitalized = 'Abc'
        for word in input_words:
            self.assertEqual(capitalized, capitalize(word))

    def test_lower(self):
        """Testea la función lowercase."""
        input_words = ['abc', 'ABC', 'aBC', 'ABc']
        lower = 'abc'
        for word in input_words:
            self.assertEqual(lower, lowercase(word))

    def test_camel_case_single_words(self):
        """Testea conversiones simples de palabras individuales."""
        input_and_expected_outputs = {
            'hello': 'hello',
            'Hello': 'hello',
            'Thisisaverylongwordlalalalalalalalalalala': 'thisisaverylongwordlalalalalalalalalalala',
            'a': 'a'
        }
        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel_case(input_val))


# --------------------------------------------------------------------------------
# Ejemplo 3: Reciclaje
# --------------------------------------------------------------------------------

from collections import namedtuple

CrateData = namedtuple('CrateData', ['houses', 'crates'])

def max_recycling(crates):
    """
    Encuentra la casa con más reciclaje y el número de cajas correspondiente.

    Argumentos:
        crates (list): Lista con el número de cajas de reciclaje por casa.

    Retorna:
        CrateData: Tupla con las casas con más reciclaje y el número de cajas.

    Ejemplo:
        >>> max_recycling([1, 3, 5, 0, 2, 6, 3, 6])
        CrateData(houses=[5, 7], crates=6)
    """
    if crates is None or len(crates) == 0:
        raise ValueError('Se requiere una lista con al menos un elemento.')

    max_houses = []
    max_crates = crates[0]

    for crate in crates:
        if crate > max_crates:
            max_crates = crate

    for house, crates in zip(range(len(crates)), crates):
        if crates == max_crates:
            max_houses.append(house)

    return CrateData(max_houses, max_crates)

def min_recycling(crates):
    """
    Encuentra la casa con menos reciclaje y el número de cajas correspondiente.

    Argumentos:
        crates (list): Lista con el número de cajas de reciclaje por casa.

    Retorna:
        CrateData: Tupla con las casas con menos reciclaje y el número de cajas.

    Ejemplo:
        >>> min_recycling([1, 0, 3, 5, 0, 2, 6])
        CrateData(houses=[1, 4], crates=0)
    """
    if crates is None or len(crates) == 0:
        raise ValueError('Se requiere una lista con al menos un elemento.')

    min_houses = []
    min_crates = crates[0]

    for crate in crates:
        if crate < min_crates:
            min_crates = crate

    for house, crates in zip(range(len(crates)), crates):
        if crates == min_crates:
            min_houses.append(house)

    return CrateData(min_houses, min_crates)

def total_crates(crates):
    """
    Calcula el total de cajas de reciclaje.

    Argumentos:
        crates (list): Lista con el número de cajas de reciclaje por casa.

    Retorna:
        int: Total de cajas de reciclaje.

    Ejemplo:
        >>> total_crates([1, 3, 5, 0, 2, 6])
        17
    """
    total = 0
    for crate in crates:
        total += crate
    return total

def positive_int_input(question):
    """
    Solicita al usuario un número entero positivo.

    Argumentos:
        question (str): Pregunta a mostrar al usuario.

    Retorna:
        int: Número entero positivo ingresado por el usuario.
    """
    while True:
        try:
            integer = int(input(question))
            if integer >= 0:
                return integer
            else:
                print('Por favor, ingrese un número entero positivo.')
        except ValueError:
            print('Por favor, ingrese un número entero positivo.')

def main():
    """Función principal para interactuar con el usuario."""
    print('Programa de camión de reciclaje')
    houses = positive_int_input('¿Cuántas casas? ')
    crates = []
    for house in range(houses):
        crates.append(positive_int_input(f'Ingrese el número de cajas para la casa {house}: '))

    maximums = max_recycling(crates)
    minimums = min_recycling(crates)
    total = total_crates(crates)

    print(f'El número total de cajas en la calle es {total}')
    print(f'La máxima cantidad de cajas de cualquier casa es {maximums.crates}')
    print(f'La casa(s) con más reciclaje es {maximums.houses}')
    print(f'La mínima cantidad de cajas de cualquier casa es {minimums.crates}')
    print(f'La casa(s) con menos reciclaje es {minimums.houses}')


# Testeo del ejemplo 3 usando unittest
class TestRecycling(unittest.TestCase):
    def test_max_values(self):
        """Testea la función max_recycling."""
        example_data = [1, 3, 5, 0, 2, 6, 3, 6]
        max_data = max_recycling(example_data)
        self.assertEqual(max_data.crates, 6)
        self.assertEqual(max_data.houses, [5, 7])

    def test_min_values(self):
        """Testea la función min_recycling."""
        example_data = [1, 0, 3, 5, 0, 2, 6]
        min_data = min_recycling(example_data)
        self.assertEqual(min_data.crates, 0)
        self.assertEqual(min_data.houses, [1, 4])

    def test_total(self):
        """Testea la función total_crates."""
        example_data = [1, 3, 5, 0, 2, 6]
        self.assertEqual(total_crates(example_data), 17)


# Ejecución de los tests
if __name__ == '__main__':
    unittest.main()