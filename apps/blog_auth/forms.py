from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import widgets


class SignUpForm(UserCreationForm):
    '''Formulario que el usuario debe completar para poder registrarse'''

    email=forms.EmailField(required=True)

    password1: forms.CharField(max_length=50, min_length=6, widget=forms.PasswordInput())

    password2: forms.CharField(max_length=50, min_length=6, widget=forms.PasswordInput())

    class Meta:
        model= User

        fields=(
            'username',
            'email',
            'password1',
            'password2',
        )

    def clean(self):
        '''Verifico que las contraseñas sean iguales'''
        
        data = super().clean()

        password1 = data['password1']

        password2 = data['password2']

        if password1 != password2:

            raise forms.ValidationError("Las contraseñas no son iguales")
        
        return data