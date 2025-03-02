###Binario a Decimal###
import unittest
import bin_to_dec

class TestBinaryToDecimal(unittest.TestCase):
    def test_binario_decimal_con_entradas_validas(self):
        # Testea conversiones válidas
        for d in range(100):  # Testea números del 0 al 99
            binary = bin(d)[2:]  # Convierte a binario sin el prefijo '0b'
            dec_output = bin_to_dec.decimal(binary)
            self.assertEqual(d, dec_output)

    def test_binario_decimal_con_entradas_invalidas(self):
        # Testea entradas inválidas
        invalid = ['123456', '101010012', 'abc', '@#$%$%^%^&']
        for invalid_input in invalid:
            with self.assertRaises(ValueError):
                bin_to_dec.decimal(invalid_input)

if __name__ == '__main__':
    unittest.main()