from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'c_dispensacion_medicamentos', views.c_dispensacionViewSet)
router.register(r'c_detalles_dispensacion', views.c_detalles_dispensacionViewSet)
router.register(r'c_lotes_medicamentos', views.c_lotes_medicamentoViewSet)
router.register(r'c_detalles_lotes', views.c_detalles_lotes_medicamentoViewSet)

urlpatterns = [
	path('api/v1',include(router.urls))
]

