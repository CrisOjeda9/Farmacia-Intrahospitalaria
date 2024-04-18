<template>
  <div>
    <!-- Card 1 -->
    <b-row>
      <b-col sm="6">
        <b-card title="Dispensación de Recetas" class="iq-mb-3">
          <b-card-text>Es un hecho establecido de hace mucho tiempo que un lector se distraerá con el contenido legible de una página cuando mire su diseño.</b-card-text>
          <b-button href="farmintra" block variant="btn btn-primary w-100" @click="handleCardButtonClick">Ir</b-button>
        </b-card>
      </b-col>
      <b-col sm="6">
        <b-card title="Control Inventario" class="iq-mb-3">
          <b-card-text>Es un hecho establecido de hace mucho tiempo que un lector se distraerá con el contenido legible de una página cuando mire su diseño.</b-card-text>
          <b-button href="farmintraInv" block variant="btn btn-primary w-100" @click="handleCardButtonClick">Ir</b-button>
        </b-card>
      </b-col>
    </b-row>
  </div>
  <b-container fluid>
    <b-row>
      <b-col lg="6">
        <iq-card>
          <template v-slot:headerTitle>
            <h4>{{ chartTitle }}</h4>
          </template>
          <template v-slot:body>
            <ApexChart :element="chartType" :chartOption="chartOptions" />
          </template>
        </iq-card>
      </b-col>
      <!-- Nueva tabla para los medicamentos más solicitados -->
      <b-col lg="6">
        <iq-card>
          <template v-slot:headerTitle>
            <h4>Medicamentos más solicitados</h4>
          </template>
          <template v-slot:body>
            <canvas id="medChart" width="400" height="350"></canvas>
          </template>
        </iq-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { xray } from '../../config/pluginInit'
import iqCard from '../../components/xray/cards/iq-card'
import ApexChart from '../../components/xray/charts/ApexChart'
import axios from 'axios'
import Chart from 'chart.js/auto'

export default {
  name: 'ApexCharts',
  components: { iqCard, ApexChart },
  data() {
    return {
      chartTitle: 'Costos y ganancias en la compra y venta de medicamentos',
      chartType: 'bar',
      chartOptions: {
        chart: {
          height: 350,
          type: 'bar',
          stacked: true
        },
        plotOptions: {
          bar: {
            horizontal: false
          }
        },
        dataLabels: {
          enabled: true,
          formatter: function (val) {
            return '$' + val.toFixed(2);
          },
          offsetY: -20,
          style: {
            fontSize: '12px',
            colors: ['#304758']
          }
        },
        xaxis: {
          categories: ['Costos', 'Ganancias']
        },
        series: [
          {
            name: 'Costos',
            data: []
          },
          {
            name: 'Ganancias',
            data: []
          }
        ]
      }
    }
  },
  mounted() {
    xray.index();
    this.fetchData();
    this.createPieChart();
  },
  methods: {
    async fetchData() {
      try {
        // Obtener datos de la API de lotes de medicamentos
        const responseMedicamentos = await axios.get('http://127.0.0.1:8000/hospital/api/v1lotes_medicamentos/');
        const medicamentosData = responseMedicamentos.data;

        // Calcular la suma de precios unitarios de medicamentos
        const totalPriceMedicamentos = medicamentosData.reduce((total, medicamento) => total + parseFloat(medicamento.precio_unitario), 0);

        // Obtener datos de la API de detalles de dispensación
        const responseDispensacion = await axios.get('http://127.0.0.1:8000/hospital/api/v1detalles_dispensacion/');
        const dispensacionData = responseDispensacion.data;

        // Calcular la suma de precios totales de dispensación
        const totalPriceDispensacion = dispensacionData.reduce((total, detalle) => total + parseFloat(detalle.precio_total), 0);

        // Actualizar los datos de la gráfica
        this.chartOptions.series[0].data = [totalPriceMedicamentos, 0]; // El segundo valor (0) es para la dispensación
        this.chartOptions.series[1].data = [0, totalPriceDispensacion]; // El primer valor (0) es para los medicamentos
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    async createPieChart() {
      try {
        const responseDispensacion = await axios.get('http://127.0.0.1:8000/hospital/api/v1dispensacion_medicamentos/');
        const dispensacionData = responseDispensacion.data;

        const totalSolicitados = dispensacionData.reduce((total, item) => total + item.total_medicamentos_solicitados, 0);
        const totalEntregados = dispensacionData.reduce((total, item) => total + item.total_medicamentos_entregados, 0);

        const total = totalSolicitados + totalEntregados;

        const pieData = {
          labels: ['Solicitados', 'Entregados'],
          datasets: [{
            data: [totalSolicitados, totalEntregados],
            backgroundColor: ['#FF6384', '#36A2EB']
          }]
        };

        new Chart(document.getElementById('medChart'), {
          type: 'pie',
          data: pieData,
          options: {
            plugins: {
              tooltip: {
                enabled: true,
                callbacks: {
                  label: function(context) {
                    var label = context.label || '';
                    if (label) {
                      label += ': ';
                    }
                    var value = context.parsed || 0;
                    label += value + ' (' + ((value / total) * 100).toFixed(2) + '%)';
                    return label;
                  }
                }
              }
            },
            responsive: true,
            maintainAspectRatio: false
          }
        });
      } catch (error) {
        console.error('Error creating pie chart:', error);
      }
    },
    handleCardButtonClick() {
      // Acción al hacer clic en el botón de la tarjeta
    }
  }
}
</script>
