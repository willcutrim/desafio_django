from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro_de_medicos, name='cadastro'),
    path('editar/<int:id>/', views.editar_medico, name='editar'),
    path('deletar/<int:id>/', views.deletar_medico, name='deletar'),
    
    
    path('cadastro-de-clinica', views.cadastro_de_clinica, name='cadastro-de-clinica'),
    path('editar-clinica/<int:id>/', views.editar_clinica, name='editar-clinica'),
    path('deletar-clinica/<int:id>/', views.deletar_clinica, name='deletar-clinica')
]