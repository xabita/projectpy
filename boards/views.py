from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Board



# Create your views here.


@login_required
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})



def principal(request):
    return HttpResponse('Menu principal!')
    
def despedida(request):
    return HttpResponse('Hasta pronto!')
    


def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})