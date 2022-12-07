from django.forms import ModelForm
from app.models import Person, DogWalker


# Aqui é onde criamos os campos do form
class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['nome', 'nomePet', 'pet']

class DogForm(ModelForm):
    class Meta:
        model = DogWalker
        fields = ['nome_dog', 'valor', 'data', 'hora', 'total']
