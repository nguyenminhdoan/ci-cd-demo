import unittest
import time
from calc import add, subtract

class TestCalcPerformance(unittest.TestCase):
    def test_add_performance(self):
        start_time = time.time()
        
        for i in range(1000):
            result = add(i, i + 1)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        self.assertLess(execution_time, 0.1, "Add function should complete 1000 operations in less than 0.1 seconds")
    
    def test_subtract_performance(self):
        start_time = time.time()
        
        for i in range(1000):
            result = subtract(i + 1, i)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        self.assertLess(execution_time, 0.1, "Subtract function should complete 1000 operations in less than 0.1 seconds")
    
    def test_large_numbers(self):
        large_num1 = 999999999
        large_num2 = 111111111
        
        result_add = add(large_num1, large_num2)
        result_subtract = subtract(large_num1, large_num2)
        
        self.assertEqual(result_add, 1111111110)
        self.assertEqual(result_subtract, 888888888)
    
    def test_float_precision(self):
        result_add = add(0.1, 0.2)
        result_subtract = subtract(0.3, 0.1)
        
        self.assertAlmostEqual(result_add, 0.3, places=10)
        self.assertAlmostEqual(result_subtract, 0.2, places=10)

if __name__ == '__main__':
    unittest.main()