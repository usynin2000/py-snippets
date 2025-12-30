from pydantic import BaseModel, field_validator, ValidationInfo
from typing import Annotated
from pydantic.functional_validators import AfterValidator, BeforeValidator, WrapValidator

# Example 1: Simple custom type with AfterValidator
def validate_positive(v: int) -> int:
    if v <= 0:
        raise ValueError("Number should be positive")
    return v

PositiveInt = Annotated[int, AfterValidator(validate_positive)]

class Product(BaseModel):
    name: str
    quantity: PositiveInt
    price: PositiveInt


# Example 2: BeforeValidator for data conversion
def convert_to_uppercase(v: str | None) -> str:
    if v is None:
        return ""
    return str(v).upper()

UpperCaseStr = Annotated[str, BeforeValidator(convert_to_uppercase)]


class Company(BaseModel):
    name: UpperCaseStr
    code: UpperCaseStr


# Example 3: WrapValidator for full control
def validate_email_or_phone(v, handler, info: ValidationInfo):
    """Validator recives email and phone"""
    if isinstance(v, str):
        if "@" in v:
            # this is email
            if not v.count("@") == 1:
                raise ValueError("Bad email")
            return {"type": "email", "value": v}
        elif v.startswith("+") or v.isdigit():
            # this is phone
            return {"type": "phone", "value": v}
    raise ValueError("The value should be email or phone!")

ContactInfo = Annotated[dict, WrapValidator(validate_email_or_phone)]


class User(BaseModel):
    name: str
    contact: ContactInfo


# Example 4: Composition of validators
def strip_whitespace(v: str) -> str:
    return v.strip() if isinstance(v, str) else v

def validate_min_length(v: str) -> str:
    if len(v) < 3: 
        raise ValueError("Minimus length is 3 chars")
    return v

CleanStrig = Annotated[
    str,
    BeforeValidator(strip_whitespace),
    AfterValidator(validate_min_length),
]


class Account(BaseModel):
    username: CleanStrig
    display_name: CleanStrig


if __name__ == "__main__":
    print("Exmaple 1: PositiveInt\n")

    try:
        product = Product(name="Laptop", quantity=10, price=5000)
        print(f"Product is created {product.model_dump()}")
    except Exception as e:
        print(f"error: {e}")
    
    try: 
        invalid_product = Product(name="Laptop", quantity=-5, price=5000)
    except Exception as e:
        print(f"Error: {e}")
    

    print("Example 2: UpperCaseStr\n")

    company = Company(name="google", code="goog")
    print(f"Company: {company.model_dump()}")
    print(f"The name of the company in uppercase {company.name}\n")


    print("Example 3: WrapValidator for email of phone\n")
    user1 = User(name="Sergo", contact="usynin.s00@mail.ru")
    print(f"User 1: {user1.model_dump()}")

    user2 = User(name="Anna", contact="+79778472107")
    print(f"User 2: {user2.model_dump()}\n")


    print("Example 4: Composition validators\n")
    account = Account(username="    john  ", display_name="       John Rogan   ")
    print(f"Account (cleaned): {account.model_dump()}")


    try: 
        invalid_account = Account(username="    jo     ", display_name="OK name")
    except Exception as e:
        print(f"Error {e}")

