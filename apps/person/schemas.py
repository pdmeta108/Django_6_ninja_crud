from ninja import ModelSchema, Schema
from pydantic import EmailStr
from .models import Person

class PersonSchema(ModelSchema):
    email: EmailStr

    class Meta:
        model = Person
        fields = ('id', 'name', 'age')

class PersonCreateSchema(Schema):
    name: str
    email: EmailStr
    age: int