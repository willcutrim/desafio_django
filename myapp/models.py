from django.db import models

class Medico(models.Model):      
    nome = models.CharField(max_length=45, blank=False, null=False)
    sobrenome = models.CharField(max_length=30, blank=False, null=False)
    data_de_admissao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome + ' ' + self.sobrenome
    
class PostodeTrabalho(models.Model):
    nome_do_posto = models.CharField(max_length=55, blank=False, null=False)
    endereco = models.CharField(max_length=55, blank=False, null=False)
    
    