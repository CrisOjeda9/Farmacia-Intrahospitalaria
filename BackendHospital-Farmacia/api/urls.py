from django.urls import path,include
from rest_framework import routers
from api import views

# Define el enrutador
router = routers.DefaultRouter()

# Registra cada vista de conjunto de vistas con el enrutador
router.register(r'areas_medicas', views.AreasMedicasViewSet)
router.register(r'bitacora', views.BitacoraViewSet)
router.register(r'citas', views.CitasViewSet)
router.register(r'departamentos', views.DepartamentosViewSet)
router.register(r'detalle_dispensacion_relacion', views.DetalleDispensacionRelacionViewSet)
router.register(r'detalle_lotes', views.DetalleLotesViewSet)
router.register(r'detalles_dispensacion', views.DetallesDispensacionViewSet)
router.register(r'dispensacion_medicamentos', views.DispensacionMedicamentosViewSet)
router.register(r'lotes_medicamentos', views.LotesMedicamentosViewSet)
router.register(r'medicamentos', views.MedicamentosViewSet)
router.register(r'pacientes', views.PacientesViewSet)
router.register(r'personal_medico', views.PersonalMedicoViewSet)
router.register(r'personas', views.PersonasViewSet)
router.register(r'receta_medica', views.RecetaMedicaViewSet)
router.register(r'receta_medica_detalle', views.RecetaMedicaDetalleViewSet)

# Define las URL con el prefijo 'api/v1/' e incluye las URLs generadas por el enrutador
urlpatterns = [
	path('api/v1',include(router.urls))
]


