from django.contrib import admin
from .models import c_dispensacion_medicamentos,c_detalles_dispensacion, c_lotes_medicamentos,c_detalles_lotes
# Register your models here.

admin.site.register(c_dispensacion_medicamentos)
admin.site.register(c_detalles_dispensacion)
admin.site.register(c_lotes_medicamentos)
admin.site.register(c_detalles_lotes)
