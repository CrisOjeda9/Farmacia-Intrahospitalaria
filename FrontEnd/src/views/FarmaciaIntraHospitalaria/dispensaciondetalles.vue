<template>
  <b-container fluid>
      
    <b-row>
      <b-col md="12">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Detalles de Dispensacion</h4>
          </template>
          <template v-slot:body>
           
            <div class="table-responsive">
              <table class="table table-striped table-bordered">
                <thead>
                  <tr>
                    <th v-for="data in columns" :key="data.field" :class="data.headerClass">
                      {{ data.label }}
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, index) in rows" :key="index">
                    <td>{{ item.id }}</td>
                    <td>{{ item.personalMedicoId }}</td>
                    <td>{{ item.recetaId }}</td>
                    <td>{{ item.nombreGenerico }}</td>
                    <td>{{ item.nombreComercial }}</td>
                    <td>{{ item.viaAdministrativa }}</td>
                    <td>{{ item.tipoPresentacion }}</td>
                    <td>{{ item.cantidadSolicitada }}</td>
                    <td>{{ item.precioUnitario }}</td>
                    <td>{{ item.cantidadEntregada }}</td>
                    <td>{{ item.importe }}</td>
                    <td>{{ item.fechaVenta }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
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
  name: 'UiDataTable',
  components: { iqCard },
  mounted() {
    xray.index()
  },
  data() {
    return {
      columns: [
        { label: 'ID', field: 'id', headerClass: 'text-left' },
        { label: 'Personal Médico ID', field: 'personalMedicoId', headerClass: 'text-left' },
        { label: 'Receta ID', field: 'recetaId', headerClass: 'text-left' },
        { label: 'Nombre Genérico', field: 'nombreGenerico', headerClass: 'text-left' },
        { label: 'Nombre Comercial', field: 'nombreComercial', headerClass: 'text-left' },
        { label: 'Vía Administrativa', field: 'viaAdministrativa', headerClass: 'text-left' },
        { label: 'Tipo de Presentación', field: 'tipoPresentacion', headerClass: 'text-left' },
        { label: 'Cantidad Solicitada', field: 'cantidadSolicitada', headerClass: 'text-left' },
        { label: 'Precio Unitario', field: 'precioUnitario', headerClass: 'text-left' },
        { label: 'Cantidad Entregada', field: 'cantidadEntregada', headerClass: 'text-left' },
        { label: 'Importe', field: 'importe', headerClass: 'text-left' },
        { label: 'Fecha de la Venta', field: 'fechaVenta', headerClass: 'text-left' }
      ],
      rows: []
    }
  },
  created() {
    this.generateData();
  },
  methods: {
    generateData() {
      const viasAdministracion = [
        'Oral', 'Intravenoso', 'Rectal', 'Cutáneo', 'Subcutáneo',
        'Oftálmico', 'Ótica', 'Nasal', 'Tópica', 'Parental', 'Vaginal'
      ];
      const tiposPresentacion = [
        'Grageas', 'Suspensión', 'Pomada', 'Jabón', 'Polvo', 'Supositorios',
        'Solución', 'Cápsulas', 'Parche', 'Jarabe', 'Gotas', 'Tabletas'
      ];
      for (let i = 1; i <= 50; i++) {
        const randomId = Math.random();
        const viaAdministrativa = viasAdministracion[Math.floor(Math.random() * viasAdministracion.length)];
        const tipoPresentacion = tiposPresentacion[Math.floor(Math.random() * tiposPresentacion.length)];
        if (randomId < 0.5) {
          this.rows.push({
            id: i,
            personalMedicoId: 'PM' + i,
            recetaId: null,
            nombreGenerico: 'Medicamento ' + i,
            nombreComercial: 'Comercial ' + i,
            viaAdministrativa: viaAdministrativa,
            tipoPresentacion: tipoPresentacion,
            cantidadSolicitada: this.getRandomInt(1, 20),
            precioUnitario: '$' + (Math.random() * (100 - 1) + 1).toFixed(2),
            cantidadEntregada: this.getRandomInt(1, 20),
            importe: '$' + (Math.random() * (1000 - 10) + 10).toFixed(2),
            fechaVenta: this.getRandomDate()
          });
        } else {
          this.rows.push({
            id: i,
            personalMedicoId: null,
            recetaId: 100 + i,
            nombreGenerico: 'Medicamento ' + i,
            nombreComercial: 'Comercial ' + i,
            viaAdministrativa: viaAdministrativa,
            tipoPresentacion: tipoPresentacion,
            cantidadSolicitada: this.getRandomInt(1, 20),
            precioUnitario: '$' + (Math.random() * (100 - 1) + 1).toFixed(2),
            cantidadEntregada: this.getRandomInt(1, 20),
            importe: '$' + (Math.random() * (1000 - 10) + 10).toFixed(2),
            fechaVenta: this.getRandomDate()
          });
      }
    }
  },
  getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  },
  getRandomDate() {
    const start = new Date(2019, 0, 1);
    const end = new Date();
    return new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime())).toISOString().split('T')[0];
  }
}
}
</script>
