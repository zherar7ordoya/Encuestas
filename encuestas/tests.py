import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Encuesta


# Create your tests here.

class EncuestaModelTests(TestCase):

    def publicado_recientemente_con_fecha_futura(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        momento = timezone.now() + datetime.timedelta(days=30)
        encuesta_futura = Encuesta(fecha_publicacion=momento)
        self.assertIs(encuesta_futura.es_reciente(), False)
