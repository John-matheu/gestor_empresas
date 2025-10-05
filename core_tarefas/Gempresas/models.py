from django.db import models

# Create your models here.

class Empresa(models.Model):
    status_choices = [
        ('A', 'Ativa'),
        ('I', 'Inativa'),
        ('S', 'Suspensa'),
    ]

    nome = models.CharField()
    cnpj = models.CharField()
    regime_federal = models.CharField()
    grupo = models.CharField(null=True)
    status = models.CharField(max_length=1, choices=status_choices, default='A',)

    def __str__(self):
            return self.nome
    
class User_model(models.Model):
    nome = models.CharField()
    email = models.CharField()
    senha = models.CharField()
    status = models.BooleanField()

    def __str__(self):
      return self.nome

class User_empresa(models.Model):
    nome = models.CharField()
    email = models.CharField()
    senha = models.CharField()
    status = models.BooleanField()

    def __str__(self):
        return self.nome





