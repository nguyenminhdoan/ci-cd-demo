import unittest
from calc import add, subtract

class TestCalcEdgeCases(unittest.TestCase):
    def test_add_very_large_numbers(self):
        large_num = 10**100
        result = add(large_num, large_num)
        self.assertEqual(result, 2 * large_num)
    
    def test_subtract_very_large_numbers(self):
        large_num = 10**100
        result = subtract(large_num, large_num)
        self.assertEqual(result, 0)
    
    def test_add_decimal_precision(self):
        result = add(0.1, 0.1)
        self.assertAlmostEqual(result, 0.2, places=15)
    
    def test_subtract_decimal_precision(self):
        result = subtract(1.0, 0.9)
        self.assertAlmostEqual(result, 0.1, places=15)
    
    def test_add_negative_zero(self):
        result = add(-0.0, 0.0)
        self.assertEqual(result, 0.0)
    
    def test_subtract_negative_zero(self):
        result = subtract(0.0, -0.0)
        self.assertEqual(result, 0.0)
    
    def test_mixed_int_float_operations(self):
        result_add = add(5, 2.5)
        result_subtract = subtract(10, 3.5)
        
        self.assertEqual(result_add, 7.5)
        self.assertEqual(result_subtract, 6.5)
    
    def test_string_representation(self):
        result = add(1, 2)
        self.assertEqual(str(result), '3')
        
        result = subtract(5, 3)
        self.assertEqual(str(result), '2')

if __name__ == '__main__':
    unittest.main()