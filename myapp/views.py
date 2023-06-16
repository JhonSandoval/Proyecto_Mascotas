from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import JsonResponse

from myapp.models import Person, Pet, Specie, Observation

# Create your views here.

def index(request):
    persons = Person.objects.all()
    list_person = []

    for person in persons:
        name_person = "{} {}".format(person.first_name, person.last_name)
        list_person.append(name_person)

    list_person = ['---']
    texto_respuesta = """
        <h1>Hola mundo</h1>
        {}
    """.format(list_person)
    return HttpResponse(texto_respuesta)

def index_2(request):
    template = 'myapp/index.html'
    return render(request, template)
    # return HttpResponse(template.render())

def lists_persons(request):
    persons = Person.objects.all()

    list_persons = []
    for p in persons:
        name_person = "{} {}".format(p.first_name, p.last_name)
        list_persons.append({
            "name": name_person,
            "id": p.id
        })
    
    context = {
        "list": list_persons
    }
    template_name = 'myapp/person_list.html'

    return render(request, template_name, context)

def lists_pets(request):
    pets = Pet.objects.all()

    lists_pets = []
    for p in pets:
        lists_pets.append([p.name, p.age, p.person, p.specie])

    context = {
        "lists": lists_pets
    }

    template_name = 'myapp/pet_list.html'

    return render(request, template_name, context)

def detail_person(request, id):
    person = Person.objects.filter(id=id).first()

    if person:
        context = {
            "id": person.id,
            "display": True, 
            "nombre": person.first_name + " " + person.last_name, 
            "edad": person.edad, 
            "nick_name": person.nick_name
        }
    else:
        context = {
            "display": False
        }
    
    template_name = 'myapp/person_detail.html'

    return render(request, template_name, context)

def detail_person_mascota(request, id):
    person = Person.objects.filter(id=id).first()

    pets = Pet.objects.filter(person=person).all()

    lists_pets = []
    for p in pets:
        lists_pets.append([p.name, p.age, p.person, p.specie])

    context = {
        "lists": lists_pets
    }

    template_name = 'myapp/pet_list.html'

    return render(request, template_name, context)

def detail_pet(request, name):
    pet = Pet.objects.filter(name__iexact = name.lower()).first()

    if pet:
        context = {
            "display": True, 
            "nombre": pet.name,
            "edad": pet.age, 
            "especie": pet.specie,
            "dueno": pet.person
        }
    else:
        context = {
            "display": False
        }
    
    template_name = 'myapp/pet_detail.html'

    return render(request, template_name, context)

def detail_pet_observation(request, name):
    pet = Pet.objects.filter(name__iexact = name.lower()).first()

    if pet:
        observations = Observation.objects.filter(pet = pet.id).all()
        context = {
            "display": True, 
            "nombre": pet.name,
            "edad": pet.age, 
            "especie": pet.specie,
            "dueno": pet.person,
            "observaciones": observations
        }
    else:
        context = {
            "display": False
        }
    
    template_name = 'myapp/pet_detail_observation.html'

    return render(request, template_name, context)

def detail_specie(request, id):
    specie = Specie.objects.filter(id = id).first()

    if specie:
        texto_respuesta = """
            <h1>Datos de la especie: {}</h1>
            <p>Tipo: {}</p>
        """.format(specie.name, specie.get_kind_display())
    else:
        texto_respuesta = """
            <h1>No se encuentra información de la especie con id: {}</h1>
        """.format(id)
    return HttpResponse(texto_respuesta)

def lists_persons_json(request):
    persons = Person.objects.all()

    list_persons = []
    for p in persons:
        name_person = "{} {}".format(p.first_name, p.last_name)
        list_persons.append(name_person)
    
    context = {
        "list": list_persons
    }

    return JsonResponse(context)