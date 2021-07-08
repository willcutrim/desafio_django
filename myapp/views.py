from django.shortcuts import render, HttpResponseRedirect
from .forms import MedicoForms, LocalPostoForms
from .models import Medico


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
        produto = Medico.objects.get(pk=id)
        produto.delete()
        
        return HttpResponseRedirect('/')