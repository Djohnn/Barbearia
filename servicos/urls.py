# servicos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('listar_servicos/', views.listar_servicos, name='listar_servicos'),
    path('adicionar_servico/', views.adicionar_servico, name='adicionar_servico'),
     
]
