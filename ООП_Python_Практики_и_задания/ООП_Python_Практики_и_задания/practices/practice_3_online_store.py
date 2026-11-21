"""Практика 3. Упрощённая модель интернет-магазина."""

from dataclasses import dataclass
from typing import Dict, List


@dataclass(eq=False)
class Product:
    name: str
    price: float
    stock: int
    category: str

    def __post_init__(self):
        if self.price < 0 or self.stock < 0:
            raise ValueError("Цена и остаток не могут быть отрицательными.")


class ShoppingCart:
    def __init__(self):
        self.items: Dict[Product, int] = {}

    def add_product(self, product: Product, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("Количество должно быть больше нуля.")
        new_quantity = self.items.get(product, 0) + quantity
        if new_quantity > product.stock:
            raise ValueError(f"Недостаточно товара «{product.name}» на складе.")
        self.items[product] = new_quantity

    def remove_product(self, product: Product) -> None:
        self.items.pop(product, None)

    def update_quantity(self, product: Product, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным.")
        if quantity == 0:
            self.remove_product(product)
        elif quantity > product.stock:
            raise ValueError(f"Недостаточно товара «{product.name}» на складе.")
        else:
            self.items[product] = quantity

    def total(self) -> float:
        return sum(product.price * quantity for product, quantity in self.items.items())

    def clear(self) -> None:
        self.items.clear()


class Order:
    def __init__(self, items: Dict[Product, int], discount_percent: float = 0, tax_percent: float = 20):
        if not 0 <= discount_percent <= 100:
            raise ValueError("Скидка должна быть от 0 до 100%.")
        if tax_percent < 0:
            raise ValueError("Налог не может быть отрицательным.")
        self.items = dict(items)
        self.discount_percent = discount_percent
        self.tax_percent = tax_percent
        self.total = 0.0
        self.is_paid = False

    def checkout(self) -> float:
        if self.is_paid:
            raise RuntimeError("Заказ уже оформлен.")
        for product, quantity in self.items.items():
            if quantity > product.stock:
                raise ValueError(f"Недостаточно товара «{product.name}» на складе.")
        subtotal = sum(p.price * q for p, q in self.items.items())
        discounted = subtotal * (1 - self.discount_percent / 100)
        self.total = round(discounted * (1 + self.tax_percent / 100), 2)
        for product, quantity in self.items.items():
            product.stock -= quantity
        self.is_paid = True
        return self.total


class Customer:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.order_history: List[Order] = []

    def place_order(self, cart: ShoppingCart, discount_percent: float = 0, tax_percent: float = 20) -> Order:
        if not cart.items:
            raise ValueError("Нельзя оформить пустую корзину.")
        order = Order(cart.items, discount_percent, tax_percent)
        order.checkout()
        self.order_history.append(order)
        cart.clear()
        return order


if __name__ == "__main__":
    laptop = Product("Ноутбук", 75_000, 5, "Электроника")
    mouse = Product("Мышь", 1_500, 20, "Аксессуары")

    cart = ShoppingCart()
    cart.add_product(laptop, 1)
    cart.add_product(mouse, 2)
    cart.update_quantity(mouse, 1)

    customer = Customer("Анна", "anna@example.com")
    order = customer.place_order(cart, discount_percent=10, tax_percent=20)

    print(f"Заказ оформлен. Итоговая сумма: {order.total:.2f} руб.")
    print(f"Заказов в истории покупателя: {len(customer.order_history)}")
    print(f"Остаток ноутбуков: {laptop.stock}")
