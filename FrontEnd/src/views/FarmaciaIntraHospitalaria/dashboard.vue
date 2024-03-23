<template>
    <div>
      <!-- Card 1 -->
      <b-row>
        <b-col sm="6">
          <b-card title="Dispensacion de Recetas" class="iq-mb-3">
            <b-card-text>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</b-card-text>
            <b-button href="farmintra" block variant="btn btn-primary w-100" @click="handleCardButtonClick">Ir</b-button>
          </b-card>
        </b-col>
        <b-col sm="6">
          <b-card title="Control Inventario" class="iq-mb-3">
            <b-card-text>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</b-card-text>
            <b-button href="farmintraInv" block variant="btn btn-primary w-100" @click="handleCardButtonClick">Ir</b-button>
          </b-card>
        </b-col>
      </b-row>
    </div>
    <b-container fluid>
      <b-row>
        <b-col lg="6" v-for="(item, index) in charts" :key="index">
          <iq-card>
            <template v-slot:headerTitle>
              <h4>{{ item.title }}</h4>
            </template>
            <template v-slot:body>
              <ApexChart :element="item.type" :chartOption="item.bodyData" />
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
  
  export default {
    name: 'ApexCharts',
    components: { iqCard, ApexChart },
    mounted() {
      xray.index()
    },
    data() {
      return {
        slide: 0,
        images: [
          'https://via.placeholder.com/800x400/FF5733/FFFFFF',
          'https://via.placeholder.com/800x400/33FF57/FFFFFF',
          'https://via.placeholder.com/800x400/5733FF/FFFFFF',
          // Agrega más URLs de imágenes aquí según sea necesario
        ],
              charts: [
          {
            title: 'Corte de Caja',
            type: 'line',
            bodyData: {
              chart: {
                height: 350,
                type: 'line',
                zoom: {
                  enabled: false
                }
              },
              series: [
                {
                  name: 'Desktops',
                  data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
                }
              ],
              dataLabels: {
                enabled: false
              },
              stroke: {
                curve: 'straight'
              },
              title: {
                text: 'Product Trends by Month',
                align: 'left'
              },
              grid: {
                row: {
                  colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
                  opacity: 0.5
                }
              },
              xaxis: {
                categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
              }
            }
          },
          {
            title: 'Line Area Chart',
            type: 'line-area',
            bodyData: {
              chart: {
                height: 350,
                type: 'area'
              },
              dataLabels: {
                enabled: false
              },
              stroke: {
                curve: 'smooth'
              },
              colors: ['#089bab', '#FC9F5B'],
              series: [
                {
                  name: 'series1',
                  data: [31, 40, 28, 51, 42, 109, 100]
                },
                {
                  name: 'series2',
                  data: [11, 32, 45, 32, 34, 52, 41]
                }
              ],
  
              xaxis: {
                type: 'datetime',
                categories: ['2018-09-19T00:00:00', '2018-09-19T01:30:00', '2018-09-19T02:30:00', '2018-09-19T03:30:00', '2018-09-19T04:30:00', '2018-09-19T05:30:00', '2018-09-19T06:30:00']
              },
              tooltip: {
                x: {
                  format: 'dd/MM/yy HH:mm'
                }
              }
            }
          },
          {
            title: 'Column Chart',
            type: 'column',
            bodyData: {
              chart: {
                height: 350,
                type: 'bar'
              },
              plotOptions: {
                bar: {
                  horizontal: false,
                  columnWidth: '55%',
                  endingShape: 'rounded'
                }
              },
              dataLabels: {
                enabled: false
              },
              stroke: {
                show: true,
                width: 2,
                colors: ['transparent']
              },
              colors: ['#089bab', '#FC9F5B', '#e64141'],
              series: [
                {
                  name: 'Net Profit',
                  data: [44, 55, 57, 56, 61, 58]
                },
                {
                  name: 'Revenue',
                  data: [76, 85, 101, 98, 87, 105]
                },
                {
                  name: 'Free Cash Flow',
                  data: [35, 41, 36, 26, 45, 48]
                }
              ],
              xaxis: {
                categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
              },
              yaxis: {
                title: {
                  text: '$ (thousands)'
                }
              },
              fill: {
                opacity: 1
              },
              tooltip: {
                y: {
                  formatter: function (val) {
                    return '$ ' + val + ' thousands'
                  }
                }
              }
            }
          },
          {
            title: 'Bar Chart',
            type: 'bar',
            bodyData: {
              chart: {
                height: 350,
                type: 'bar'
              },
              plotOptions: {
                bar: {
                  horizontal: true
                }
              },
              dataLabels: {
                enabled: false
              },
              series: [
                {
                  data: [470, 540, 580, 690, 1100, 1200, 1380]
                }
              ],
              xaxis: {
                categories: ['Netherlands', 'Italy', 'France', 'Japan', 'United States', 'China', 'Germany']
              }
            }
          },
        ]
      }
    }
  }
  </script>
  
  