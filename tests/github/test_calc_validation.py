import unittest
from calc import add, subtract

class TestCalcValidation(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(1, 1), 2)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-10, 10), 0)
    
    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 0), 0)
    
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(5, 5), 0)
    
    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-3, -5), 2)
    
    def test_subtract_zero(self):
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(0, 0), 0)

if __name__ == '__main__':
    unittest.main()