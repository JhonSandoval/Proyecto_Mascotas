from django.contrib import admin
from myapp.models import Person
from myapp.models import Pet
from myapp.models import Specie
from myapp.models import Observation

# Register your models here.
admin.site.register(Person)
admin.site.register(Pet)
admin.site.register(Specie)
admin.site.register(Observation)
