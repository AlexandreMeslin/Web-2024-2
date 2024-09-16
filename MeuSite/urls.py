"""
URL configuration for MeuSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from MeuSite import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls.base import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User

urlpatterns = [
    path("admin/", admin.site.urls),
    path('MeuApp/', include('MeuApp.urls')),
    path('contatos/', include('contatos.urls')),
    path('', views.home, name='homepage'),
    path('seguranca/', views.homeSec, name='sec-home'),
    path('seguranca/registro/', views.registro, name='sec-registro'),
    path('seguranca/login/', LoginView.as_view(template_name='seguranca/form.html', extra_context={'titulo':'Login', 'cabecalho':'Página de Login', 'texto_btn': 'Login'}), name='sec-login'),
    path('seguranca/profile/', views.paginaSecreta, name='sec-paginaSecreta'),
    path('meulogout/', views.logout, name='sec-meulogout'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('sec-home'),), name='sec-logout'),
    path('seguranca/password_change/', PasswordChangeView.as_view(template_name='seguranca/form.html', success_url=reverse_lazy('sec-password_change_done'), extra_context={'titulo':'Troca Senha', 'cabecalho':'Página de Troca de Senha', 'texto_btn': 'Troca senha'},), name='sec-password_change'),
    path('seguranca/password_change_done/', PasswordChangeDoneView.as_view(template_name='seguranca/password_change_done.html', ), name='sec-password_change_done'),
    path('seguranca/terminaRegistro/<int:pk>/', views.MeuUpdateView.as_view(template_name='seguranca/form.html', success_url=reverse_lazy('sec-home'), model=User, fields=['first_name', 'last_name', 'email', ], extra_context={'titulo':'Registro de Usuário', 'cabecalho':'Complete seus dados', 'texto_btn': 'Atualiza'}, ), name='sec-completaDadosUsuario'),
]
