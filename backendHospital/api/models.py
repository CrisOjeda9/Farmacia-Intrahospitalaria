from django.db import models

# Create your models here.

# Modelo Farmacia Intrahospitalaria ------------------------------------------


class c_dispensacion_medicamentos(models.Model):
    # di_ID = models.AutoField(primary_key=True)
    Personal_Medico_ID = models.CharField(max_length=15)
    Receta_ID = models.CharField(max_length=15)
    Fecha_Registro = models.DateTimeField(auto_now_add=True)
    Total_Medicamentos_Solicitados = models.IntegerField()
    Total_Medicamentos_Entregados = models.IntegerField()  

    # Definir la enumeración para el campo de estado
    class Estado(models.TextChoices):
        DISPONIBLE = 'Disponible'
        NO_DISPONIBLE = 'No Disponible'

    # Agregar el campo de estado con las opciones de la enumeración
    di_estatus = models.CharField(max_length=15, choices=Estado.choices, default=Estado.DISPONIBLE)

    def __str__(self):
        return str(self.Receta_ID)

    


class c_detalles_dispensacion(models.Model):
    Dispensacion_ID = models.CharField(max_length=15)
    Detalle_Receta_ID = models.CharField(max_length=15)
    Fecha_Entrega = models.DateTimeField(auto_now_add=True)  
    Cantidad_Entregada = models.IntegerField()  
    Precio_Unitario = models.DecimalField(max_digits=10, decimal_places=2)
    Precio_Total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.Dispensacion_ID)



class c_lotes_medicamentos(models.Model):
    Medicamento_ID = models.CharField(max_length=15)
    Descripcion = models.CharField(max_length=15)
    Cantidad = models.IntegerField()  
    fecha_vencimiento = models.DateField() 
    fecha_ingreso = models.DateField(auto_now_add=True) 
   
    def __str__(self):
        return str(self.Medicamento_ID)

class c_detalles_lotes(models.Model):
    Lotes_ID = models.CharField(max_length=15)
    Codigo = models.CharField(max_length=15)
    Marca = models.CharField(max_length=50)  
    Precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)  
    Estatus = models.CharField(max_length=15)
   
    def __str__(self):
        return str(self.Lotes_ID)
