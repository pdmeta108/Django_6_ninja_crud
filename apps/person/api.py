from ninja import Router
from .schemas import PersonSchema, PersonCreateSchema
from .models import Person

from django.shortcuts import get_object_or_404

router = Router()

@router.get("/persons", response=list[PersonSchema])
def list_persons(request):
    persons = Person.objects.all()
    return persons

@router.get("/persons/{person_id}", response=PersonSchema)
def get_person(request, person_id: int):
    person = get_object_or_404(Person, id=person_id)
    return person

@router.post("/persons", response=PersonSchema)
def create_person(request, payload: PersonCreateSchema):
    person = Person.objects.create(**payload.dict())
    return person

@router.put("/persons/{person_id}", response=PersonSchema)
def update_person(request, person_id: int, payload: PersonCreateSchema):
    person = get_object_or_404(Person, id=person_id)
    for attr, value in payload.dict().items():
        setattr(person, attr, value)
    person.save()
    return person

@router.delete("/persons/{person_id}")
def delete_person(request, person_id: int):
    person = get_object_or_404(Person, id=person_id)
    person.delete()
    return {"success": True}