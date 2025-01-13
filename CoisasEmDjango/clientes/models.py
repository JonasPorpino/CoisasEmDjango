from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=70, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nome

# criando telefones para relacionar com os clientes 
# Nesse tipo é um cliente para muitos telefones

class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=80)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.descricao + ' - ' + self.numero