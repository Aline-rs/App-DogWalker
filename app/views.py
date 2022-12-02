from django.shortcuts import render, redirect
from app.forms import PersonForm
from app.models import Person


# Create your views here.
def home(request):
    data = {}
    data['db'] = Person.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = PersonForm()
    return render(request, 'form.html', data)


def create(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Person.objects.get(pk=pk)
    return render(request, 'view.html', data)