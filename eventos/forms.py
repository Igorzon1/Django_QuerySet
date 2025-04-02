from django import forms
from django.contrib.auth.models import User
from .models import Categoria, Evento, CustomUser, Inscricao

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Categoria'}),
        }

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descricao', 'data', 'local', 'categoria', 'capacidade', 'organizador', 'palestrante']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'local': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'capacidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'organizador': forms.TextInput(attrs={'class': 'form-control'}),
            'palestrante': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme a Senha'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de Usuário'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['cpf', 'idade']
        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade'}),
        }

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['evento', 'user', 'compareceu']
        widgets = {
            'evento': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'compareceu': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
