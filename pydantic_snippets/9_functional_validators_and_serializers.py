"""
Pydantic Functional Validators and Serializers Examples

This file demonstrates the use of:
- BeforeValidator: preprocesses input data before validation
- AfterValidator: validates/transforms data after validation
- PlainSerializer: customizes how data is serialized in model_dump()
"""

from pydantic import AfterValidator, BaseModel, BeforeValidator, PlainSerializer, ValidationError
from typing import Annotated, List
from datetime import datetime
import json


# === BeforeValidator Examples ===

def strip_and_title(v: str) -> str:
    """BeforeValidator: Clean and format string input"""
    return str(v).strip().title()

def parse_comma_separated(v: str) -> List[str]:
    """BeforeValidator: Convert comma-separated string to list"""
    if isinstance(v, str):
        return [item.strip() for item in v.split(",") if item.strip()]
    return v

def ensure_positive(v) -> float:
    """BeforeValidator: Convert negative to positive"""
    try:
        num = float(v)
        return abs(num)
    except (ValueError, TypeError):
        return 0.0


# === AfterValidator Examples ===

def validate_email_domain(v: str) -> str:
    """AfterValidator: Check email domain restrictions"""
    if not v.endswith(("@gmail.com", "@yahoo.com", "@outlook.com")):
        raise ValueError("Only Gmail, Yahoo, and Outlook emails allowed")
    return v

def validate_password_strength(v: str) -> str:
    """AfterValidator: Check password requirements"""
    if len(v) < 8:
        raise ValueError("Password must be at least 8 characters")
    if not any(c.isupper() for c in v):
        raise ValueError("Password must contain at least one uppercase letter")
    if not any(c.isdigit() for c in v):
        raise ValueError("Password must contain at least one digit")
    return v

def validate_age_range(v: int) -> int:
    """AfterValidator: Check age is reasonable"""
    if not (0 <= v <= 150):
        raise ValueError("Age must be between 0 and 150")
    return v


# === PlainSerializer Examples (if available) ===

def format_currency(v: float) -> str:
    """PlainSerializer: Format price as currency string"""
    return f"${v:,.2f}"

def format_datetime_readable(v: datetime) -> str:
    """PlainSerializer: Format datetime in readable format"""
    return v.strftime("%B %d, %Y at %I:%M %p")

def mask_sensitive_data(v: str) -> str:
    """PlainSerializer: Mask sensitive information"""
    if len(v) <= 4:
        return v
    return v[:2] + "*" * (len(v) - 4) + v[-2:]

# Custom types with serializers
CurrencyAmount = Annotated[float, PlainSerializer(format_currency)]
ReadableDateTime = Annotated[datetime, PlainSerializer(format_datetime_readable)]
MaskedString = Annotated[str, PlainSerializer(mask_sensitive_data)]


# === Model Definitions ===

class UserProfile(BaseModel):
    """Example with BeforeValidator and AfterValidator"""
    name: Annotated[str, BeforeValidator(strip_and_title)]
    email: Annotated[str, AfterValidator(validate_email_domain)]
    age: Annotated[int, AfterValidator(validate_age_range)]
    tags: Annotated[List[str], BeforeValidator(parse_comma_separated)] = []


class SecureAccount(BaseModel):
    """Example with password validation"""
    username: str
    password: Annotated[str, AfterValidator(validate_password_strength)]
    balance: Annotated[float, BeforeValidator(ensure_positive)]


class Product(BaseModel):
    """Example with PlainSerializer for custom output"""
    name: str
    price: CurrencyAmount
    created_at: ReadableDateTime
    serial_number: MaskedString

class Order(BaseModel):
    """Complex example combining all three"""
    customer_email: Annotated[str, AfterValidator(validate_email_domain)]
    items: Annotated[List[str], BeforeValidator(parse_comma_separated)]
    total_amount: CurrencyAmount
    order_date: ReadableDateTime
    tracking_number: MaskedString


# === Demo Code ===

if __name__ == "__main__":
    print("=== Pydantic Functional Validators and Serializers Demo ===\n")
    a = 2

    # Example 1: BeforeValidator and AfterValidator
    print("1. User Profile with Validators:")
    try:
        user = UserProfile(
            name="  john doe  ",
            email="john.doe@gmail.com",
            age=25,
            tags="python, web dev, ai"
        )
        print(f"✓ User created: {user.model_dump()}")
    except ValidationError as e:
        print(f"✗ Validation error: {e}")

    try:
        invalid_user = UserProfile(
            name="Jane Smith",
            email="jane.smith@forbidden.com",  # Invalid domain
            age=200,  # Invalid age
            tags="javascript, react"
        )
    except ValidationError as e:
        print(f"✗ Expected validation errors: {len(e.errors())} errors found")

    print()
    a = 4

    # Example 2: Password validation
    print("2. Secure Account with Password Validation:")
    try:
        account = SecureAccount(
            username="johndoe",
            password="MySecurePass123",
            balance=-100  # Will be converted to positive
        )
        print(f"✓ Account created: {account.model_dump()}")
    except ValidationError as e:
        print(f"✗ Validation error: {e}")

    try:
        weak_account = SecureAccount(
            username="weakuser",
            password="123"  # Too weak
        )
    except ValidationError as e:
        print(f"✗ Expected password validation error: {e.errors()[0]['msg']}")

    print()

    # Example 3: PlainSerializer (if available)
    print("3. Product with Custom Serialization:")
    product = Product(
        name="Gaming Laptop",
        price=2499.99,
        created_at=datetime(2025, 1, 19, 14, 30),
        serial_number="SN123456789"
    )

    print(f"✓ Product data: {product.model_dump()}")
    print(f"✓ Serialized JSON: {product.model_dump_json(indent=2)}")

    print("\n4. Order with Combined Validators and Serializers:")
    order = Order(
        customer_email="customer@gmail.com",
        items="laptop, mouse, keyboard",
        total_amount=2749.99,
        order_date=datetime.now(),
        tracking_number="TRK987654321"
    )

    print(f"✓ Order data: {order.model_dump()}")
    print(f"✓ Serialized JSON: {order.model_dump_json(indent=2)}")

else:
    print("3. PlainSerializer examples skipped (not available in this Pydantic version)")

print("\n=== Demo Complete ===")



# PlainSerializer - это инструмент для кастомизации вывода данных при сериализации. Он не влияет на валидацию или внутреннее хранение, но меняет то, как данные выглядят при выводе.
# Что делает PlainSerializer?
# Он преобразует данные только при сериализации (когда вызывается model_dump() или model_dump_json()), но не меняет сами данные в модели.

# class Product(BaseModel):
#     name: str
#     price: CurrencyAmount  # float внутри, но string при выводе
#     serial_number: MaskedString

# product = Product(
#     name="Gaming Laptop",
#     price=2499.99,  # Хранится как float
#     serial_number="SN123456789"  # Хранится как string
# )

# # Внутренние данные остаются неизменными:
# print(product.price)  # 2499.99 (float)
# print(product.serial_number)  # "SN123456789" (string)

# # Но при сериализации данные преобразуются:
# print(product.model_dump())
# # {'name': 'Gaming Laptop', 'price': '$2,499.99', 'serial_number': 'SN*****89'}