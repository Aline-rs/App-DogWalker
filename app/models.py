from django.db import models

from project import settings


# Create your models here.
class Person(models.Model):
    nome = models.CharField(max_length=150)
    nomePet = models.CharField(max_length=150)
    pet = models.CharField(max_length=150)


class DogWalker(models.Model):
    nome = models.CharField(max_length=150)
    valor = models.IntegerField()
    data = models.DateField()
    hora = models.TimeField(null=True)
    total = models.DecimalField()


def save(self, *args, **kwargs):
    self.total = (self.hora * self.valor)
    return super(DogWalker, self).save(*args, **kwargs)


