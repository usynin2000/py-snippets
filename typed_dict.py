from typing import TypedDict

# TypedDict — для словарей с фиксированной структурой
# Используется вместо dict[str, Any], когда поля фиксированы.

class User(TypedDict):
    name: str
    age: int


if __name__ == '__main__':
    user = User(name="John", age=12)
    print(user)
    print(type(user))
    print(user['name'])
