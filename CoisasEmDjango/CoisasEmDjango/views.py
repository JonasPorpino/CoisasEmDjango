from django.http import HttpResponse

def home(request):
    return HttpResponse('Ola mundo')

def clientes(request):
    return HttpResponse('Aqui tem coisas do clientes')