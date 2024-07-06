from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from . models import Users
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login
from.models import Barbeiro

# Create your views here.

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        return render(request, 'login.html')
        
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        print(username, senha)
        user = auth.authenticate(username=username, 
                                 password=senha)
        if user:
            auth.login(request, user)
            return redirect(reverse('cliente:home'))
        
        if not user:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos. Tente novamente.')
            return redirect(reverse('login'))
        
        auth.login(request, user)
        return HttpResponse('Usuário logado com sucesso')

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, "As Duas senhas devem ser iguais")
            return redirect(reverse('cadastro'))

        if len(senha) < 3:
            messages.add_message(request, constants.ERROR, "A senha deve ter mais que 6 digitos")
            return redirect(reverse('cadastro'))
        
        users = Users.objects.filter(username=username)
        

        if users.exists():
            messages.add_message(request, constants.ERROR, "Já existe um usúario com esse ursername")
            return redirect(reverse('cadastro'))
        
        users = Users.objects.create_user(
            username=username,
            email=email,
            password=senha,
            
        )
        
        return redirect(reverse('login'))
    

def logout(request):
    request.session.flush()
    return redirect(reverse(login))



def criar_barbeiro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        bio = request.POST['bio']
        especializacao = request.POST['especializacao']
        foto = request.FILES['foto']

        barbeiro = Barbeiro(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
            nome=nome,
            bio=bio,
            especializacao=especializacao,
            foto=foto
        )
        barbeiro.save()
        return redirect('login')
    else:
        return render(request, 'criar_barbeiro.html')