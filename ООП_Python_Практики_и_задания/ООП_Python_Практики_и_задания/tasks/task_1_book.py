"""Задание 1. Класс Book с информацией о книге."""

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str:
        return f'Книга: «{self.title}», автор: {self.author}, год издания: {self.year}'


if __name__ == "__main__":
    book = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
    print(book.info())
