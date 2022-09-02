from django.contrib import admin
from .models import Categoria, Noticia, Comentario, RespuestaComentario

# Register your models here.

class CategoriaNoticiaAdmin(admin.ModelAdmin):

    list_display = ('categoria_nombre', )

admin.site.register(Categoria, CategoriaNoticiaAdmin)


class NoticiaAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'contenido', 'autor', 'imagen_ref',)

    list_filter = ('autor', ('categorias', admin.RelatedOnlyFieldListFilter), )

    list_editable = ('contenido',)

    list_per_page: 15

admin.site.register(Noticia, NoticiaAdmin)


class ComentarioNoticiaAdmin(admin.ModelAdmin):

    list_display = ('autor', 'noticia', 'aprobado',)

    list_filter = (('autor', admin.RelatedOnlyFieldListFilter), ('noticia', admin.RelatedOnlyFieldListFilter), 'aprobado')

    actions = ['aprobar']

    def aprobar(self, request, queryset):

        queryset.update(aprobado = True)


admin.site.register(Comentario, ComentarioNoticiaAdmin)



class RespuestaComentarioNoticiaAdmin(admin.ModelAdmin):

    list_display = ('autor', 'contenido', 'comentario',)

    list_filter = (('autor', admin.RelatedOnlyFieldListFilter), ('comentario', admin.RelatedOnlyFieldListFilter))


admin.site.register(RespuestaComentario, RespuestaComentarioNoticiaAdmin)