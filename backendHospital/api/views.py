from rest_framework import viewsets
from .models import c_dispensacion_medicamentos,c_detalles_dispensacion,c_lotes_medicamentos,c_detalles_lotes
from .serializer import c_dispensacionSerializer,c_detalles_dispensacionSerializer,c_lotesSerializer,c_detalles_lotesSerializer

class c_dispensacionViewSet(viewsets.ModelViewSet):
	queryset = c_dispensacion_medicamentos.objects.all()
	serializer_class = c_dispensacionSerializer

class c_detalles_dispensacionViewSet(viewsets.ModelViewSet):
	queryset = c_detalles_dispensacion.objects.all()
	serializer_class = c_detalles_dispensacionSerializer

class c_lotes_medicamentoViewSet(viewsets.ModelViewSet):
	queryset = c_lotes_medicamentos.objects.all()
	serializer_class = c_lotesSerializer

class c_detalles_lotes_medicamentoViewSet(viewsets.ModelViewSet):
	queryset = c_detalles_lotes.objects.all()
	serializer_class = c_detalles_lotesSerializer
