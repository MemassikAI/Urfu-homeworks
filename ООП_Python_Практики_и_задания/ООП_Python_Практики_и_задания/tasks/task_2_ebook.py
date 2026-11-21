"""Задание 2. Электронная книга наследует класс Book."""

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str:
        return f'Книга: «{self.title}», автор: {self.author}, год издания: {self.year}'


class Ebook(Book):
    def __init__(self, title: str, author: str, year: int, file_format: str):
        super().__init__(title, author, year)
        self.format = file_format.lower().lstrip(".")

    def info(self) -> str:
        return f'{super().info()}, формат: {self.format.upper()}'


if __name__ == "__main__":
    ebook = Ebook("1984", "Джордж Оруэлл", 1949, "epub")
    print(ebook.info())
