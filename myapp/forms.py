from django import forms
from django.core import validators
from django.forms import fields
from .models import Medico, PostodeTrabalho, TabeladeHorario, TabelaFolga

class MedicoForms(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome','sobrenome']
        

class LocalPostoForms(forms.ModelForm):
    class Meta:
        model = PostodeTrabalho
        fields = ['nome_do_posto', 'endereco']
        
        
        
class TabelaForms(forms.ModelForm):
    class Meta:
        model = TabeladeHorario
        fields = '__all__'

class TabelaFolgaForms(forms.ModelForm):
    class Meta:
        model = TabelaFolga
        fields = '__all__'
        