from django.shortcuts import render
from contatos.models import Pessoa
from django.views.generic.base import View

# Create your views here.

class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        contexto = {'pessoa' : pessoas, }
        return render(request, 'contatos/listaContatos.html', contexto)