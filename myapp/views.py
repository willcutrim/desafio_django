from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import MedicoForms, LocalPostoForms, TabelaForms, TabelaFolgaForms
from .models import Medico, PostodeTrabalho, TabeladeHorario, TabelaFolga


def deletar_horario(request, id):
    if request.method == 'POST':
        tabela = TabeladeHorario.objects.get(pk=id)
        tabela.delete()
        return redirect('/home')
    

def home(request):
    listar = Medico.objects.all()
    horario = TabeladeHorario.objects.filter()[:5]
    start_date = request.GET.get('data_inicial')
    end_date = request.GET.get('data_final')
    
    if start_date and end_date:
        horario = TabeladeHorario.objects.filter(data_de_trabalho__range=[start_date, end_date])
    return render(request, 'html/home.html', {'listar': listar, 'horario': horario})

def cadastro_de_medicos(request):
    listar = Medico.objects.all()
    if request.method == 'POST':
        form = MedicoForms(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MedicoForms()
    
    return render(request, 'html/cadastro.html', {'form': form, 'listar': listar})


def editar_medico(request, id):
    listar = Medico.objects.get(pk=id)
    if request.method == 'POST':
        form = MedicoForms(request.POST, instance=listar)
        if form.is_valid():
            form.save()
    else:
        listar = Medico.objects.get(pk=id)
    form = MedicoForms(instance=listar)

    return render(request, 'html/editar.html', {'form': form, 'listar': listar})

def deletar_medico(request, id):
    if request.method == 'POST':
        medico = Medico.objects.get(pk=id)
        medico.delete()
        return redirect('/cadastro-de-medico')
    
def cadastro_de_clinica(request):
    listar = PostodeTrabalho.objects.all()
    if request.method == 'POST':
        form = LocalPostoForms(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LocalPostoForms()
    
    return render(request, 'html/cadastro_postos.html', {'form': form, 'listar': listar})

def editar_clinica(request, id):
    listar = PostodeTrabalho.objects.get(pk=id)
    if request.method == 'POST':
        form = LocalPostoForms(request.POST, instance=listar)
        if form.is_valid():
            form.save()
    else:
        listar = PostodeTrabalho.objects.get(pk=id)
    form = LocalPostoForms(instance=listar)

    return render(request, 'html/editar.html', {'form': form, 'listar': listar})


def deletar_clinica(request, id):
    if request.method == 'POST':
        clinica = PostodeTrabalho.objects.get(pk=id)
        clinica.delete()
        
        return redirect('/cadastro-de-clinica')


def cadastro_de_tabela(request):
    horario = TabeladeHorario.objects.all()
    medicos = Medico.objects.all()
    folga = TabelaFolga.objects.all()
    clinica = PostodeTrabalho.objects.all()
    if request.method == 'POST':
        form = TabelaForms(request.POST)
        
        if form.is_valid():
            form.save()
            print('cadastrou lindamente')
        else:
            print('deu gongo')
    else:
        form = TabelaForms()
    
    return render(request, 'html/cadastro_tabela.html', {'form': form, 'medicos': medicos, 'clinica': clinica, 'horario':horario})

def cadastro_folga(request):
    folga = TabelaFolga.objects.all()
    medicos = Medico.objects.all()
    if request.method == 'POST':
        form = TabelaFolgaForms(request.POST)
        if form.is_valid():
            form.save()
            print('o cara foi cadatrado!')
        else:
            print('deu B.O siô')
    else:
        form = TabelaFolgaForms()
        
    return render(request, 'html/cadastro_de_folga.html', {'folga': folga, 'form': form, 'medicos': medicos})


