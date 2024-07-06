from django.shortcuts import render, get_object_or_404, redirect
#TODO ATIVAR AS PROTEÇÃO DAS VIEWS
#from django.contrib.auth.decorators import login_required
from .models import Agendamento
from .forms import AgendamentoForm
from servicos.models import Servico

# @login_required
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'listar_agendamentos.html', {'agendamentos': agendamentos})

# @login_required
def criar_agendamento(request):
    servicos = Servico.objects.all()
    barbeiros = Barbeiro.objects.all()
    servico_id = request.GET.get('servico')
    servico_selecionado = None

    if servico_id:
        servico_selecionado = get_object_or_404(Servico, id=servico_id)

    if request.method == 'POST':
        data = request.POST.get('data')
        hora = request.POST.get('hora')
        servico = get_object_or_404(Servico, id=request.POST.get('servico'))
        barbeiro = get_object_or_404(Barbeiro, id=request.POST.get('barbeiro'))

        Agendamento.objects.create(
            cliente=request.user,
            barbeiro=barbeiro,
            data=data,
            hora=hora,
            servico=servico.nome,
            status='pendente'
        )
        return redirect('cliente:home')

    return render(request, 'agendamentos/criar_agendamento.html', {
        'servicos': servicos,
        'barbeiros': barbeiros,
        'servico_selecionado': servico_selecionado,
    })

# def criar_agendamento(request):
#     if request.method == 'POST':
#         form = AgendamentoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('listar_agendamentos')
#     else:
#         form = AgendamentoForm()
#     return render(request, 'criar_agendamento.html', {'form': form})

# @login_required
def editar_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('listar_agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'editar_agendamento.html', {'form': form})
#TODO
#@login_required
def escolher_servico(request):
    servicos = Servico.objects.all()
    return render(request, 'agendamentos/escolher_servico.html', {'servicos': servicos})



#TODO
#@login_required
def agendar_servico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    
    if request.method == 'POST':
        cliente = request.user
        barbeiro = ...  # lógica para selecionar barbeiro
        data = request.POST.get('data')
        hora = request.POST.get('hora')
        status = 'pendente'

        agendamento = Agendamento(cliente=cliente, barbeiro=barbeiro, data=data, hora=hora, servico=servico, status=status)
        agendamento.save()
        messages.success(request, 'Agendamento criado com sucesso!')
        return redirect('nome_da_view_de_sucesso')

    return render(request, 'agendamentos/agendar_servico.html', {'servico': servico})
