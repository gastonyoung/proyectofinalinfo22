from tokenize import Comment
from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Noticia, Comentario, RespuestaComentario
from apps.eventos_app.models import Evento
from django.http.response import Http404
from .forms import ComentarioForm, NoticiaForm 
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import( CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ComentarioForm
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def NoticiasComunidad(request,id):
    lista_noticias = Noticia.objects.all()
    datanoticia = Noticia.objects.get(id=id)
    context = {
        "noticias": lista_noticias,
        "id": datanoticia
    }
    return render(request, 'categorias/NoticiasComunidad.html', context)


def home(request):
    lista_noticias = Noticia.objects.all().order_by('-tiempo_publicacion')[:3]
    lista_eventos = Evento.objects.all().order_by('-tiempo_publicacion')[:3]
    context = {
        "noticias": lista_noticias,
        "eventos": lista_eventos,
    }
    return render(request,"HOME.html", context)

def noticias(request, id):
    lista_noticias = Noticia.objects.all().order_by('-tiempo_publicacion')
    lista_categorias = Categoria.objects.all()
    
    if id == 9000:
        lista_noticias = Noticia.objects.all().order_by('tiempo_publicacion')
    
    if id > 0 and id != 9000:
        categoria_sele = Categoria.objects.get(id = id)
        lista_noticias = Noticia.objects.filter(categorias = categoria_sele).order_by('tiempo_publicacion')

    context = {
        "noticias": lista_noticias,
        "categorias": lista_categorias,
    }
    return render(request, 'noticias/Noticias.html', context)

@login_required
def articulo(request,id):

    try:
        datanoticia = Noticia.objects.get(id=id)

        lista_comentarios = Comentario.objects.filter(aprobado=True)

    except Noticia.DoesNotExist:

        raise Http404('La Noticia solicitada no existe')

    form_class = ComentarioForm()

    if request.method=="POST":

        form_class = ComentarioForm(request.POST)

        if form_class.is_valid():

            print("Validación Exitosa")

            comment = Comentario(
                autor_id = request.user.id,
                contenido = form_class.cleaned_data["contenido"],
                noticia = datanoticia,
            )

            comment.save()

    context = {
        "noticia": datanoticia,
        "comentarios":lista_comentarios,
        "form":form_class
    }

    return render(request,"noticias/Articulo.html",context)



class CrearNoticiaView(CreateView, LoginRequiredMixin):
    login_url= '/login'
    #redirect_field_name='index_detail.html'

    form_class = NoticiaForm

    model = Noticia


    def blog_categoria(request, categoria):
        posts = Noticia.objects.filter(
            categories__name__contains=categoria
        ).order_by(
            'creado'
        )
        context = {
            "categoria": categoria,
            "posts": posts
        }
        return render(request, "blog_categoria.html", context)

def categoriaDetail(request, id):

    try:
        lista_categorias = Categoria.objects.all()
        categoria = Categoria.objects.get(id = id)
        noticias = Noticia.objects.filter(categorias = id)
        lista_comentarios = Comentario.objects.filter(aprobado=True)
    except Noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')\
    
    form = ComentarioForm()
    
    if (request.method == "POST") and (request.user.id != None):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comment = Comentario(
                autor_id = request.user.id,
                cuerpo_comentario=form.cleaned_data["cuerpo_comentario"],
                noticia=noticias
            )
            comment.save()
            return redirect("Noticia")

    context = {
        "categori":categoria,
        "categorias":lista_categorias,
        "form":form,
        "noticias": noticias,
        "comentarios": lista_comentarios
    }
    return render(request, 'noticias/Noticias.html', context)


@login_required
def hacer_comentario(request, id):
    
    datanoticia = Noticia.objects.get(id=id)

    if request.method=="POST":

        form_class = ComentarioForm(request.POST)

        if form_class.is_valid():

            print("Validación Exitosa")

            comment = Comentario(
                autor = form_class.cleaned_data["autor"],
                contenido = form_class.cleaned_data["contenido"],
                noticia = datanoticia,
            )

            comment.save()

            noticia_id = Noticia.id

            return redirect("Articulo", id=noticia_id)

    else:

        form_class = ComentarioForm()

    context = {"form": form_class,}
    
    return render(request,"Articulo.html", context)


@login_required
def post_publish(request, id):
    try:
        noticias =Noticia.objects.get(id =id)
    except Noticia.DoesNotExist:
        raise Http404('No existe la noticia')
    
    Noticia.publish()
    return redirect('detalle-noticia', id=id)


@login_required
def comment_approve(request, id):

    try:
        comentarios=Comentario.objects.get(id=id)
    except Comentario.DoesNotExist:
        raise Http404("El comentario selecionado no existe")
    
    comentarios.approve()

    return redirect('place_holder_detallenoticia', id=comentarios.noticia.id)


@login_required
def comment_delete(request, id):

    try:
        comentarios=Comentario.objects.get(id=id)
    except Comentario.DoesNotExist:
        raise Http404("El comentario selecionado no existe")
    
    comentarios.delete()

    return redirect('place_holder_detallenoticia', id=comentarios.noticia.id)


def ayudanos(request):
    return render(request,"ayudanos.html",{})
    

