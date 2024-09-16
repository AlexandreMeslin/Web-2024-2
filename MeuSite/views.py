from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView

def home(request):
    return render(request, 'MeuSite/home.html')

'''
Controle de Acesso
'''
def homeSec(request):
    return render(request, 'seguranca/homeSec.html')

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
    else:
        formulario = UserCreationForm()
    context = {
        'form' : formulario, 
        'titulo' : 'Registro de Usuário',
        'cabecalho' : 'Página de Registro',
        'texto_btn' : 'Registrar',
    }
    return render(request, 'seguranca/form.html', context)

@login_required
def paginaSecreta(request):
		return render(request, 'seguranca/paginaSecreta.html')

def logout(request):
    # view para apresentar o formulário 
    # de confirmação de logout
    return render(request, 'seguranca/logout.html')

class MeuUpdateView(UpdateView):
      def get(self, request, pk, *args, **kwargs):
            if request.user.id == pk:
                  return super().get(request, pk, args, kwargs)
            else:
                  return redirect('sec-home')
