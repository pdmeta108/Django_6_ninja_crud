from ninja import ModelSchema, Schema
from pydantic import EmailStr
from .models import Person

class PersonSchema(ModelSchema):
    class Meta:
        model = Person
        fields = ('id', 'name', 'email', 'age')

class PersonCreateSchema(Schema):
    name: str
    email: EmailStr
    age: int