from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Encuesta, Opciones


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'encuestas/index.html'
    context_object_name = 'lista_recientes'

    def get_queryset(self):
        return Encuesta.objects.filter(
            fecha_publicacion__lte=timezone.now()
            ).order_by('-fecha_publicacion')[:5]


class DetalleView(generic.DetailView):
        model = Encuesta
        template_name = 'encuestas/detalle.html'

        def get_queryset(self):
            return Encuesta.objects.filter(fecha_publicacion__lte=timezone.now())


class ResultadosView(generic.DetailView):
    model = Encuesta
    template_name =  'encuestas/resultados.html'


def voto(request, encuesta_id):
    encuesta = get_object_or_404(Encuesta, pk=encuesta_id)
    try:
        opcion_elegida = encuesta.opciones_set.get(pk=request.POST['opcion'])
    except (KeyError, Opciones.DoesNotExist):
        return render(request, 'encuestas/detalle.html', {
            'encuesta': encuesta,
            'mensaje_error': "No has elegido nada",
        })
    else:
        opcion_elegida.los_votos += 1
        opcion_elegida.save()
        return HttpResponseRedirect(reverse('encuestas:resultados', args=(encuesta.id,)))
