from pydantic import BaseModel

class UserInput(BaseModel):
    name: str
    age: int
    email: str 


class UserOutput(BaseModel):
    name: str
    age: int
    email: str 
    user_id: int = 0

# directly
user_input = UserInput(name="Sergi", age=25, email="sergo@example.com")
user_output = UserOutput.model_validate(user_input.model_dump())

print(user_output)