from django import forms
from .models import Empresa, User_model, User_empresa


class Empresaform(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'cnpj', 'regime_federal', 'grupo', 'status']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'id': 'nome_input'}),
            'cnpj': forms.NumberInput(attrs={'class': 'form-control', 'id': 'cnpj_input'}),
            'regime_federal': forms.TextInput(attrs={'class': 'form-control', 'id': 'regime_federal_input'}),
            'grupo': forms.TextInput(attrs={'class': 'form-control', 'id': 'grupo_input'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'id': 'status_input'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User_empresa
        fields = ['nome', 'email', 'senha']
        





