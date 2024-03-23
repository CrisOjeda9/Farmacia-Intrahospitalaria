<template>
  <b-container fluid>
    <b-row>
      <!-- Contratación de personal -->
      <b-col lg="6">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Contratación de Personal</h4>
          </template>
          <template v-slot:body>
            <p>Publicación de vacantes, proceso de selección de candidatos, entrevistas, revisión de currículums.</p>
          </template>
        </iq-card>
      </b-col>

      <!-- Capacitación y desarrollo profesional -->
      <b-col lg="6">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Capacitación y Desarrollo Profesional</h4>
          </template>
          <template v-slot:body>
            <p>Programas de formación, cursos de actualización, planes de carrera para empleados.</p>
          </template>
        </iq-card>
      </b-col>

      <!-- Gestión de nómina y beneficios -->
      <b-col lg="6">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Gestión de Nómina y Beneficios</h4>
          </template>
          <template v-slot:body>
            <p>Procesamiento de pagos, administración de beneficios como seguro médico y bonos.</p>
          </template>
        </iq-card>
      </b-col>

      <!-- Administración de registros de empleados -->
      <b-col lg="6">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Administración de Registros de Empleados</h4>
          </template>
          <template v-slot:body>
            <p>Mantenimiento de expedientes, actualización de información personal y laboral.</p>
          </template>
        </iq-card>
      </b-col>

      <!-- Implementación y seguimiento de políticas laborales -->
      <b-col lg="6">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Implementación y Seguimiento de Políticas Laborales</h4>
          </template>
          <template v-slot:body>
            <p>Aplicación de normativas internas, comunicación de políticas y procedimientos.</p>
          </template>
        </iq-card>
      </b-col>

      <!-- Manejo de relaciones laborales y resolución de conflictos -->
      <b-col lg="6">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Manejo de Relaciones Laborales y Resolución de Conflictos</h4>
          </template>
          <template v-slot:body>
            <p>Mediación en disputas, promoción de un ambiente laboral saludable y colaborativo.</p>
          </template>
        </iq-card>
      </b-col>

      <!-- Evaluación del desempeño y programas de retroalimentación -->
      <b-col lg="6">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Evaluación del Desempeño y Programas de Retroalimentación</h4>
          </template>
          <template v-slot:body>
            <p>Revisiones periódicas, establecimiento de metas, retroalimentación constructiva.</p>
          </template>
        </iq-card>
      </b-col>

      <!-- Diseño e implementación de programas de bienestar y salud ocupacional -->
      <b-col lg="6">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Diseño e Implementación de Programas de Bienestar y Salud Ocupacional</h4>
          </template>
          <template v-slot:body>
            <p>Actividades de bienestar, promoción de estilos de vida saludables, prevención de accidentes laborales.</p>
          </template>
        </iq-card>
      </b-col>

      <!-- Coordinación de horarios y turnos de trabajo -->
      <b-col lg="6">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Coordinación de Horarios y Turnos de Trabajo</h4>
          </template>
          <template v-slot:body>
            <p>Elaboración de horarios, asignación de turnos, gestión de vacaciones y permisos.</p>
          </template>
        </iq-card>
      </b-col>

      <!-- Cumplimiento legal y normativo en materia laboral y de recursos humanos -->
      <b-col lg="6">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Cumplimiento Legal y Normativo en Materia Laboral y de Recursos Humanos</h4>
          </template>
          <template v-slot:body>
            <p>Seguimiento de leyes laborales, cumplimiento de regulaciones gubernamentales, gestión de documentación.</p>
          </template>
        </iq-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { xray } from '../../config/pluginInit'
import iqCard from '../../components/xray/cards/iq-card'

export default {
  name: 'RecursosHumanos',
  components: { iqCard },
  mounted() {
    xray.index()
  },
  // datos o lógica necesaria
}
</script>
