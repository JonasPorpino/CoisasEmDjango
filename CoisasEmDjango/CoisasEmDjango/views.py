from django.http import HttpResponse
from django.shortcuts import render

# existem dois tipos de views  as:
# function based views e as class based views
# aqui apenas functions

def home(request):
    sexo='m'
    nome='Afonso'
    lista=[
        {'nome':'Pedro','sexo':'m'},
        {'nome':'Maria','sexo':'f'},
        {'nome':'Joaquim','sexo':'m'},
        {'nome':'João','sexo':'m'}
    ]
    data = {'lista': lista, 'sexo':sexo, 'nome':nome}
    return render(request,'index.html', data )


