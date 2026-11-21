import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tasks.task_1_book import Book as BasicBook
from tasks.task_2_ebook import Ebook
from tasks.task_3_book_features import Book as FeatureBook
from tasks.task_4_abstract_printable import Book as PrintableBook, Printable
from practices.practice_1_employees import Employee, Manager, Developer
from practices.practice_2_transport import Car, Bicycle, Airplane
from practices.practice_3_online_store import Product, ShoppingCart, Customer
from practices.practice_4_spaceship import SpaceShip, CrewMember, Mission


class TestTasks(unittest.TestCase):
    def test_task_1(self):
        self.assertIn("Толстой", BasicBook("Война и мир", "Толстой", 1869).info())

    def test_task_2(self):
        ebook = Ebook("1984", "Оруэлл", 1949, "epub")
        self.assertEqual(ebook.format, "epub")
        self.assertIn("EPUB", ebook.info())

    def test_task_3(self):
        book = FeatureBook("1984", "Оруэлл", 1949)
        self.assertEqual(book, FeatureBook.from_string("1984;Оруэлл;1949"))
        self.assertIsInstance(str(book), str)
        book.age = 20
        self.assertEqual(book.age, 20)

    def test_task_4(self):
        self.assertTrue(issubclass(PrintableBook, Printable))
        self.assertIn("Достоевский", PrintableBook("Преступление", "Достоевский", 1866).print_info())


class TestPractices(unittest.TestCase):
    def test_employees(self):
        self.assertEqual(Manager("М", 50000, 2, 1000).calculate_salary(), 52000)
        self.assertEqual(Developer("Д", 50000, 3, 500).calculate_salary(), 51500)

    def test_transport_polymorphism(self):
        vehicles = [Car("A", "B"), Bicycle("C", "D"), Airplane("E", "F")]
        self.assertEqual(len([v.description() for v in vehicles]), 3)

    def test_online_store(self):
        product = Product("Товар", 100, 5, "Категория")
        cart = ShoppingCart()
        cart.add_product(product, 2)
        customer = Customer("Имя", "mail@example.com")
        order = customer.place_order(cart, discount_percent=10, tax_percent=20)
        self.assertEqual(order.total, 216.0)
        self.assertEqual(product.stock, 3)
        self.assertEqual(len(customer.order_history), 1)
        self.assertEqual(cart.total(), 0)

    def test_spaceship(self):
        ship = SpaceShip("Тест", 100, 100)
        crew = CrewMember("Пилот", "пилот")
        mission = Mission("Тестовая", "цель", {"fuel": 100})
        ship.accelerate(5)
        mission.asteroid_encounter(ship, 20)
        crew.take_damage(10)
        self.assertEqual(ship.hull, 80)
        self.assertEqual(crew.health, 90)
        mission.complete()
        self.assertTrue(mission.completed)


if __name__ == "__main__":
    unittest.main()
