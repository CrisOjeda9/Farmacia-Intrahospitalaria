from rest_framework import viewsets
from .models import AreasMedicas, Bitacora, Citas, Departamentos, DetalleDispensacionRelacion, DetalleLotes, DetallesDispensacion, DispensacionMedicamentos, LotesMedicamentos, Medicamentos, Pacientes, PersonalMedico, Personas, RecetaMedica, RecetaMedicaDetalle
from .serializer import AreasMedicasSerializer, BitacoraSerializer, CitasSerializer, DepartamentosSerializer, DetalleDispensacionRelacionSerializer, DetalleLotesSerializer, DetallesDispensacionSerializer, DispensacionMedicamentosSerializer, LotesMedicamentosSerializer, MedicamentosSerializer, PacientesSerializer, PersonalMedicoSerializer, PersonasSerializer, RecetaMedicaSerializer, RecetaMedicaDetalleSerializer


class AreasMedicasViewSet(viewsets.ModelViewSet):
    queryset = AreasMedicas.objects.all()
    serializer_class = AreasMedicasSerializer


class BitacoraViewSet(viewsets.ModelViewSet):
    queryset = Bitacora.objects.all()
    serializer_class = BitacoraSerializer


class CitasViewSet(viewsets.ModelViewSet):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer


class DepartamentosViewSet(viewsets.ModelViewSet):
    queryset = Departamentos.objects.all()
    serializer_class = DepartamentosSerializer


class DetalleDispensacionRelacionViewSet(viewsets.ModelViewSet):
    queryset = DetalleDispensacionRelacion.objects.all()
    serializer_class = DetalleDispensacionRelacionSerializer


class DetalleLotesViewSet(viewsets.ModelViewSet):
    queryset = DetalleLotes.objects.all()
    serializer_class = DetalleLotesSerializer


class DetallesDispensacionViewSet(viewsets.ModelViewSet):
    queryset = DetallesDispensacion.objects.all()
    serializer_class = DetallesDispensacionSerializer


class DispensacionMedicamentosViewSet(viewsets.ModelViewSet):
    queryset = DispensacionMedicamentos.objects.all()
    serializer_class = DispensacionMedicamentosSerializer


class LotesMedicamentosViewSet(viewsets.ModelViewSet):
    queryset = LotesMedicamentos.objects.all()
    serializer_class = LotesMedicamentosSerializer


class MedicamentosViewSet(viewsets.ModelViewSet):
    queryset = Medicamentos.objects.all()
    serializer_class = MedicamentosSerializer


class PacientesViewSet(viewsets.ModelViewSet):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer


class PersonalMedicoViewSet(viewsets.ModelViewSet):
    queryset = PersonalMedico.objects.all()
    serializer_class = PersonalMedicoSerializer


class PersonasViewSet(viewsets.ModelViewSet):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer


class RecetaMedicaViewSet(viewsets.ModelViewSet):
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer


class RecetaMedicaDetalleViewSet(viewsets.ModelViewSet):
    queryset = RecetaMedicaDetalle.objects.all()
    serializer_class = RecetaMedicaDetalleSerializer
