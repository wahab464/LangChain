from pydantic import BaseModel,EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0 , lt=4)

new_student = {'name' : 'Abdul Wahab','age':'22','email':'wahabtufail48@gmail.com','cgpa':'3.25'}

student = Student(**new_student)

print(student)