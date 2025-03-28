from django.shortcuts import render, redirect
from .models import Evento, Inscricao, Categoria, CustomUser
from .forms import EventoForm, InscricaoForm, CategoriaForm, CustomUserForm

def index(request):
    return render(request, 'eventos/home_eventos.html')

def cadastro_categorias(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'eventos/cadastro_categorias.html', {'form': form})

def cadastro_eventos(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventoForm()
    return render(request, 'eventos/cadastro_eventos.html', {'form': form})