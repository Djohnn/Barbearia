from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('cadastro/', views.cadastro, name="cadastro" ),
    path('sair/', views.logout, name="sair"),
    path('criar_barbeiro/', views.criar_barbeiro, name='criar_barbeiro')
]