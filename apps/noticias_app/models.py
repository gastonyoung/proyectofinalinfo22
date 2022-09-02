from datetime import datetime
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):

    categoria_nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.categoria_nombre



class Noticia(models.Model):

    titulo = models.CharField(max_length=200)
    
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    contenido = models.TextField()

    imagen_ref = models.ImageField(null = True, blank = True, upload_to = 'imagenes/noticia', help_text = 'Seleccione una imagen para mostrar')

    tiempo_creacion = models.DateTimeField(default=timezone.now) 

    ultima_modificacion = models.DateTimeField(auto_now=True)

    tiempo_publicacion = models.DateTimeField(null = True, blank = True)

    categorias = models.ManyToManyField('Categoria')



    def publicar_noticia(self):

        self.tiempo_publicacion = datetime.now
        self.save()


    def comentariosAprobados(self):

        return self.comentarios.filter(aprobado=True)
    
    def __str__(self):
        return self.titulo



class Comentario(models.Model):

    autor = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    contenido = models.TextField()

    tiempo_creacion = models.DateTimeField(default=timezone.now)    

    noticia = models.ForeignKey('Noticia', related_name='comentarios', on_delete=models.CASCADE)

    aprobado = models.BooleanField(default=False)

    def aprobarComentario(self):

        self.aprobado = True
        self.save()





class RespuestaComentario(models.Model):

    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE) 

    contenido = models.TextField()

    tiempo_creacion = models.DateTimeField(default=timezone.now)    

    comentario = models.ForeignKey('Comentario', related_name='respuestaComentarios', on_delete=models.CASCADE)


