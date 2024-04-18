<template>
  <b-container fluid>
    <b-row>
      <b-col md="12">
        <iq-card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Detalles Lotes</h4>
          </template>
          <template v-slot:body>
            <b-row>

              <b-col md="12" class="table-responsive w-100">
                <b-table striped bordered hover :items="rows" :fields="columns">
                  <template v-slot:cell(id)="data">
                    <span>{{ data.index + 1 }}</span>
                  </template>
                  <template v-slot:cell(codigo)="data">
                    <span>{{ data.item.codigo }}</span>
                  </template>
                  <template v-slot:cell(nombre_generico)="data">
                    <span>{{ data.item.nombre_generico }}</span>
                  </template>
                  <template v-slot:cell(nombre_comercial)="data"> <!-- Ajuste aquí -->
                    <span>{{ data.item.nombre_comercial }}</span>
                  </template>
                  <template v-slot:cell(tipo_presentacion)="data">
                    <span>{{ data.item.tipo_presentacion }}</span>
                  </template>
                  <template v-slot:cell(via_administracion)="data">
                    <span>{{ data.item.via_administracion }}</span>
                  </template>
                  <template v-slot:cell(marca)="data">
                    <span>{{ data.item.marca }}</span>
                  </template>
                  <template v-slot:cell(cantidad)="data">
                    <span>{{ data.item.cantidad }}</span>
                  </template>

                  <template v-slot:cell(precio_costo)="data">
                    <span>{{ data.item.precio_costo }}</span>
                  </template>

                  <template v-slot:cell(precio_venta)="data">
                    <span>{{ data.item.precio_venta }}</span>
                  </template>

              

                  <template v-slot:cell(fecha_solicitud)="data">
                    <span>{{ formatDate(data.item.fecha_solicitud) }}</span>
                  </template>

                  <template v-slot:cell(fecha_entrega)="data">
                    <span>{{ formatDate(data.item.fecha_entrega) }}</span>
                  </template>

                  <template v-slot:cell(fecha_caducidad)="data">
                    <span>{{ formatDate(data.item.fecha_caducidad) }}</span>
                  </template>

                  <template v-slot:cell(descripcion)="data"> <!-- Ajuste aquí -->
                    <span>{{ data.item.descripcion }}</span>
                  </template>
                  <template v-slot:cell(acciones)="data">
                    <div>
                      <b-button variant="link" size="sm" @click="remove(data.item)">
                        <i class="ri-delete-bin-line text-danger"></i>
                      </b-button>

                    </div>
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { xray } from '../../config/pluginInit'
import iqCard from '../../components/xray/cards/iq-card'
import axios from 'axios' // Importa Axios si no lo has hecho ya

export default {
  name: 'InventarioMedicamentos',
  components: { iqCard },
  setup() {
    const router = useRouter()

    const redirectToNewMedicine = () => {
      router.push('/nuevoMed')
    }

    const columns = [
      { label: 'ID', key: 'id', class: 'text-left' },
      { label: 'Código', key: 'codigo', class: 'text-left' },
      { label: 'Nombre Genérico', key: 'nombre_generico', class: 'text-left' },
      { label: 'Nombre Comercial', key: 'nombre_comercial', class: 'text-left' },
      { label: 'Tipo de Presentación', key: 'tipo_presentacion', class: 'text-left' },
      { label: 'Vía de Administración', key: 'via_administracion', class: 'text-left' },
      { label: 'Marca', key: 'marca', class: 'text-left' },
      { label: 'Cantidad', key: 'cantidad', class: 'text-left' },
      { label: 'Precio Costo', key: 'precio_costo', class: 'text-left' },
      { label: 'Precio Venta', key: 'precio_venta', class: 'text-left' },
      { label: 'Fecha de Solicitud', key: 'fecha_solicitud', class: 'text-left' }, // Agregamos la fecha de solicitud
      { label: 'Fecha de Entrega', key: 'fecha_entrega', class: 'text-left' },
      { label: 'Fecha de Caducidad', key: 'fecha_caducidad', class: 'text-left' },
      { label: 'Descripción', key: 'descripcion', class: 'text-left' }, // Nuevo campo de Descripción
      { label: 'Acciones', key: 'acciones', class: 'text-center' }
    ]

    const rows = ref([])
    const fetchMedicamento = async (id) => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/hospital/api/v1medicamentos/${id}`);
        return response.data;
      } catch (error) {
        console.error('Error fetching medicamento:', error);
        return null;
      }
    };
    const fetchData = async () => {
      try {
        const response1 = await axios.get('http://127.0.0.1:8000/hospital/api/v1lotes_medicamentos/')
        const response2 = await axios.get('http://127.0.0.1:8000/hospital/api/v1detalle_lotes/')

        // Mapear los datos de la primera API
        const data1 = response1.data.map(item => ({
          id: item.id,
          cantidad: item.cantidad,
          precio_costo: item.precio_unitario,
          fecha_solicitud: item.fecha_solicitud,
          descripcion: item.descripcion,
          fecha_entrega: item.fecha_ingreso,
        }))

        // Mapear los datos de la segunda API
        const data2 = response2.data.map(item => ({
          id: item.lotes,
          codigo: item.codigo,
          nombre_generico: item.medicamento,
          nombre_comercial: item.medicamento,
          tipo_presentacion: item.medicamento,
          via_administracion: item.medicamento,
          marca: item.marca,
          fecha_vencimiento: item.fecha_vencimiento,
          precio_venta: item.precio_unitario,
          fecha_caducidad: item.fecha_vencimiento,
          editable: false
        }))

        // Combina los datos de ambas API
        const combinedData = data1.map(item1 => {
          const correspondingItem = data2.find(item2 => item1.id === item2.id)
          return correspondingItem ? { ...item1, ...correspondingItem } : item1
        })
        // Obtener detalles del medicamento para cada elemento
        for (const item of combinedData) {
          const medicamentoDetails = await fetchMedicamento(item.id);
          
          if (medicamentoDetails) {
            item.nombre_generico = medicamentoDetails.nombre_generico;
            item.nombre_comercial = medicamentoDetails.nombre_comercial;
            item.via_administracion = medicamentoDetails.via_administracion;
            item.tipo_presentacion = medicamentoDetails.presentacion;
          }
        }
        // Asignar el conjunto combinado de datos a rows
        rows.value = combinedData
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    }

    fetchData()
    const remove = async (item) => {
  try {
    // Eliminar el documento de la primera API (lotes_medicamentos)
    await axios.delete(`http://127.0.0.1:8000/hospital/api/v1lotes_medicamentos/${item.id}`);
    
    // Eliminar el documento de la segunda API (detalle_lotes)
    await axios.delete(`http://127.0.0.1:8000/hospital/api/v1detalle_lotes/${item.id}`);
    
    // Eliminar el documento de la lista local
    let index = rows.value.indexOf(item);
    if (index !== -1) {
      rows.value.splice(index, 1);
    }
  } catch (error) {
    console.error('Error removing item:', error);
  }
}



    const formatDate = (date) => {
      const options = { year: 'numeric', month: 'numeric', day: 'numeric' }
      return new Date(date).toLocaleDateString('es-ES', options)
    }

    return { redirectToNewMedicine, columns, rows, remove, formatDate }
  },
  mounted() {
    xray.index()
  },
  methods: {
    // Si hubiera algún método adicional, agrégalo aquí
  },
  data() {
    return {
      // Si hubiera alguna data adicional, agrégala aquí
    }
  }
}
</script>
