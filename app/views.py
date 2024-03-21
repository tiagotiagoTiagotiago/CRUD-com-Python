from django.shortcuts import render, redirect
from app.forms import UsuarioForm
from app.models import Usuario

# Create your views here.
def home(request):
    data = {}
    data['db'] = Usuario.objects.all()
    return render(request, 'index.html', data) 

def form(request):
    data = {}
    data['form'] = UsuarioForm
    return render(request, 'form.html', data)

def create(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    

def view(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    return render(request, 'view.html', data)



def edit(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    data['form'] = UsuarioForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data ={}
    data['db'] = Usuario.objects.get(pk=pk)
    form = UsuarioForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def delete(requeste, pk):
    db = Usuario.objects.get(pk=pk)
    db.delete()
    return redirect('home')    