from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # processamento antes de mostrar a home page
    #return HttpResponse('Alô mundo!')
    return render(request, 'MeuApp/home.html')

def segundasPagina(request):
    # processamento antes de mostrar a segunda página
    return render(request, 'MeuApp/segunda.html')
