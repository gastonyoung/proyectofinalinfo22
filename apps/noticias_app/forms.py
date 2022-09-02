from django import forms
from .models import Comentario, Noticia
from django.forms import widgets
from django.contrib.auth.models import User

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('autor', 'titulo', 'contenido', 'categorias')

        widgets ={
            'titulo': forms.TextInput(attrs={'class':'textIntputClass'}),
            'contenido': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class ComentarioForm(forms.Form):

	model = Comentario
	fields = ('contenido')

	contenido = forms.CharField(widget=forms.Textarea)