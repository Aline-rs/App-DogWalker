from django.db import models

from project import settings


# Create your models here.
class Person(models.Model):
    nome = models.CharField(max_length=150)
    valor = models.CharField(max_length=100)
    data = models.IntegerField()
