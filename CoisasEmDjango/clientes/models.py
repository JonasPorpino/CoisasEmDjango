from django.db import models

# Esse tipo de relacionamento será de muito para muitos

class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# o tipo de relacionamento é de um para um
class CPF(models.Model):
    numero = models.CharField(max_length=15)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.numero

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=70, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()
    cpf = models.OneToOneField(CPF, on_delete=models.CASCADE, null=True, blank=True)# ele vem acima por questão de referência
    departamentos = models.ManyToManyField(Departamento, blank=True)

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
    
