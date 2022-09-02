"""proyectoFinalInformatorio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.urls import re_path as url
from apps.noticias_app import views as viewsnoticia
from apps.eventos_app import views as viewsevento
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewsnoticia.home, name='home'),
    path('HOME', viewsnoticia.home, name='HOME'),   
    path('login', include('apps.blog_auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('noticias/<int:id>/', viewsnoticia.noticias, name='noticias'),
    path('eventos/<int:id>/', viewsevento.eventos, name='eventos'),

#CategoriasNoticias
    path('NoticiasComunidad', viewsnoticia.NoticiasComunidad, name='NoticiasComunidad'),
    path('noticia/<int:id>/', viewsnoticia.NoticiasComunidad, name='NoticiasComunidad'),
    path('categoria/<int:id>', viewsnoticia.categoriaDetail, name='Noticia'),

    path('articulo/<int:id>/', viewsnoticia.articulo, name='articulo'),
    path('ayudanos', viewsnoticia.ayudanos, name='ayudanos'),
    url('noticias/', include('apps.noticias_app.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT,show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,show_indexes=True)
