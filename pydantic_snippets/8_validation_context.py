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

# Example 2: Using context in model_validator
class Order(BaseModel):
    product_id: int
    quantity: int
    price: float
    discount: float = 0

    @model_validator(mode="after")
    def validate_order(self, info: ValidationInfo) -> "Order":
        if info.context:
            max_quantity = info.context.get("max_quantity_per_order")
            if max_quantity and self.quantity > max_quantity:
                raise ValueError(f"Max quantitiy: {max_quantity}")
        
            max_discount = info.context.get("max_discount_percent", 100)
            if self.discount > max_discount:
                raise ValueError(f"Max discount: {max_discount}")
        
        return self 



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
    

    print("Example 2: Context for order:\n")

    order_context = {"max_quantity_per_order": 10, "max_discount_percent": 50}

    try: 
        order1 = Order.model_validate(
            {"product_id": 1, "quantity": 15, "price": 1000, "discount": 30},
            context=order_context,
        )
    except Exception as e:
        print(f"Error of quantity: {e}")


    order2 = Order.model_validate(
        {"product_id": 1, "quantity": 5, "price": 1000, "discount": 40},
        context=order_context
    )
    print(f"✓ Valid order: {order2.model_dump()}\n")