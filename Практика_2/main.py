"""Запуск примеров работы калькулятора."""

import numpy as np

from calculator import add_numbers, divide, multiply, subtract


def main() -> None:
    """Показать результаты арифметических операций и версию NumPy."""
    print("2 + 3 =", add_numbers(2, 3))
    print("7 - 4 =", subtract(7, 4))
    print("3 * 4 =", multiply(3, 4))
    print("8 / 2 =", divide(8, 2))
    print("NumPy version:", np.__version__)


if __name__ == "__main__":
    main()
