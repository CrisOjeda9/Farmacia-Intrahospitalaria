from rest_framework import serializers
from .models import  c_dispensacion_medicamentos,c_detalles_dispensacion, c_lotes_medicamentos,c_detalles_lotes
  
#Modelo de farmacia  

class c_dispensacionSerializer(serializers.ModelSerializer):  
    class Meta:
        model = c_dispensacion_medicamentos
        fields = '__all__'
class c_detalles_dispensacionSerializer(serializers.ModelSerializer):  
    class Meta:
        model = c_detalles_dispensacion
        fields = '__all__'
  
class c_lotesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = c_lotes_medicamentos
        fields = '__all__'
        
class c_detalles_lotesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = c_detalles_lotes
        fields = '__all__'
 