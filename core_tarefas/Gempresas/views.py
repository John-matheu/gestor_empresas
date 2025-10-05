from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse

from .models import Empresa, User_model, User_empresa, User_model, User_empresa 
from .form import Empresaform

# Create your views here.


def home(request):
    return render(request, 'Gempresas/index_meu.html')


# ------------------------------------------------------------------------------------------------------------------------
# Empresas

def empresas(request):
    return render(request, 'Gempresas/lista_de_empresas.html')

def listar_empresas(request):
    emp = Empresa.objects.all()
    tamanho = len(emp)
    return render(request, 'Gempresas/lista_de_empresas_meu.html', {'empresas': emp, 'tamanho': tamanho})

def add_empresa(request):
    if request.method == 'POST':
        form = Empresaform(request.POST)
        if form.is_valid():
            print('[+] Formulario valido')
            form.save()
            return redirect('listar_empresas')
        
        else:
            print('[-] Formulario Invalido')

    else:
        form = Empresaform()
    return render(request, 'Gempresas/add_empresa.html', {'form': form})

def edit_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    if request.method == 'POST':
        form = Empresaform(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('listar_empresas')
    else:
        form = Empresaform(instance=empresa)

    return render(request, 'Gempresas/edit_empresa_meu.html', {'form': form})


def delete_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    empresa.delete()
    return redirect('listar_empresas')





# ------------------------------------------------------------------------------------------------------------------------
# Users

def listar_users(request):
    user = User_model.objects.all()
    tamanho = len(user)
    return render(request, 'Gempresas/lista_de_users.html', {'users': user, 'tamanho': tamanho})


def listar_user_empresas(request):
    user_empresa = User_empresa.objects.all()
    tamanho = len(user_empresa)
    return render(request, 'Gempresas/listar_usuarios_clientes.html', {'usuarios_clientes': user_empresa, 'tamanho': tamanho })


def add_user(request):
    pass

def add_user_empresa(request):
    pass


