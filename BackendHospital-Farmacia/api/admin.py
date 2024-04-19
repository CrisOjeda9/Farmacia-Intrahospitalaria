from django.contrib import admin
from .models import AreasMedicas, Bitacora, Citas, Departamentos, DetalleDispensacionRelacion, DetalleLotes, DetallesDispensacion, DispensacionMedicamentos, LotesMedicamentos, Medicamentos, Pacientes, PersonalMedico, Personas, RecetaMedica, RecetaMedicaDetalle

admin.site.register(AreasMedicas)
admin.site.register(Bitacora)
admin.site.register(Citas)
admin.site.register(Departamentos)
admin.site.register(DetalleDispensacionRelacion)
admin.site.register(DetalleLotes)
admin.site.register(DetallesDispensacion)
admin.site.register(DispensacionMedicamentos)
admin.site.register(LotesMedicamentos)
admin.site.register(Medicamentos)
admin.site.register(Pacientes)
admin.site.register(PersonalMedico)
admin.site.register(Personas)
admin.site.register(RecetaMedica)
admin.site.register(RecetaMedicaDetalle)
