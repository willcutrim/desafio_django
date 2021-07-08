from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro_de_medicos, name='cadastro'),
    path('editar/<int:id>/', views.editar_medico, name='editar'),
    path('deletar/<int:id>/', views.deletar_medico, name='deletar'),
]