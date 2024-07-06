# cliente/urls.py
from django.urls import path
from . import views

app_name = 'cliente'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('novo_agendamento/', lambda request: redirect('agendamentos:criar_agendamento'), name='novo_agendamento'),
    
]