from django.http import HttpResponse

# existem dois tipos de views  as:
# function based views e as class based views
# aqui apenas functions

def home(request):
    return HttpResponse('Ola mundo')

def clientes(request):
    return HttpResponse('Aqui tem coisas do clientes')