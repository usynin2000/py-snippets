from pydantic import BaseModel, computed_field
from datetime import datetime, date
from typing import Optional


# Example 1: Computed field for calculation
class Rectangle(BaseModel):
    width: float
    height: float


    @computed_field # without this decorator there will no be propertry in model_dump
    @property
    def area(self) -> float:
        return self.width * self.height
    

    @computed_field
    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    

# Example 2: Computed field with dates
class Employee(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    salary: float
    bonus_percent: float = 0

    @computed_field
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    @computed_field
    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
    
    @computed_field
    @property
    def total_compensation(self) -> float:
        return self.salary + (self.salary * self.bonus_percent / 100)



if __name__ == "__main__":
    # Example 1
    rect = Rectangle(width=10, height=5)
    print(f"Rectangle {rect.width}x{rect.height}")
    print(f"Area {rect.area}")
    print(f"Perimeter {rect.perimeter}")
    print(f"Whole object {rect.model_dump()}\n")


    # Example 2
    emp = Employee(
        first_name="Sergey",
        last_name="Usynin",
        birth_date=date(2000, 12, 7),
        salary=10000000,
        bonus_percent=15,
    )

    print(f"Employee: {emp.full_name}")
    print(f"Age {emp.age} years old")
    print(f"Salary {emp.salary} dollars.")
    print(f"Bonus {emp.bonus_percent}")
    print(f"Total compensation {emp.total_compensation}")
    print(f"\n JSON: {emp.model_dump_json(indent=2)}")