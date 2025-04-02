from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_categorias/', views.cadastro_categorias, name='cadastro_categorias'),
    path('cadastro_eventos/', views.cadastro_eventos, name='cadastro_eventos'),
    path('cadastro_usuario/', views.cadastro_usuario, name='cadastro_usuario'),
    path('lista_eventos/',views.lista_eventos,name='lista_eventos'),
]