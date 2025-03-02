###Recicle###
import unittest
from unittest.mock import Mock, patch
import recycling

class TestRecycling(unittest.TestCase):
    def test_max_values(self):
        example_data = [1, 3, 5, 0, 2, 6, 3, 6]
        max_data = recycling.max_recycling(example_data)
        self.assertEqual(max_data.crates, 6)
        self.assertEqual(max_data.houses, [5, 7])

if __name__ == '__main__':
    unittest.main()