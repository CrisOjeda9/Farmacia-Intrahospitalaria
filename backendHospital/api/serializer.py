from rest_framework import serializers
from .models import AreasMedicas, Bitacora, Citas, Departamentos, DetalleDispensacionRelacion, DetalleLotes, DetallesDispensacion, DispensacionMedicamentos, LotesMedicamentos, Medicamentos, Pacientes, PersonalMedico, Personas, RecetaMedica, RecetaMedicaDetalle

class AreasMedicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasMedicas
        fields = '__all__'

class BitacoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bitacora
        fields = '__all__'

class CitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields = '__all__'

class DepartamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamentos
        fields = '__all__'

class DetalleDispensacionRelacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleDispensacionRelacion
        fields = '__all__'

class DetalleLotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleLotes
        fields = '__all__'

class DetallesDispensacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallesDispensacion
        fields = '__all__'

class DispensacionMedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispensacionMedicamentos
        fields = '__all__'

class LotesMedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotesMedicamentos
        fields = '__all__'

class MedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamentos
        fields = '__all__'

class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'

class PersonalMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalMedico
        fields = '__all__'

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = '__all__'

class RecetaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaMedica
        fields = '__all__'

class RecetaMedicaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaMedicaDetalle
        fields = '__all__'
