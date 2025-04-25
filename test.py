import unittest
import math
import time
from calc_1 import Calculator, ParserError, EvaluationError

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        self.calc_deg = Calculator()
        print("\nИнициализирован калькулятор")

    def test_basic_arithmetic(self):
        test_cases = [
            ("2+3", 5, "Сложение"),
            ("5-2", 3, "Вычитание"),
            ("3*4", 12, "Умножение"),
            ("10/2", 5, "Деление"),
            ("2^3", 8, "Возведение в степень"),
            ("2+3*4", 14, "Приоритет операций"),
            ("(2+3)*4", 20, "Скобки"),
            ("2*-3", -6, "Унарный минус"),
            ("8^(1/3)", 2, "Дробная степень")
        ]
        
        print("\n=== ТЕСТИРОВАНИЕ БАЗОВОЙ АРИФМЕТИКИ ===")
        for expr, expected, description in test_cases:
            with self.subTest(expr=expr):
                print(f"\nТест: {description}")
                print(f"Выражение: {expr}")
                print(f"Ожидаемый результат: {expected}")
                result = self.calc.calculate(expr)
                print(f"Фактический результат: {result}")
                self.assertAlmostEqual(result, expected)
                print("✅ Тест пройден")

    def test_floats_and_scientific(self):
        test_cases = [
            ("3.14", 3.14, "Десятичные дроби"),
            ("1e5", 1e5, "Научная нотация (положительная степень)"),
            ("1.25e+09", 1.25e+09, "Научная нотация с явным '+'"),
            ("-5", -5, "Отрицательные числа")
        ]
        
        print("\n=== ТЕСТИРОВАНИЕ ДРОБНЫХ ЧИСЕЛ И НАУЧНОЙ НОТАЦИИ ===")
        for expr, expected, description in test_cases:
            with self.subTest(expr=expr):
                print(f"\nТест: {description}")
                print(f"Выражение: {expr}")
                print(f"Ожидаемый результат: {expected}")
                result = self.calc.calculate(expr)
                print(f"Фактический результат: {result}")
                self.assertAlmostEqual(result, expected)
                print("✅ Тест пройден")

    def test_errors(self):
        error_cases = [
            ("1/0", EvaluationError, "Деление на ноль"),
            ("2/", ParserError, "Неполное выражение"),
            ("1 + (2 * 3", ParserError, "Незакрытая скобка")
        ]
        
        print("\n=== ТЕСТИРОВАНИЕ ОБРАБОТКИ ОШИБОК ===")
        for expr, error_type, description in error_cases:
            with self.subTest(expr=expr):
                print(f"\nТест: {description}")
                print(f"Выражение: {expr}")
                print(f"Ожидаемая ошибка: {error_type.__name__}")
                try:
                    result = self.calc.calculate(expr)
                    print(f"❌ Ошибка не возникла! Получен результат: {result}")
                    self.fail(f"Ожидалась ошибка {error_type.__name__}")
                except Exception as e:
                    print(f"Фактическая ошибка: {type(e).__name__}: {str(e)}")
                    self.assertIsInstance(e, error_type)
                    print("✅ Тест пройден")


class TestPerformance(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        print("\nИнициализирован калькулятор для тестов производительности")
    
    def test_long_expression(self):
        expr = "1" + "+1" * 1023
        expected = 1024
        
        print("\n=== ТЕСТ ПРОИЗВОДИТЕЛЬНОСТИ: ДЛИННОЕ ВЫРАЖЕНИЕ ===")
        print(f"Выражение: 1 + 1 + ... + 1 (1024 операции)")
        print(f"Ожидаемый результат: {expected}")
        
        start = time.time()
        result = self.calc.calculate(expr)
        end = time.time()
        duration = end - start
        
        print(f"Фактический результат: {result}")
        print(f"Время выполнения: {duration:.6f} сек")
        
        self.assertEqual(result, expected)
        self.assertLess(duration, 0.2)
        print("✅ Тест пройден")


if __name__ == '__main__':
    print("\n" + "="*60)
    print("=== НАЧАЛО ТЕСТИРОВАНИЯ КАЛЬКУЛЯТОРА ===".center(50))
    print("="*60)
    
    unittest.main(verbosity=2)
    
    print("\n" + "="*60)
    print("=== ТЕСТИРОВАНИЕ ЗАВЕРШЕНО ===".center(50))
    print("="*60)
