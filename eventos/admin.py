from django.contrib import admin
from .models import Evento, Categoria, Inscricao, CustomUser
from django.contrib.auth.models import User

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'local', 'categoria', 'ativo')  # Campos exibidos na lista
    list_filter = ('categoria', 'ativo', 'data')  # Filtros laterais
    search_fields = ('titulo', 'descricao', 'local')  # Campos pesquisáveis
    ordering = ('data',)  # Ordenação padrão
    list_editable = ('ativo',)  # Permite editar o campo "ativo" diretamente na lista
    date_hierarchy = 'data'  # Navegação por hierarquia de datas

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('evento', 'user', 'compareceu')
    list_filter = ('compareceu',)
    search_fields = ('evento__titulo', 'user__user__username')  # Pesquisa por título do evento e nome do usuário

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'cpf', 'idade')
    search_fields = ('user__username', 'cpf', 'telefone')