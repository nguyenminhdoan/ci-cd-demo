import unittest
from calc import add, subtract

class TestAdvancedCalc(unittest.TestCase):
    def test_add_multiple_operations(self):
        result = add(add(1, 2), add(3, 4))
        self.assertEqual(result, 10)
    
    def test_subtract_multiple_operations(self):
        result = subtract(subtract(10, 2), subtract(5, 3))
        self.assertEqual(result, 6)
    
    def test_mixed_operations(self):
        result = add(subtract(10, 3), add(2, 1))
        self.assertEqual(result, 10)
    
    def test_chain_operations(self):
        result = 0
        for i in range(1, 6):
            result = add(result, i)
        self.assertEqual(result, 15)
    
    def test_boundary_values(self):
        self.assertEqual(add(float('inf'), 1), float('inf'))
        self.assertEqual(subtract(float('inf'), 1), float('inf'))
        self.assertTrue(str(add(float('nan'), 1)) == 'nan')
    
    def test_type_consistency(self):
        self.assertIsInstance(add(1, 2), int)
        self.assertIsInstance(add(1.0, 2.0), float)
        self.assertIsInstance(subtract(5, 3), int)
        self.assertIsInstance(subtract(5.0, 3.0), float)

if __name__ == '__main__':
    unittest.main()