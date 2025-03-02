###Camel Case###
import unittest
from unittest.mock import patch
import camel

class TestCamelCase(unittest.TestCase):
    def test_capitalize(self):
        input_words = ['abc', 'ABC', 'aBC', 'ABc']
        capitalized = 'Abc'
        for word in input_words:
            self.assertEqual(capitalized, camel.capitalize(word))

    def test_camel_case_single_words(self):
        input_and_expected_outputs = {
            'hello': 'hello',
            'Hello': 'hello',
            'Thisisaverylongwordlalalalalalalalalalala': 'thisisaverylongwordlalalalalalalalalalala',
            'a': 'a'
        }
        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

if __name__ == '__main__':
    unittest.main()