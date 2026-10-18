"""Шифр Цезаря для русского и английского текста."""

ENGLISH = "abcdefghijklmnopqrstuvwxyz"
RUSSIAN = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def shift_char(char: str, shift: int) -> str:
    """Сдвинуть букву в её алфавите, сохранив регистр."""
    for alphabet in (ENGLISH, RUSSIAN):
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            shifted = alphabet[(index + shift) % len(alphabet)]
            return shifted.upper() if char.isupper() else shifted
    return char


def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    """Зашифровать или расшифровать текст заданным сдвигом."""
    if decrypt:
        shift = -shift
    return "".join(shift_char(char, shift) for char in text)


def main() -> None:
    """Получить настройки и вывести результат шифрования."""
    mode = input("1 — шифровать, 2 — дешифровать: ").strip()
    text = input("Введите текст: ")
    try:
        shift = int(input("Введите величину сдвига: "))
    except ValueError:
        print("Сдвиг должен быть целым числом.")
        return

    if mode not in {"1", "2"}:
        print("Выберите 1 или 2.")
        return

    print("Результат:", caesar_cipher(text, shift, decrypt=mode == "2"))


if __name__ == "__main__":
    main()
