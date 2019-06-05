import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Encuesta(models.Model):
    texto_encuesta = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('Fecha de publicación')
    
    def __str__(self):
        return self.texto_encuesta

    def es_reciente(self):
        es_ahora = timezone.now()
        return es_ahora - datetime.timedelta(days=3) <= self.fecha_publicacion <= es_ahora
        # return self.fecha_publicacion >= timezone.now() - datetime.timedelta(days=3)

    es_reciente.admin_order_field = 'fecha_publicacion'
    es_reciente.boolean = True
    es_reciente.short_description = '¿Publicado recientemente?'


class Opciones(models.Model):
    la_encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    texto_opcion = models.CharField(max_length=200)
    los_votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_opcion
