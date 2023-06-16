from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()
    nick_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

# Model specie
class Specie(models.Model):
    kinds = [
        ("D", "Domestico"),
        ("W", "Silvestre")
    ]
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=1, choices=kinds, default="D")

    def __str__(self) -> str:
        return "{}-{}".format(self.name, self.get_kind_display())

# Model Pet
class Pet(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=0)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} - {} - {}".format(self.name, self.person, self.age)

class Observation(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField()
    file = models.FileField()

    def __str__(self) -> str:
        return "{} - {} - {}".format(self.pet.name, self.description[0:20], self.date)