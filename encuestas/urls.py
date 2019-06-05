from django.urls import path, include
from . import views

app_name = 'encuestas'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:encuesta_id>/voto/', views.voto, name='voto'),
    path('<int:pk>/', include([
        path('detalle/', views.DetalleView.as_view(), name='detalle'),
        path('resultados/', views.ResultadosView.as_view(), name='resultados'),
        ])),
    ]
