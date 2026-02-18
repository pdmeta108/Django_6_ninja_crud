from ninja import ModelSchema
from .models import Person

class PersonSchema(ModelSchema):
    class Meta:
        model = Person
        fields = ('name', 'email', 'age')