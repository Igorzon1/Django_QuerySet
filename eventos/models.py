from django.contrib.auth.models import User
from django.db import models

# Classe de Categoria
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Classe de Usuário Customizado
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)  # Campo opcional
    idade = models.PositiveIntegerField(blank=True, null=True)  # Campo opcional

    def __str__(self):
        return self.user.username  # Referenciando o username do User relacionado

# Classe de Evento
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    data = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    local = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    capacidade = models.PositiveIntegerField()
    organizador = models.CharField(max_length=100)
    palestrante = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.titulo

# Classe de Inscrição
class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    compareceu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.user.username} - {self.evento.titulo}"  # Referenciando o username do User relacionado
