"""Генератор паролей с настройками символов."""

import secrets
import string


def generate_password(
    length: int,
    lowercase: bool = True,
    uppercase: bool = True,
    digits: bool = True,
    special: bool = True,
) -> str:
    """Сгенерировать пароль из выбранных наборов символов."""
    pools = []
    if lowercase:
        pools.append(string.ascii_lowercase)
    if uppercase:
        pools.append(string.ascii_uppercase)
    if digits:
        pools.append(string.digits)
    if special:
        pools.append("!@#$%^&*()-_=+[]{};:,.?")

    if length < 1:
        raise ValueError("Длина пароля должна быть положительной.")
    if not pools:
        raise ValueError("Выберите хотя бы один набор символов.")
    if length < len(pools):
        raise ValueError("Длина меньше количества выбранных типов символов.")

    chars = [secrets.choice(pool) for pool in pools]
    all_chars = "".join(pools)
    chars.extend(secrets.choice(all_chars) for _ in range(length - len(chars)))
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def ask_yes_no(prompt: str) -> bool:
    """Запросить у пользователя ответ да или нет."""
    answer = input(prompt).strip().lower()
    return answer in {"д", "да", "y", "yes", "1"}


def main() -> None:
    """Спросить параметры генерации и напечатать пароль."""
    try:
        length = int(input("Длина пароля: "))
    except ValueError:
        print("Введите длину целым числом.")
        return

    lowercase = ask_yes_no("Строчные буквы? [д/н]: ")
    uppercase = ask_yes_no("Заглавные буквы? [д/н]: ")
    digits = ask_yes_no("Цифры? [д/н]: ")
    special = ask_yes_no("Спецсимволы? [д/н]: ")

    try:
        print("Ваш пароль:", generate_password(
            length, lowercase, uppercase, digits, special
        ))
    except ValueError as error:
        print("Ошибка:", error)


if __name__ == "__main__":
    main()
