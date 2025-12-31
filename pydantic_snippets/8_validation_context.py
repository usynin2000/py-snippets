from pydantic import BaseModel, field_validator, model_validator, ValidationInfo
from typing import Annotated

# Exmaple 1: Using context in field_validator
class User(BaseModel):
    username: str
    age: int
    role: str = "user"

    @field_validator("age")
    @classmethod
    def validate_age(cls, v: int, info: ValidationInfo) -> int:
        # Access to context of validation
        if info.context: 
            min_age = info.context.get("min_age", 0)
            if v < min_age:
                raise ValueError(f"Age must to be more than {min_age}")
            return v 
    
    @field_validator("role")
    @classmethod
    def vaidate_role(cls, v: str, info: ValidationInfo) -> str:
        if info.context:
            allowed_roles = info.context.get("allowed_roles", ["user", "admin"])
            if v not in allowed_roles: 
                raise ValueError(f"Role should be on of {allowed_roles}")
            return v




if __name__ == "__main__":
    print("Exmaple 1: Context for age and role\n")

    # Without context
    user1 = User(username="Sergo", age=25, role="user")

    print(f"User without context {user1}")

    # With context
    context = {"min_age": 18, "allowed_roles": ["user", "moderator", "admin"]}

    try:
        user2 = User.model_validate(
            {"username": "Anya", "age": 16, "role": "user"},
            context=context,
        )
    except Exception as e:
        print(f"Error!! problem with context {e}")