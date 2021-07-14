from django.urls import path
from . import views

urlpatterns = [

    path('home', views.home, name='home'),
    path('deletar-horario/<int:id>/', views.deletar_horario, name='deletar-horario'),
    
    path('cadastro-de-medico', views.cadastro_de_medicos, name='cadastro-de-medico'),
    path('editar-medico/<int:id>/', views.editar_medico, name='editar-medico'),
    path('deletar/<int:id>/', views.deletar_medico, name='deletar'),
    
    
    path('cadastro-de-clinica', views.cadastro_de_clinica, name='cadastro-de-clinica'),
    path('editar-clinica/<int:id>/', views.editar_clinica, name='editar-clinica'),
    path('deletar-clinica/<int:id>/', views.deletar_clinica, name='deletar-clinica'),
    
    path('cadastro-de-tabela', views.cadastro_de_tabela, name='cadastro-de-tabela'),
    
    path('cadastro-de-folga', views.cadastro_folga, name='cadastro-de-folga')
   
]