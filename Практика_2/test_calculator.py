"""Тесты арифметических функций."""

import unittest

from calculator import add_numbers, divide


class TestCalculator(unittest.TestCase):
    """Проверки функций калькулятора."""

    def test_add_positive_numbers(self):
        """Проверить сложение положительных чисел."""
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        """Проверить сложение отрицательных чисел."""
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_add_zero(self):
        """Проверить сложение с нулём."""
        self.assertEqual(add_numbers(5, 0), 5)

    def test_divide(self):
        """Проверить деление на ненулевое число."""
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """Проверить обработку деления на ноль."""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()
