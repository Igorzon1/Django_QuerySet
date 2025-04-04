from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Evento, Inscricao, Categoria, CustomUser
from .forms import EventoForm, InscricaoForm, CategoriaForm, CustomUserForm, UserRegistrationForm

def index(request):
    #mostrar os eventos cadastrados
    eventos = Evento.objects.all()
    return render(request, 'eventos/home_eventos.html', {'eventos': eventos})

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

def cadastro_usuario(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        custom_user_form = CustomUserForm(request.POST)

        if user_form.is_valid() and custom_user_form.is_valid():
            # Salvar o usuário padrão
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Salvar o CustomUser
            custom_user = custom_user_form.save(commit=False)
            custom_user.user = user
            custom_user.save()

            return redirect('index')  # Redirecionar para a página inicial ou outra página
    else:
        user_form = UserRegistrationForm()
        custom_user_form = CustomUserForm()

    return render(request, 'eventos/cadastro_usuario.html', {
        'user_form': user_form,
        'custom_user_form': custom_user_form,
    })

def lista_eventos(request):
    Eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': Eventos})