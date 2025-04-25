import unittest
import math
import time
from calc import Calculator, ParserError, EvaluationError

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        self.calc_deg = Calculator()

    def test_basic_arithmetic(self):
        test_cases = [
            ("2+3", 5),
            ("5-2", 3),
            ("3*4", 12),
            ("10/2", 5),
            ("2+3*4", 14),
            ("2*-3", -6)
        ]
        
        for expr, expected in test_cases:
            with self.subTest(expr=expr):
                result = self.calc.calculate(expr)
                print(f"\nТест: {expr} = {expected}")
                print(f"Результат: {result}")
                self.assertAlmostEqual(result, expected)

    def test_floats_and_scientific(self):
        test_cases = [
            ("3.14", 3.14),
            ("1e5", 1e5),
            ("1.25e+09", 1.25e+09),
            ("-5", -5)
        ]
        
        for expr, expected in test_cases:
            with self.subTest(expr=expr):
                result = self.calc.calculate(expr)
                print(f"\nТест: {expr} = {expected}")
                print(f"Результат: {result}")
                self.assertAlmostEqual(result, expected)

    def test_errors(self):
        error_cases = [
            ("1/0", EvaluationError),
            ("2/", ParserError)
        ]
        
        for expr, error_type in error_cases:
            with self.subTest(expr=expr):
                print(f"\nТест ошибки: {expr} → ожидается {error_type.__name__}")
                with self.assertRaises(error_type):
                    self.calc.calculate(expr)
                print(f"Получена ожидаемая ошибка: {error_type.__name__}")


class TestPerformance(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_long_expression(self):
        expr = "1" + "+1" * 1023
        expected = 1024
        
        print(f"\nТест производительности: длинное выражение (1024 операции)")
        start = time.time()
        result = self.calc.calculate(expr)
        end = time.time()
        duration = end - start
        
        print(f"Результат: {result} (ожидается {expected})")
        print(f"Время выполнения: {duration:.6f} сек")
        
        self.assertEqual(result, expected)
        self.assertLess(duration, 0.2)
    
    def test_large_numbers(self):
        expr = "1e300 + 1e30000"
        expected = 1e300 + 1e30000
        
        print(f"\nТест производительности: очень большие числа")
        start = time.time()
        result = self.calc.calculate(expr)
        end = time.time()
        duration = end - start
        
        print(f"Результат: {result} (ожидается {expected})")
        print(f"Время выполнения: {duration:.6f} сек")
        
        self.assertAlmostEqual(result, expected)
        self.assertLess(duration, 0.1)


if __name__ == '__main__':
    print("\n=== Начало тестирования калькулятора ===")
    unittest.main(verbosity=2)
    print("\n=== Тестирование завершено ===")