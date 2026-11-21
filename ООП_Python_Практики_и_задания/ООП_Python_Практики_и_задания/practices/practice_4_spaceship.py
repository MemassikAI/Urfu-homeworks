"""Практика 4. Симулятор управления космическим кораблём."""

from typing import Dict, List


class SpaceShip:
    def __init__(self, name: str, fuel: float, hull: int, speed: float = 0):
        if fuel < 0 or not 0 <= hull <= 100 or speed < 0:
            raise ValueError("Некорректные начальные параметры корабля.")
        self.name = name
        self.fuel = float(fuel)
        self.hull = int(hull)
        self.speed = float(speed)

    def accelerate(self, amount: float, fuel_cost: float = 2) -> None:
        if amount <= 0 or fuel_cost < 0:
            raise ValueError("Ускорение должно быть положительным, расход топлива — неотрицательным.")
        required_fuel = amount * fuel_cost
        if self.fuel < required_fuel:
            raise ValueError("Недостаточно топлива для ускорения.")
        self.fuel -= required_fuel
        self.speed += amount

    def travel(self, distance: float, fuel_per_unit: float = 1) -> None:
        if distance < 0 or fuel_per_unit < 0:
            raise ValueError("Расстояние и расход топлива не могут быть отрицательными.")
        required_fuel = distance * fuel_per_unit
        if self.fuel < required_fuel:
            raise ValueError("Недостаточно топлива для полёта.")
        self.fuel -= required_fuel

    def take_damage(self, damage: int) -> None:
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным.")
        self.hull = max(0, self.hull - damage)

    def repair(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Ремонт не может быть отрицательным.")
        self.hull = min(100, self.hull + amount)


class CrewMember:
    def __init__(self, name: str, role: str, health: int = 100, skills=None):
        if not 0 <= health <= 100:
            raise ValueError("Здоровье должно быть от 0 до 100.")
        self.name = name
        self.role = role
        self.health = health
        self.skills = dict(skills or {})

    def take_damage(self, damage: int) -> None:
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным.")
        self.health = max(0, self.health - damage)

    def train(self, skill: str, points: int = 1) -> None:
        if points <= 0:
            raise ValueError("Количество очков навыка должно быть положительным.")
        self.skills[skill] = self.skills.get(skill, 0) + points


class Mission:
    def __init__(self, title: str, goal: str, resource_budget: Dict[str, float]):
        self.title = title
        self.goal = goal
        self.resource_budget = dict(resource_budget)
        self.events: List[str] = []
        self.completed = False

    def record_event(self, event: str) -> None:
        self.events.append(event)

    def asteroid_encounter(self, ship: SpaceShip, damage: int = 15) -> None:
        ship.take_damage(damage)
        self.record_event(f"Встреча с астероидами: корпус повреждён на {damage}%.")

    def accident(self, ship: SpaceShip, crew_member: CrewMember, hull_damage: int = 10, crew_damage: int = 5) -> None:
        ship.take_damage(hull_damage)
        crew_member.take_damage(crew_damage)
        self.record_event(
            f"Авария: корпус -{hull_damage}%, здоровье {crew_member.name} -{crew_damage}%."
        )

    def complete(self) -> None:
        self.completed = True
        self.record_event(f"Миссия выполнена: {self.goal}")


if __name__ == "__main__":
    ship = SpaceShip("Орёл", fuel=100, hull=100)
    pilot = CrewMember("Алексей", "пилот", skills={"пилотирование": 3})
    engineer = CrewMember("Мария", "инженер", skills={"ремонт": 4})
    mission = Mission("Экспедиция-1", "достичь орбиты Марса", {"fuel": 100, "spare_parts": 5})

    ship.accelerate(10)
    ship.travel(20)
    mission.asteroid_encounter(ship)
    engineer.train("ремонт")
    ship.repair(10)
    mission.complete()

    print(f"Корабль: {ship.name}; топливо: {ship.fuel}; корпус: {ship.hull}%; скорость: {ship.speed}")
    print(f"Экипаж: {pilot.name} ({pilot.role}), здоровье: {pilot.health}%; "
          f"{engineer.name} ({engineer.role}), навыки: {engineer.skills}")
    print(f"Миссия: {mission.title}; цель: {mission.goal}; завершена: {mission.completed}")
    print("События:")
    for event in mission.events:
        print("-", event)
