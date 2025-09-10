from django.shortcuts import render
from django.http import HttpResponse

from .models import Empresa, User_model, User_empresa

# Create your views here.


def home(request):
    return render(request, 'Gempresas/index.html')

def empresas(request):
    return render(request, 'Gempresas/lista_de_empresas.html')

def listar_empresas(request):
    emp = Empresa.objects.all()
    tamanho = len(emp)
    return render(request, 'Gempresas/lista_de_empresas.html', {'empresas': emp, 'tamanho': tamanho})



def listar_users(request):
    user = User_model.objects.all()
    tamanho = len(user)
    return render(request, 'Gempresas/lista_de_users.html', {'users': user, 'tamanho': tamanho})


def listar_user_empresas(request):
    user_empresa = User_empresa.objects.all()
    tamanho = len(user_empresa)
    return render(request, 'Gempresas/listar_usuarios_clientes.html', {'usuarios_clientes': user_empresa, 'tamanho': tamanho })


