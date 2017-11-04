from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!')


def principal(request):
    return HttpResponse('Menu principal!')
    
def despedida(request):
    return HttpResponse('Hasta pronto!')
    
