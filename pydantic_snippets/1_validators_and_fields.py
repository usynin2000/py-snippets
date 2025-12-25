from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional

# Example 1: Field with validation and settings

class Product(BaseModel):
    name: str = Field(min_length=1, max_length=100, description="Name of the product")
    price : float = Field(gt=0, description="Price should be greater than 0")
    quantity: int = Field(ge=0, le=10000)
    discount: Optional[float] = Field(default=0, ge=0, le=100)


    @field_validator("name", mode="before")
    @classmethod
    def name_must_not_be_empty(cls, v: str):
        if v.strip() == "":
            raise ValueError("Name must not be empty")
        return v.strip().title()
    
    @field_validator("discount", mode="before")
    @classmethod 
    def validate_discount(cls, v: float | None) -> float | None:
        if v and v > 50:
            print("Attention the discount is huge!")
        return v
    


class Order(BaseModel):
    product_price: float
    quantity: int
    discount_percent: float = 0
    total: Optional[float] = None

    @model_validator(mode="after")
    def calculate_total(self):
        subtotal = self.product_price * self.quantity
        discount_amount = subtotal * (self.discount_percent / 100)
        self.total = subtotal - discount_amount
        return self


if __name__ == "__main__":

    print("Example 1:\n")
    product = Product(
        name= "  laptop  ",
        price=50000.50,
        quantity=10,
        discount=60,
    )

    print("Product is ", product)
    print(f"The name (stripped) is {product.name}\n")

    print("Example 2:\n")

    order = Order(product_price=1000, quantity=5, discount_percent=10)
    print(f"The order is {order}")
    print(f"Total price to pay: {order.total} dollars!!\n")


    print("Example 3: Error while validation\n")

    try:
        ivalid_product = Product(name="Some name", price=-100, quantity=5)
    except Exception as e:
        print(f"Exception {e}")


