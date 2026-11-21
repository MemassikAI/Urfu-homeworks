"""Практика 2. Полиморфизм для транспортных средств."""

class Transport:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def description(self) -> str:
        raise NotImplementedError("Дочерний класс должен реализовать description().")


class Car(Transport):
    def description(self) -> str:
        return f"Автомобиль {self.brand} {self.model}: передвигается по дорогам."


class Bicycle(Transport):
    def description(self) -> str:
        return f"Велосипед {self.brand} {self.model}: приводится в движение педалями."


class Airplane(Transport):
    def description(self) -> str:
        return f"Самолёт {self.brand} {self.model}: перевозит пассажиров по воздуху."


if __name__ == "__main__":
    vehicles = [
        Car("Toyota", "Camry"),
        Bicycle("Stels", "Navigator"),
        Airplane("Airbus", "A320"),
    ]
    # Один и тот же вызов метода — разное поведение объектов.
    for vehicle in vehicles:
        print(vehicle.description())
