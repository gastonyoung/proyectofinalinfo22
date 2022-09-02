"""proyectofinalInfo URL Configuration

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
from django.urls import include,path
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from apps.noticias_app import views
from django.views.generic.base import TemplateView
from apps.noticias_app import views as viewsnoticia


urlpatterns = [
    path('noticia/<int:id>/', views.articulo, name='articulo'),
    path('noticia/<int:id>/', views.NoticiasComunidad, name='NoticiasComunidad'),

    path('categoria/<int:id>', viewsnoticia.categoriaDetail, name='Noticias'),

    path("noticias/new", views.CrearNoticiaView.as_view(), name='CrearNoticiaView'),
    path("noticias/<int:id>/add_comment", views.hacer_comentario, name='hacer_comentario')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)