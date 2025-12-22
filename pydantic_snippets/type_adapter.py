from pydantic import TypeAdapter, BaseModel

# Пример 1: Валидация списка моделей
class User(BaseModel):
    name: str
    age: int

# Данные из API (например, JSON)
data = [
    {"name": "Иван", "age": 25},
    {"name": "Мария", "age": 30}
]

# Валидация всего списка за раз
# Validate all list by one try
users = TypeAdapter(list[User]).validate_python(data)

print(f"Exmaple 1: users = {users}\n")

# Пример 2: Валидация словаря
data_dict = {"key1": "value1", "key2": "value2"}
result = TypeAdapter(dict[str, str]).validate_python(data_dict)
print(f"Example 2: result = {result}\n")

# Пример 3: Валидация списка примитивов
numbers = [1, 2, 3, 4, 5]
validated = TypeAdapter(list[int]).validate_python(numbers)

print(f"Example 3: validated list of ints = {validated}\n")

# Пример 4: Вложенные структуры
class Address(BaseModel):
    city: str
    street: str

class Person(BaseModel):
    name: str
    addresses: list[Address]

data_nested = {
    "name": "Иван",
    "addresses": [
        {"city": "Москва", "street": "Ленина"},
        {"city": "СПб", "street": "Невский"}
    ]
}

person = TypeAdapter(Person).validate_python(data_nested)

print(f"Example 4: person = {person}\n")