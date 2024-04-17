from django.db import models


class AreasMedicas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=150)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    estatus = models.TextField(db_column='Estatus', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecha_registro = models.DateTimeField(db_column='Fecha_Registro')  # Field name made lowercase.
    fecha_actualizacion = models.DateTimeField(db_column='Fecha_Actualizacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'areas_medicas'


class Bitacora(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_tabla = models.CharField(db_column='Nombre_Tabla', max_length=80)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=80)  # Field name made lowercase.
    operacion = models.CharField(db_column='Operacion', max_length=6)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion')  # Field name made lowercase.
    fecha_hora = models.DateTimeField(db_column='Fecha_Hora')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bitacora'


class Citas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    

    class Meta:
        managed = False
        db_table = 'citas'


class Departamentos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.
    areamedica = models.ForeignKey(AreasMedicas, models.DO_NOTHING, db_column='AreaMedica_ID', blank=True, null=True)  # Field name made lowercase.
    departamento_superior = models.ForeignKey('self', models.DO_NOTHING, db_column='Departamento_Superior_ID', blank=True, null=True)  # Field name made lowercase.
    responsable_id = models.PositiveIntegerField(db_column='Responsable_ID', blank=True, null=True)  # Field name made lowercase.
    estatus = models.TextField(db_column='Estatus')  # Field name made lowercase. This field type is a guess.
    fecha_registro = models.DateTimeField(db_column='Fecha_Registro')  # Field name made lowercase.
    fecha_actualizacion = models.DateTimeField(db_column='Fecha_Actualizacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamentos'


class DetalleDispensacionRelacion(models.Model):
    dispensacion = models.OneToOneField('DispensacionMedicamentos', models.DO_NOTHING, db_column='Dispensacion_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Dispensacion_ID, Detalle_Dispensacion_ID) found, that is not supported. The first column is selected.
    detalle_dispensacion = models.ForeignKey('DetallesDispensacion', models.DO_NOTHING, db_column='Detalle_Dispensacion_ID')  # Field name made lowercase.
    estatus = models.CharField(db_column='Estatus', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_dispensacion_relacion'
        unique_together = (('dispensacion', 'detalle_dispensacion'),)


class DetalleLotes(models.Model):
    lotes = models.OneToOneField('LotesMedicamentos', models.DO_NOTHING, db_column='Lotes_ID', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=6)  # Field name made lowercase.
    medicamento = models.ForeignKey('Medicamentos', models.DO_NOTHING, db_column='Medicamento_ID')  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=200)  # Field name made lowercase.
    fecha_vencimiento = models.DateField()
    precio_unitario = models.DecimalField(db_column='Precio_unitario', max_digits=10, decimal_places=2)  # Field name made lowercase.
    estatus = models.CharField(db_column='Estatus', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_lotes'


class DetallesDispensacion(models.Model):
    dispensacion = models.OneToOneField('DispensacionMedicamentos', models.DO_NOTHING, db_column='Dispensacion_ID', primary_key=True)  # Field name made lowercase.
    detalle_receta = models.ForeignKey('RecetaMedicaDetalle', models.DO_NOTHING, db_column='Detalle_Receta_ID')  # Field name made lowercase.
    cantidad_entregada = models.PositiveIntegerField(db_column='Cantidad_Entregada')  # Field name made lowercase.
    precio_unitario = models.DecimalField(db_column='Precio_Unitario', max_digits=10, decimal_places=2)  # Field name made lowercase.
    precio_total = models.DecimalField(db_column='Precio_Total', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalles_dispensacion'


class DispensacionMedicamentos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    receta = models.ForeignKey('RecetaMedica', models.DO_NOTHING, db_column='Receta_ID')  # Field name made lowercase.
    personal_medico = models.ForeignKey('PersonalMedico', models.DO_NOTHING, db_column='Personal_Medico_ID')  # Field name made lowercase.
    fecha_registro = models.DateTimeField(db_column='Fecha_Registro')  # Field name made lowercase.
    total_medicamentos_solicitados = models.PositiveIntegerField(db_column='Total_Medicamentos_Solicitados')  # Field name made lowercase.
    total_medicamentos_entregados = models.PositiveIntegerField(db_column='Total_Medicamentos_Entregados')  # Field name made lowercase.
    estatus = models.CharField(db_column='Estatus', max_length=23, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dispensacion_medicamentos'


class LotesMedicamentos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=300)  # Field name made lowercase.
    cantidad = models.PositiveIntegerField(db_column='Cantidad')  # Field name made lowercase.
    precio_unitario = models.DecimalField(db_column='Precio_unitario', max_digits=10, decimal_places=2)  # Field name made lowercase.
    fecha_solicitud = models.DateField(db_column='Fecha_solicitud')  # Field name made lowercase.
    fecha_ingreso = models.DateTimeField(db_column='Fecha_ingreso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lotes_medicamentos'


class Medicamentos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_comercial = models.CharField(db_column='Nombre_Comercial', max_length=250)  # Field name made lowercase.
    nombre_generico = models.CharField(db_column='Nombre_Generico', max_length=250)  # Field name made lowercase.
    via_administracion = models.CharField(db_column='Via_Administracion', max_length=11, blank=True, null=True)  # Field name made lowercase.
    presentacion = models.CharField(db_column='Presentacion', max_length=12, blank=True, null=True)  # Field name made lowercase.
    estatus = models.BooleanField(db_column='Estatus', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cantidad = models.CharField(db_column='Cantidad', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicamentos'


class Pacientes(models.Model):
    persona = models.OneToOneField('Personas', models.DO_NOTHING, db_column='Persona_ID', primary_key=True)  # Field name made lowercase.
    nss = models.CharField(db_column='NSS', unique=True, max_length=15, blank=True, null=True)  # Field name made lowercase.
    tipo_seguro = models.CharField(db_column='Tipo_Seguro', max_length=50)  # Field name made lowercase.
    fecha_registro = models.DateTimeField(db_column='Fecha_Registro')  # Field name made lowercase.
    fecha_ultimacita = models.DateTimeField(db_column='Fecha_UltimaCita')  # Field name made lowercase.
    estatus_medico = models.CharField(db_column='Estatus_Medico', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estatus_vida = models.CharField(db_column='Estatus_Vida', max_length=10)  # Field name made lowercase.
    estatus = models.TextField(db_column='Estatus', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pacientes'
        db_table_comment = '\t'


class PersonalMedico(models.Model):
    persona = models.OneToOneField('Personas', models.DO_NOTHING, db_column='Persona_ID', primary_key=True)  # Field name made lowercase.
    departamento = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='Departamento_ID')  # Field name made lowercase.
    especialidad = models.CharField(db_column='Especialidad', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=14)  # Field name made lowercase.
    cedula_profesional = models.IntegerField(db_column='Cedula_Profesional', unique=True, blank=True, null=True)  # Field name made lowercase.
    estatus = models.CharField(db_column='Estatus', max_length=8)  # Field name made lowercase.
    fecha_contratacion = models.DateTimeField(db_column='Fecha_Contratacion')  # Field name made lowercase.
    fecha_terminacion_contrato = models.DateTimeField(db_column='Fecha_Terminacion_Contrato', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personal_medico'


class Personas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=80)  # Field name made lowercase.
    primer_apellido = models.CharField(db_column='Primer_Apellido', max_length=80)  # Field name made lowercase.
    segundo_apellido = models.CharField(db_column='Segundo_Apellido', max_length=80, blank=True, null=True)  # Field name made lowercase.
    curp = models.CharField(db_column='CURP', unique=True, max_length=18, blank=True, null=True)  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=3)  # Field name made lowercase.
    grupo_sanguineo = models.CharField(db_column='Grupo_Sanguineo', max_length=2)  # Field name made lowercase.
    tipo_sanguineo = models.CharField(db_column='Tipo_Sanguineo', max_length=1)  # Field name made lowercase.
    fecha_nacimiento = models.DateField(db_column='Fecha_Nacimiento')  # Field name made lowercase.
    estatus = models.TextField(db_column='Estatus')  # Field name made lowercase. This field type is a guess.
    fecha_registro = models.DateTimeField(db_column='Fecha_Registro')  # Field name made lowercase.
    fecha_actualizacion = models.DateTimeField(db_column='Fecha_Actualizacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personas'


class RecetaMedica(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cita = models.ForeignKey(Citas, models.DO_NOTHING, db_column='CITA_ID')  # Field name made lowercase.
    fecha_hora_registro = models.DateTimeField(db_column='FECHA_HORA_REGISTRO')  # Field name made lowercase.
    estatus = models.CharField(db_column='ESTATUS', max_length=23, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'receta_medica'


class RecetaMedicaDetalle(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    receta = models.ForeignKey(RecetaMedica, models.DO_NOTHING)
    medicamento = models.ForeignKey(Medicamentos, models.DO_NOTHING, db_column='MEDICAMENTO_ID')  # Field name made lowercase.
    dosis = models.CharField(db_column='DOSIS', max_length=1024)  # Field name made lowercase.
    recomendaciones = models.CharField(db_column='RECOMENDACIONES', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'receta_medica_detalle'
