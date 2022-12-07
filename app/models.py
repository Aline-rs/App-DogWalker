from django.db import models

from project import settings


# Create your models here.
class Person(models.Model):
    nome = models.CharField(max_length=150)
    nomePet = models.CharField(max_length=150, null=True)
    pet = models.CharField(max_length=150, null=True)


class DogWalker(models.Model):
    nome_dog = models.CharField(max_length=150)
    valor = models.IntegerField()
    data = models.DateField()
    hora = models.TimeField(null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def soma():
        self.total = (self.hora * self.valor)
        return super(DogWalker, self).save(*args, **kwargs)

