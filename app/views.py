from django.shortcuts import render, redirect
from app.forms import PersonForm, DogForm
from app.models import Person, DogWalker
from django.http import HttpResponse
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    data = {}
    data['db'] = Person.objects.all()
    return render(request, 'index.html', data)

def contratacao(request):
    data = {}
    data['db'] = DogWalker.objects.all()
    return render(request, 'contratacao.html', data)

def add(request):
    num1 = int(request.GET["num1"])
    res = num1 * 50
    hora = num1
    return render(request, 'result.html', {"result": res})

def lista(request):
    data = {}
    data['db'] = DogWalker.objects.all()
    return render(request, 'listadog.html', data)


def form(request):
    data = {}
    data['form'] = PersonForm()
    return render(request, 'form.html', data)


def create(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def createCadastro(request):
    cadastro = DogForm(request.POST)
    if cadastro.is_valid():
        cadastro.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Person.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Person.objects.get(pk=pk)
    data['form'] = PersonForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Person.objects.get(pk=pk)
    form = PersonForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Person.objects.get(pk=pk)
    db.delete()
    return redirect('home')
