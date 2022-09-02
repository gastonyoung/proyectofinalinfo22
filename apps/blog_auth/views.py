from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth.models import User

# Create your views here.

class Login(auth_views.LoginView):
    '''Vista de Login de Usuario'''

    template_name = 'login.html'

class Logout(LoginRequiredMixin, auth_views.LogoutView):
    '''Vista de Cierre de Sesión del Usuario'''

    template_name = 'logout.html'

class WelcomeView(CreateView):

    template_name='welcome.html'


class SignUpView(FormView):
    '''Vista de Registro de Usuario'''

    template_name='blog_auth/register.html'

    form_class=SignUpForm

    success_url = reverse_lazy('registercomplete')


    def form_valid(self, form):
        '''Verificamos que los datos del formulario sean válidos y los guardamos'''

        form.save()

        return super().form_valid(form)
