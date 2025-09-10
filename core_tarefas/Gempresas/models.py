from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField()
    cnpj = models.CharField()
    regime_federal = models.CharField()
    grupo = models.CharField(null=True)
    status = models.CharField()

    def __str__(self):
            return self.nome
    
class User_model(models.Model):
    nome = models.CharField()
    email = models.CharField()
    senha = models.CharField()

    def __str__(self):
      return self.nome

class User_empresa(models.Model):
    nome = models.CharField()
    email = models.CharField()
    senha = models.CharField()

    def __str__(self):
        return self.nome





