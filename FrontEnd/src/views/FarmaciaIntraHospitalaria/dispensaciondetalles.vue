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
                  <template v-slot:cell(detalleRecetaId)="data">
                    <span>{{ data.item.detalleRecetaId }}</span>
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
import { ref, onMounted } from 'vue'

export default {
  name: 'UiDataTable',
  components: { iqCard },
  setup() {
    const columns = [
      { key: 'id', label: 'ID', field: 'id', headerClass: 'text-left' },
      { key: 'personalMedicoId', label: 'Personal Médico ID', field: 'personalMedicoId', headerClass: 'text-left' },
      { key: 'recetaId', label: 'Receta ID', field: 'recetaId', headerClass: 'text-left' },
      { key: 'detalleRecetaId', label: 'Detalle Receta ID', field: 'detalleRecetaId', headerClass: 'text-left' },
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
        const response1 = await axios.get('http://127.0.0.1:8000/hospital/api/v1dispensacion_medicamentos/')
        const response2 = await axios.get('http://127.0.0.1:8000/hospital/api/v1detalles_dispensacion/')

        // Mapear los datos de la primera API
        const data1 = response1.data.map(item => ({
          id: item.id,
          personalMedicoId: item.personal_medico,
          recetaId: item.receta,
          cantidadSolicitada: item.total_medicamentos_solicitados,
          cantidadEntregada: item.total_medicamentos_entregados,
          fechaVenta: item.fecha_registro,
          estatus: item.estatus
        }))

        // Mapear los datos de la segunda API
        const data2 = response2.data.map(item => ({
          id: item.dispensacion,
          detalleRecetaId: item.detalle_receta,
          cantidadEntregada: item.cantidad_entregada,
          precioUnitario: item.precio_unitario,
          importe: item.precio_total
        }))

        // Combina los datos de ambas API
        const combinedData = data1.map(item1 => {
          const correspondingItem = data2.find(item2 => item1.id === item2.id)
          return correspondingItem ? { ...item1, ...correspondingItem } : item1
        })

        // Obtener los detalles del medicamento usando el ID de la receta
        const medicamentoRequests = combinedData.map(async item => {
          try {
            const medicamentoResponse = await axios.get(`http://127.0.0.1:8000/hospital/api/v1medicamentos/${item.recetaId}`)
            const medicamentoData = medicamentoResponse.data
            return {
              ...item,
              nombreGenerico: medicamentoData.nombre_generico,
              nombreComercial: medicamentoData.nombre_comercial,
              viaAdministrativa: medicamentoData.via_administracion,
              tipoPresentacion: medicamentoData.presentacion
            }
          } catch (error) {
            console.error('Error fetching medicamento data:', error)
            return item
          }
        })

        // Esperar a que todas las solicitudes de detalles de medicamentos se completen
        const medicamentoDetails = await Promise.all(medicamentoRequests)

        // Asignar el conjunto combinado de datos a rows
        rows.value = medicamentoDetails
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    }

    // Llamar a fetchData() cada vez que el componente se monte
    onMounted(fetchData)

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

<style scoped>
/* Aquí puedes agregar estilos específicos para este componente si es necesario */
</style>
