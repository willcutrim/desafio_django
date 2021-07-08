from django import forms
from django.core import validators
from .models import Medico, PostodeTrabalho

class MedicoForms(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'
        

class LocalPostoForms(forms.ModelForm):
    class Meta:
        model = PostodeTrabalho
        fields = '__all__'