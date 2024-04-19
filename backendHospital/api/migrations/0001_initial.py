# Generated by Django 5.0.1 on 2024-04-19 07:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreasMedicas',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=150)),
                ('descripcion', models.TextField(blank=True, db_column='Descripcion', null=True)),
                ('estatus', models.TextField(blank=True, db_column='Estatus', null=True)),
                ('fecha_registro', models.DateTimeField(db_column='Fecha_Registro')),
                ('fecha_actualizacion', models.DateTimeField(blank=True, db_column='Fecha_Actualizacion', null=True)),
            ],
            options={
                'db_table': 'areas_medicas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre_tabla', models.CharField(db_column='Nombre_Tabla', max_length=80)),
                ('usuario', models.CharField(db_column='Usuario', max_length=80)),
                ('operacion', models.CharField(db_column='Operacion', max_length=6)),
                ('descripcion', models.TextField(db_column='Descripcion')),
                ('fecha_hora', models.DateTimeField(db_column='Fecha_Hora')),
            ],
            options={
                'db_table': 'bitacora',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('fecha_cita', models.DateTimeField(db_column='Fecha_Cita')),
            ],
            options={
                'db_table': 'citas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=100)),
                ('responsable_id', models.PositiveIntegerField(blank=True, db_column='Responsable_ID', null=True)),
                ('estatus', models.TextField(db_column='Estatus')),
                ('fecha_registro', models.DateTimeField(db_column='Fecha_Registro')),
                ('fecha_actualizacion', models.DateTimeField(blank=True, db_column='Fecha_Actualizacion', null=True)),
            ],
            options={
                'db_table': 'departamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispensacionMedicamentos',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('fecha_registro', models.DateTimeField(db_column='Fecha_Registro')),
                ('total_medicamentos_solicitados', models.PositiveIntegerField(db_column='Total_Medicamentos_Solicitados')),
                ('total_medicamentos_entregados', models.PositiveIntegerField(db_column='Total_Medicamentos_Entregados')),
                ('estatus', models.CharField(blank=True, db_column='Estatus', max_length=23, null=True)),
            ],
            options={
                'db_table': 'dispensacion_medicamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LotesMedicamentos',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(db_column='Descripcion', max_length=300)),
                ('cantidad', models.PositiveIntegerField(db_column='Cantidad')),
                ('precio_unitario', models.DecimalField(db_column='Precio_unitario', decimal_places=2, max_digits=10)),
                ('fecha_solicitud', models.DateField(db_column='Fecha_solicitud')),
                ('fecha_ingreso', models.DateTimeField(db_column='Fecha_ingreso')),
            ],
            options={
                'db_table': 'lotes_medicamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medicamentos',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre_comercial', models.CharField(db_column='Nombre_Comercial', max_length=250)),
                ('nombre_generico', models.CharField(db_column='Nombre_Generico', max_length=250)),
                ('via_administracion', models.CharField(blank=True, db_column='Via_Administracion', max_length=11, null=True)),
                ('presentacion', models.CharField(blank=True, db_column='Presentacion', max_length=12, null=True)),
                ('estatus', models.TextField(blank=True, db_column='Estatus', null=True)),
                ('cantidad', models.CharField(db_column='Cantidad', max_length=45)),
            ],
            options={
                'db_table': 'medicamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('titulo', models.CharField(blank=True, db_column='Titulo', max_length=20, null=True)),
                ('nombre', models.CharField(db_column='Nombre', max_length=80)),
                ('primer_apellido', models.CharField(db_column='Primer_Apellido', max_length=80)),
                ('segundo_apellido', models.CharField(blank=True, db_column='Segundo_Apellido', max_length=80, null=True)),
                ('curp', models.CharField(blank=True, db_column='CURP', max_length=18, null=True, unique=True)),
                ('genero', models.CharField(db_column='Genero', max_length=3)),
                ('grupo_sanguineo', models.CharField(db_column='Grupo_Sanguineo', max_length=2)),
                ('tipo_sanguineo', models.CharField(db_column='Tipo_Sanguineo', max_length=1)),
                ('fecha_nacimiento', models.DateField(db_column='Fecha_Nacimiento')),
                ('estatus', models.TextField(db_column='Estatus')),
                ('fecha_registro', models.DateTimeField(db_column='Fecha_Registro')),
                ('fecha_actualizacion', models.DateTimeField(blank=True, db_column='Fecha_Actualizacion', null=True)),
            ],
            options={
                'db_table': 'personas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecetaMedica',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('fecha_hora_registro', models.DateTimeField(db_column='FECHA_HORA_REGISTRO')),
                ('estatus', models.CharField(blank=True, db_column='ESTATUS', max_length=23, null=True)),
            ],
            options={
                'db_table': 'receta_medica',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecetaMedicaDetalle',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('dosis', models.CharField(db_column='DOSIS', max_length=1024)),
                ('recomendaciones', models.CharField(blank=True, db_column='RECOMENDACIONES', max_length=1024, null=True)),
            ],
            options={
                'db_table': 'receta_medica_detalle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleDispensacionRelacion',
            fields=[
                ('dispensacion', models.OneToOneField(db_column='Dispensacion_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.dispensacionmedicamentos')),
                ('estatus', models.CharField(blank=True, db_column='Estatus', max_length=11, null=True)),
            ],
            options={
                'db_table': 'detalle_dispensacion_relacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetallesDispensacion',
            fields=[
                ('dispensacion', models.OneToOneField(db_column='Dispensacion_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.dispensacionmedicamentos')),
                ('cantidad_entregada', models.PositiveIntegerField(db_column='Cantidad_Entregada')),
                ('precio_unitario', models.DecimalField(db_column='Precio_Unitario', decimal_places=2, max_digits=10)),
                ('precio_total', models.DecimalField(db_column='Precio_Total', decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'detalles_dispensacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleLotes',
            fields=[
                ('lotes', models.OneToOneField(db_column='Lotes_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.lotesmedicamentos')),
                ('codigo', models.CharField(db_column='Codigo', max_length=6)),
                ('marca', models.CharField(db_column='Marca', max_length=200)),
                ('fecha_vencimiento', models.DateField()),
                ('precio_unitario', models.DecimalField(db_column='Precio_unitario', decimal_places=2, max_digits=10)),
                ('estatus', models.CharField(blank=True, db_column='Estatus', max_length=13, null=True)),
            ],
            options={
                'db_table': 'detalle_lotes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('persona', models.OneToOneField(db_column='Persona_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.personas')),
                ('nss', models.CharField(blank=True, db_column='NSS', max_length=15, null=True, unique=True)),
                ('tipo_seguro', models.CharField(db_column='Tipo_Seguro', max_length=50)),
                ('fecha_registro', models.DateTimeField(db_column='Fecha_Registro')),
                ('fecha_ultimacita', models.DateTimeField(db_column='Fecha_UltimaCita')),
                ('estatus_medico', models.CharField(blank=True, db_column='Estatus_Medico', max_length=100, null=True)),
                ('estatus_vida', models.CharField(db_column='Estatus_Vida', max_length=10)),
                ('estatus', models.TextField(blank=True, db_column='Estatus', null=True)),
            ],
            options={
                'db_table': 'pacientes',
                'db_table_comment': '\t',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PersonalMedico',
            fields=[
                ('persona', models.OneToOneField(db_column='Persona_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.personas')),
                ('especialidad', models.CharField(blank=True, db_column='Especialidad', max_length=50, null=True)),
                ('tipo', models.CharField(db_column='Tipo', max_length=14)),
                ('cedula_profesional', models.IntegerField(blank=True, db_column='Cedula_Profesional', null=True, unique=True)),
                ('estatus', models.CharField(db_column='Estatus', max_length=8)),
                ('fecha_contratacion', models.DateTimeField(db_column='Fecha_Contratacion')),
                ('fecha_terminacion_contrato', models.DateTimeField(blank=True, db_column='Fecha_Terminacion_Contrato', null=True)),
            ],
            options={
                'db_table': 'personal_medico',
                'managed': False,
            },
        ),
    ]
