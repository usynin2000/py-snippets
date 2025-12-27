from pydantic import BaseModel, Field

from typing import Literal
from datetime import datetime

# Base model
class BaseEntity(BaseModel):
    id: int | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = None


class User(BaseEntity):
    username: str
    email: str
    is_active: bool = True


class Post(BaseEntity):
    title: str
    content: str
    author_id: int
    views: int = 0 

# Example 2: Multiple Inheritance
class TimestampMixin(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class AuthorMixin(BaseModel):
    author_id: int
    author_name: str


class Article(TimestampMixin, AuthorMixin):
    title: str
    content: str
    category: str


class Cat(BaseModel):
    pet_type: Literal["cat"]
    name: str
    meow_volume: int

class Dog(BaseModel):
    pet_type: Literal["dog"]
    name: str
    bark_volume: int

class Lizard(BaseModel):
    pet_type: Literal["lizard"]
    name: str
    scales_color: str

from typing import Union
from pydantic import Field as F

class PetOwner(BaseModel):
    name: str
    pet: Union[Cat, Dog, Lizard] = F(discriminator="pet_type")



if __name__ == "__main__":
    # Example 1
    user = User(id=1, username="sergo", email="usynin.s00@mail.ru")
    post = Post(id=10, title="My post", content="Content of post", author_id=1)

    print(f"User: {user.model_dump()}")
    print(f"\n Post: {post.model_dump()}")


    # Example 2
    article = Article(
        title="Article about Python",
        content="Contents of article...",
        category="Programming",
        author_name="Sergey Usynin",
        author_id=1,
    )

    print("\n Article: ", article.model_dump())

    # Example 3: Discriminated Union
    owner1 = PetOwner(
        name="Alex",
        pet={"pet_type": "cat", "name": "Murka", "meow_volume": 10}
    )
    
    owner2 = PetOwner(
        name="Anya",
        pet={"pet_type": "dog", "name": "Balloon", "bark_volume": 15}
    )

    owner3 = PetOwner(
        name="Sergo",
        pet={"pet_type": "lizard", "name": "Satoshi", "scales_color": "Green"}
    )

    print("\n Owner 1: ", owner1.model_dump())
    print("\n Owner 2: ", owner2.model_dump())
    print("\n Owner 3: ", owner3.model_dump())


