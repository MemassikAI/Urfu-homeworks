"""Задание 4. Абстрактный Printable и его реализация в Book."""

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_info(self) -> str:
        """Возвращает информацию, которую можно вывести."""
        raise NotImplementedError


class Book(Printable):
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def print_info(self) -> str:
        return f'«{self.title}» — {self.author}, {self.year}'


if __name__ == "__main__":
    book = Book("Преступление и наказание", "Фёдор Достоевский", 1866)
    print(book.print_info())
