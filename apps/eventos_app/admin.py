from datetime import datetime
from django.contrib import admin
from .models import CategoriaEvento, Evento
from django.utils import timezone
from datetime import datetime
from django.utils.safestring import mark_safe

# Register your models here.

'''
admin.site.register(CategoriaEvento)

admin.site.register(Evento)
'''

admin.site.empty_value_display = '(None)'


class CategoriaEventoAdmin(admin.ModelAdmin):

    list_display = ('categoria_nombre',)

admin.site.register(CategoriaEvento, CategoriaEventoAdmin)


class EventoAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'autor', 'imagen_ref', 'horario_comienzo_evento', 'lugar_evento', )

    list_filter = ('autor', 'categorias')

    list_editable = ('horario_comienzo_evento', 'lugar_evento',)

    readonly_fields = ['evento_img']

    def evento_img(self, obj):

        return mark_safe(
            '<a href="{0}"><img src="{0}" width="30%"></a>'.format(self.img.url)
        )



    list_per_page: 15

admin.site.register(Evento, EventoAdmin)