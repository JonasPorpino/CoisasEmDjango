from django.http import HttpResponse
from django.shortcuts import render

# existem dois tipos de views  as:
# function based views e as class based views
# aqui apenas functions

def home(request):
    sexo = 'm'
    nome = 'Mendonça'
    return render(request,'index.html', {'sexo': sexo, 'nome': nome})


