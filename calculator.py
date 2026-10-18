"""Базовые арифметические функции калькулятора."""


def add_numbers(a: float, b: float) -> float:
    """Вернуть сумму двух чисел."""
    return a + b


def divide(a: float, b: float) -> float:
    """Разделить первое число на второе."""
    if b == 0:
        raise ZeroDivisionError("На ноль делить нельзя.")
    return a / b


def subtract(a: float, b: float) -> float:
    """Вернуть разность двух чисел."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Вернуть произведение двух чисел."""
    return a * b
