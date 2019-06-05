from django.contrib import admin
from .models import Encuesta, Opciones


# Register your models here.

class OpcionesInline(admin.TabularInline):
    model = Opciones
    extra = 3

class EncuestaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                {'fields': ['texto_encuesta']}),
        ('Info sobre fechas', {'fields': ['fecha_publicacion']}),
    ]
    inlines = [OpcionesInline]
    list_display = ('texto_encuesta', 'fecha_publicacion', 'es_reciente')
    list_filter = ['fecha_publicacion']
    search_fields = ['texto_encuesta']

admin.site.register(Encuesta, EncuestaAdmin)

admin.site.site_header = 'Gerardo TORDOYA'

