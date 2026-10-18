"""Конвертер обычных и римских чисел."""

VALUES = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]
SUBTRACTIVE = {"CM": 900, "CD": 400, "XC": 90,
               "XL": 40, "IX": 9, "IV": 4}


def to_roman(number: int) -> str:
    """Преобразовать целое число от 1 до 3999 в римское."""
    if not 1 <= number <= 3999:
        raise ValueError("Поддерживаются числа от 1 до 3999.")
    result = []
    for value, symbol in VALUES:
        count, number = divmod(number, value)
        result.append(symbol * count)
    return "".join(result)


def from_roman(roman: str) -> int:
    """Преобразовать каноническую римскую запись в целое число."""
    roman = roman.strip().upper()
    if not roman:
        raise ValueError("Строка не должна быть пустой.")

    singles = {"I": 1, "V": 5, "X": 10, "L": 50,
               "C": 100, "D": 500, "M": 1000}
    total = 0
    index = 0
    while index < len(roman):
        pair = roman[index:index + 2]
        if pair in SUBTRACTIVE:
            total += SUBTRACTIVE[pair]
            index += 2
        elif roman[index] in singles:
            total += singles[roman[index]]
            index += 1
        else:
            raise ValueError(f"Недопустимый символ: {roman[index]}")

    if to_roman(total) != roman:
        raise ValueError(f"Некорректная римская запись: {roman}")
    return total


def main() -> None:
    """Предложить направление преобразования."""
    print('Примеры: ["IV", "IX", "XLII", "XCIX", "MMXXIII"]')
    mode = input("1 — обычное в римское, 2 — римское в обычное: ").strip()
    try:
        if mode == "1":
            print(to_roman(int(input("Число (1–3999): "))))
        elif mode == "2":
            print(from_roman(input("Римское число: ")))
        else:
            print("Выберите 1 или 2.")
    except ValueError as error:
        print("Ошибка:", error)


if __name__ == "__main__":
    main()
