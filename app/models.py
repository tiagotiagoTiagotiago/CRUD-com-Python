from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=90)
    cpf = models.CharField(max_length=14)  
    email = models.EmailField()
    numero_telefone = models.CharField(max_length=15)  
    cep = models.CharField(max_length=9)