from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
import json

# Example 1: Base serilization
class UserProfile(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    username: str
    email: str
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool = True
    score: int | None = None


# Example 2: Custom serilization with alias
class APIResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: int = Field(alias="userId")
    full_name: str = Field(alias="fullName")
    email_address: str = Field(alias="email")


# Example 3: Exclude and include while serilization
class SecureUser(BaseModel):
    username: str
    email: str
    password_hash: str
    internal_id: int


if __name__ == "__main__":
    user = UserProfile(username="Sergo2000   ", email=" exmaple@gmail.com", score=100)
    
    # here date will be as python object 'created_at': datetime.datetime(2025, 12, 25, 16, 22, 52, 144669
    print("1. model_dmp():")
    print(user.model_dump()) 


    # here date will be json serilizable "created_at":"2025-12-25T16:22:52.144669"
    print("\n2. model_dump_json():")
    print(user.model_dump_json()) 


    # Example 2: Work with alias
    api_data = {
        "userId": 1,
        "fullName": "Sergo Sergeev",
        "email": "sergo@gmail.com",
    }

    response = APIResponse(**api_data)

    print("\n3. Data with alias:")
    print(response.model_dump())

    print("\n4. With alis in output:")
    print(response.model_dump(by_alias=True))


    # Example 3: Exceptions fields while serilization
    secure_user = SecureUser(
        username="admin",
        email="admin@example.com",
        password_hash="secret_hash_12345",
        internal_id=999,
    )
    print("\n5. Safe output (without password)")
    print(secure_user.model_dump(exclude={"password_hash", "internal_id"}))

    print("\n6. Only public fields")
    print(secure_user.model_dump(include={"username", "email"}))
    

    

