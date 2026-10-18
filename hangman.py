"""Простая консольная игра «Виселица»."""

import random

WORDS = ["питон", "функция", "алгоритм", "переменная", "компьютер"]
MAX_MISTAKES = 6


def play() -> None:
    """Провести один раунд игры."""
    word = random.choice(WORDS)
    guessed = set()
    mistakes = 0

    print("Игра «Виселица». Угадайте слово по буквам.")
    while mistakes < MAX_MISTAKES:
        visible = " ".join(char if char in guessed else "_" for char in word)
        print(f"\nСлово: {visible}")
        print(f"Ошибки: {mistakes}/{MAX_MISTAKES}")
        letter = input("Введите одну букву: ").strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Введите ровно одну букву.")
            continue
        if letter in guessed:
            print("Вы уже называли эту букву.")
            continue

        guessed.add(letter)
        if letter not in word:
            mistakes += 1
            print("Такой буквы нет.")
        else:
            print("Есть такая буква!")

        if all(char in guessed for char in word):
            print(f"Победа! Слово: {word}")
            return

    print(f"Вы проиграли. Загаданное слово: {word}")


if __name__ == "__main__":
    play()
