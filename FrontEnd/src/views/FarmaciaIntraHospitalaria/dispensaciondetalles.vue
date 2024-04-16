<template>
  <b-container fluid>
    <b-row>
      <b-col md="12">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Detalles de Dispensacion</h4>
          </template>
          <template v-slot:body>
            <b-row>
              <b-col md="12" class="table-responsive w-100">
                <b-table striped bordered hover :items="rows" :fields="columns">
                  <template v-slot:cell(id)="data">
                    <span>{{ data.item.id }}</span>
                  </template>
                  <template v-slot:cell(personalMedicoId)="data">
                    <span>{{ data.item.personalMedicoId }}</span>
                  </template>
                  <template v-slot:cell(recetaId)="data">
                    <span>{{ data.item.recetaId }}</span>
                  </template>
                  <template v-slot:cell(nombreGenerico)="data">
                    <span>{{ data.item.nombreGenerico }}</span>
                  </template>
                  <template v-slot:cell(nombreComercial)="data">
                    <span>{{ data.item.nombreComercial }}</span>
                  </template>
                  <template v-slot:cell(viaAdministrativa)="data">
                    <span>{{ data.item.viaAdministrativa }}</span>
                  </template>
                  <template v-slot:cell(tipoPresentacion)="data">
                    <span>{{ data.item.tipoPresentacion }}</span>
                  </template>
                  <template v-slot:cell(cantidadSolicitada)="data">
                    <span>{{ data.item.cantidadSolicitada }}</span>
                  </template>
                  <template v-slot:cell(precioUnitario)="data">
                    <span>{{ data.item.precioUnitario }}</span>
                  </template>
                  <template v-slot:cell(cantidadEntregada)="data">
                    <span>{{ data.item.cantidadEntregada }}</span>
                  </template>
                  <template v-slot:cell(importe)="data">
                    <span>{{ data.item.importe }}</span>
                  </template>
                  <template v-slot:cell(estatus)="data">
                    <span>{{ data.item.estatus }}</span>
                  </template>
                  <template v-slot:cell(fechaVenta)="data">
                    <span>{{ data.item.fechaVenta }}</span>
                  </template>
                </b-table>
              </b-col>
            </b-row>
          </template>
        </iq-card>
      </b-col>
    </b-row>
  </b-container>
</template>


<script>
import iqCard from '../../components/xray/cards/iq-card'
import axios from 'axios';
import { ref } from 'vue'


export default {
  name: 'UiDataTable',
  components: { iqCard },
  setup() {

    const columns = [
      { key: 'id', label: 'ID', field: 'id', headerClass: 'text-left' },
      { key: 'personalMedicoId', label: 'Personal Médico ID', field: 'personalMedicoId', headerClass: 'text-left' },
      { key: 'recetaId', label: 'Receta ID', field: 'recetaId', headerClass: 'text-left' },
      { key: 'nombreGenerico', label: 'Nombre Genérico', field: 'nombreGenerico', headerClass: 'text-left' },
      { key: 'nombreComercial', label: 'Nombre Comercial', field: 'nombreComercial', headerClass: 'text-left' },
      { key: 'viaAdministrativa', label: 'Vía Administrativa', field: 'viaAdministrativa', headerClass: 'text-left' },
      { key: 'tipoPresentacion', label: 'Tipo de Presentación', field: 'tipoPresentacion', headerClass: 'text-left' },
      { key: 'cantidadSolicitada', label: 'Cantidad Solicitada', field: 'cantidadSolicitada', headerClass: 'text-left' },
      { key: 'precioUnitario', label: 'Precio Unitario', field: 'precioUnitario', headerClass: 'text-left' },
      { key: 'cantidadEntregada', label: 'Cantidad Entregada', field: 'cantidadEntregada', headerClass: 'text-left' },
      { key: 'importe', label: 'Importe', field: 'importe', headerClass: 'text-left' },
      { key: 'estatus', label: 'Estatus', field: 'estatus', headerClass: 'text-left' },
      { key: 'fechaVenta', label: 'Fecha de la Venta', field: 'fechaVenta', headerClass: 'text-left' }
    ]
    const rows = ref([])

    const fetchData = async () => {
      try {
        const response1 = await axios.get('http://127.0.0.1:8000/hospital/api/v1c_dispensacion_medicamentos/')
        const response2 = await axios.get('http://127.0.0.1:8000/hospital/api/v1c_detalle_dispensacion/')

        // Mapear los datos de la primera API
        const data1 = response1.data.map(item => ({
          personalMedicoId : item.Personal_Medico_ID ,
          recetaId : item.Receta_ID,
          cantidadSolicitada : item.Total_Medicamentos_Solicitados,
          cantidadEntregada: item.Total_Medicamentos_Entregados,
          estatus: item.Estatus

        }))

        // Mapear los datos de la segunda API
        const data2 = response2.data.map(item => ({
          id: item.Dispensacion_ID
        }))

        // Combina los datos de ambas API
        const combinedData = data1.map(item1 => {
          const correspondingItem = data2.find(item2 => item1.id === item2.id)
          return correspondingItem ? { ...item1, ...correspondingItem } : item1
        })

        // Asignar el conjunto combinado de datos a rows
        rows.value = combinedData
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    }

    fetchData()

    const remove = (item) => {
      let index = rows.value.indexOf(item)
      rows.value.splice(index, 1)
    }



    const formatDate = (date) => {
      const options = { year: 'numeric', month: 'numeric', day: 'numeric' }
      return new Date(date).toLocaleDateString('es-ES', options)
    }

    return { columns, rows, remove, formatDate }
  }
}


</script>
