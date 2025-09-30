from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # URL raiz chama a view home
    
    path('listar_empresas/', views.listar_empresas, name='listar_empresas'),
    path('add_empresa/', views.add_empresa, name='add_empresa'),
    path('delete_empresa/', views.delete_empresa, name='delete_empresa'),
    path('empresa/editar/<int:id>', views.edit_empresa, name='edit_empresa'),



    path('listar_users/', views.listar_users, name='listar_users'),
    path('listar_users_empresas/', views.listar_user_empresas, name='listar_users_empresas'),
]



