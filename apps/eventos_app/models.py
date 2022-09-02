from datetime import datetime
from tkinter import CASCADE
from django.db import models
from django.utils import timezone

# Create your models here.

class CategoriaEvento(models.Model):

    categoria_nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.categoria_nombre

class Evento(models.Model):

    titulo = models.CharField(max_length=200)

    autor = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    contenido = models.TextField()

    imagen_ref = models.ImageField(null = True, blank = True, upload_to = 'imagenes/evento', help_text = 'Seleccione una imagen para mostrar')

    tiempo_creacion = models.DateTimeField(default=timezone.now) 

    ultima_modificacion = models.DateTimeField(auto_now=True)

    tiempo_publicacion = models.DateTimeField(null = True, blank = True)

    categorias = models.ManyToManyField('CategoriaEvento', related_name='evento')

    lugar_evento = models.CharField(max_length=150)
    
    modalidad_evento = models.CharField(null=True, blank=True, max_length=150)

    horario_comienzo_evento = models.DateTimeField(null=True, blank=True)


    def publicar_evento(self):

        self.tiempo_publicacion = datetime.now
        self.save()


    def comentariosAprobados(self):

        return self.comentarios_evento.filter(aprobado=True)