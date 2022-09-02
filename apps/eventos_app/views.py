from django.shortcuts import render
from django.http.response import Http404
from .models import Evento,CategoriaEvento
from apps.noticias_app.models import Categoria, Noticia, Comentario, RespuestaComentario
from apps.noticias_app.forms import ComentarioForm, NoticiaForm 

# Create your views here.

def home(request):
    return render(request,"HOME.html",{})

def eventos(request, id):
    lista_eventos = Evento.objects.all().order_by('-horario_comienzo_evento')
    lista_categorias = CategoriaEvento.objects.all()
    
    if id == 9000:
        lista_eventos = Evento.objects.all().order_by('horario_comienzo_evento')
    
    if id > 0 and id != 9000:
        categoria_sele = CategoriaEvento.objects.get(id = id)
        lista_eventos = Evento.objects.filter(categorias = categoria_sele).order_by('horario_comienzo_evento')

    context = {
        "eventos": lista_eventos,
        "categorias": lista_categorias,
    }
    return render(request, 'eventos/Eventos.html', context)