from django.db import models
from django.contrib.auth.models import AbstractUser 

class Users(AbstractUser):
    choices_cargo = (
        ('V', 'Vendedor'),
        ('G', 'Gerente'),
        ('C', 'Caixa'),
        ('CL', 'Cliente'),
        ('B', 'Barbeiro')
    )
    cargo = models.CharField(max_length=2, choices=choices_cargo, default='CL')

class Barbeiro(Users):
    nome = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    especializacao = models.CharField(max_length=50, blank=True)
    foto = models.ImageField(upload_to='barbeiros', blank=True)

    def __str__(self):
        return self.nome