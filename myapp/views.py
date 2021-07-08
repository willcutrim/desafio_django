from django.shortcuts import render, HttpResponseRedirect
from .forms import MedicoForms, LocalPostoForms
from .models import Medico, PostodeTrabalho


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
        
        return HttpResponseRedirect('/')
    
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
        
        return HttpResponseRedirect('/cadastro-de-clinica')
