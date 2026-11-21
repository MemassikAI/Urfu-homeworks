"""Задание 3. Магические методы, свойство и альтернативный конструктор."""

from datetime import date


class Book:
    def __init__(self, title: str, author: str, year: int):
        if not isinstance(year, int) or year < 0 or year > date.today().year:
            raise ValueError("Год издания должен быть корректным целым числом.")
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f'«{self.title}» — {self.author} ({self.year})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title, self.author, self.year) == (
            other.title, other.author, other.year
        )

    @property
    def age(self) -> int:
        """Возраст книги в годах."""
        return date.today().year - self.year

    @age.setter
    def age(self, value: int) -> None:
        """Позволяет задать возраст книги и пересчитывает год издания."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Возраст книги должен быть неотрицательным целым числом.")
        self.year = date.today().year - value

    @classmethod
    def from_string(cls, data: str) -> "Book":
        """Создаёт книгу из строки формата 'название;автор;год'."""
        parts = [part.strip() for part in data.split(";")]
        if len(parts) != 3:
            raise ValueError("Ожидается строка формата: название;автор;год")
        title, author, year_text = parts
        try:
            year = int(year_text)
        except ValueError as exc:
            raise ValueError("Год издания должен быть целым числом.") from exc
        return cls(title, author, year)


if __name__ == "__main__":
    first = Book("1984", "Джордж Оруэлл", 1949)
    second = Book.from_string("1984; Джордж Оруэлл; 1949")
    print(first)
    print("Книги одинаковы:", first == second)
    print("Возраст книги:", first.age)
    first.age = 25
    print("Год после изменения возраста:", first.year)
