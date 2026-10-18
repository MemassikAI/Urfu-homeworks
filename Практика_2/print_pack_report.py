"""Отчёт о фасовке пирожных по 3 или 5 штук."""


def print_pack_report(amount: int) -> None:
    """Проверить числа от amount до 1 в порядке убывания."""
    if not isinstance(amount, int) or amount <= 1:
        raise ValueError("Нужно передать целое число больше единицы.")

    for number in range(amount, 0, -1):
        if number % 3 == 0 and number % 5 == 0:
            message = "расфасуем по 3 или по 5"
        elif number % 5 == 0:
            message = "расфасуем по 5"
        elif number % 3 == 0:
            message = "расфасуем по 3"
        else:
            message = "не заказываем!"
        print(f"{number} - {message}")


if __name__ == "__main__":
    print_pack_report(15)
