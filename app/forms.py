from django.forms import ModelForm
from app.models import Person


# Aqui é onde criamos os campos do form
class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['nome', 'nomePet', 'pet']
