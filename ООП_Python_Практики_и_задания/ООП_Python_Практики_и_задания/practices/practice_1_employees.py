"""Практика 1. Наследование и расчёт зарплаты сотрудников."""

class Employee:
    def __init__(self, name: str, base_salary: float):
        if base_salary < 0:
            raise ValueError("Оклад не может быть отрицательным.")
        self.name = name
        self.base_salary = float(base_salary)

    def calculate_salary(self) -> float:
        return self.base_salary


class Manager(Employee):
    def __init__(self, name: str, base_salary: float, team_size: int, bonus_per_employee: float = 500):
        super().__init__(name, base_salary)
        if team_size < 0 or bonus_per_employee < 0:
            raise ValueError("Размер команды и премия не могут быть отрицательными.")
        self.team_size = team_size
        self.bonus_per_employee = bonus_per_employee

    def calculate_salary(self) -> float:
        return self.base_salary + self.team_size * self.bonus_per_employee


class Developer(Employee):
    def __init__(self, name: str, base_salary: float, completed_tasks: int, bonus_per_task: float = 1000):
        super().__init__(name, base_salary)
        if completed_tasks < 0 or bonus_per_task < 0:
            raise ValueError("Количество задач и премия не могут быть отрицательными.")
        self.completed_tasks = completed_tasks
        self.bonus_per_task = bonus_per_task

    def calculate_salary(self) -> float:
        return self.base_salary + self.completed_tasks * self.bonus_per_task


if __name__ == "__main__":
    staff = [
        Employee("Алексей", 50_000),
        Manager("Мария", 70_000, team_size=5),
        Developer("Иван", 80_000, completed_tasks=8),
    ]
    for employee in staff:
        print(f"{employee.name}: {employee.calculate_salary():,.2f} руб.")
