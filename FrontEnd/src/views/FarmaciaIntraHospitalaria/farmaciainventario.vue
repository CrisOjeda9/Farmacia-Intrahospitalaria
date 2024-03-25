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
                  <template v-slot:cell(cantidad)="data">
                    <span v-if="!data.item.editable">{{ data.item.cantidad }}</span>
                    <input v-else type="number" v-model="data.item.cantidad" class="form-control" ref="editableInput">
                  </template>
                  <template v-slot:cell(precio_costo)="data">
                    <span v-if="!data.item.editable">{{ data.item.precio_costo }}</span>
                    <input v-else type="number" v-model="data.item.precio_costo" class="form-control"
                      ref="editableInput">
                  </template>
                  <template v-slot:cell(precio_venta)="data">
                    <span v-if="!data.item.editable">{{ data.item.precio_venta }}</span>
                    <input v-else type="number" v-model="data.item.precio_venta" class="form-control"
                      ref="editableInput">
                  </template>
                  <template v-slot:cell(numero_lote)="data">
                    <span v-if="!data.item.editable">{{ data.item.numero_lote }}</span>
                    <input v-else v-model="data.item.numero_lote" class="form-control" ref="editableInput">
                  </template>
                  <template v-slot:cell(fecha_solicitud)="data"> <!-- Ajuste aquí -->
                    <span v-if="!data.item.editable">{{ formatDate(data.item.fecha_solicitud) }}</span>
                    <input v-else type="date" v-model="data.item.fecha_solicitud" class="form-control"
                      ref="editableInput">
                  </template>
                  <template v-slot:cell(fecha_entrega)="data"> <!-- Ajuste aquí -->
                    <span v-if="!data.item.editable">{{ formatDate(data.item.fecha_entrega) }}</span>
                    <input v-else type="date" v-model="data.item.fecha_entrega" class="form-control"
                      ref="editableInput">
                  </template>
                  <template v-slot:cell(fecha_caducidad)="data">
                    <span v-if="!data.item.editable">{{ formatDate(data.item.fecha_caducidad) }}</span>
                    <input v-else type="date" v-model="data.item.fecha_caducidad" class="form-control"
                      ref="editableInput">
                  </template>
                  <template v-slot:cell(descripcion)="data"> <!-- Ajuste aquí -->
                    <span>{{ data.item.descripcion }}</span>
                  </template>
                  <template v-slot:cell(acciones)="data">
                    <div>
                      <b-button variant="link" size="sm" @click="remove(data.item)">
                        <i class="ri-delete-bin-line text-danger"></i>
                      </b-button>
                      <b-button variant="link" size="sm" @click="toggleEdit(data.item)">
                        <i class="ri-edit-line text-primary"></i>
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
import { useRouter } from 'vue-router'
import { xray } from '../../config/pluginInit'
import iqCard from '../../components/xray/cards/iq-card'

export default {
  name: 'InventarioMedicamentos',
  components: { iqCard },
  setup() {
    const router = useRouter()

    const redirectToNewMedicine = () => {
      router.push('/nuevoMed')
    }

    return { redirectToNewMedicine }
  },
  mounted() {
    xray.index()
  },
  methods: {
    remove(item) {
      let index = this.rows.indexOf(item)
      this.rows.splice(index, 1)
    },
    toggleEdit(item) {
      if (item.editable) {
        this.saveChanges()
      } else {
        this.rows.forEach(row => {
          if (row !== item) {
            row.editable = false
          }
        })
        item.editable = true
      }
    },
    saveChanges() {
      this.rows.forEach(row => {
        row.editable = false
      })
    },
    formatDate(date) {
      const options = { year: 'numeric', month: 'numeric', day: 'numeric' }
      return new Date(date).toLocaleDateString('es-ES', options)
    }
  },
  data() {
    return {
      columns: [
        { label: 'ID', key: 'id', class: 'text-left' },
        { label: 'Código', key: 'codigo', class: 'text-left' },
        { label: 'Nombre Genérico', key: 'nombre_generico', class: 'text-left' },
        { label: 'Nombre Comercial', key: 'nombre_comercial', class: 'text-left' },
        { label: 'Tipo de Presentación', key: 'tipo_presentacion', class: 'text-left' },
        { label: 'Vía de Administración', key: 'via_administracion', class: 'text-left' },
        { label: 'Cantidad', key: 'cantidad', class: 'text-left' },
        { label: 'Precio Costo', key: 'precio_costo', class: 'text-left' },
        { label: 'Precio Venta', key: 'precio_venta', class: 'text-left' },
        { label: 'Número de Lote', key: 'numero_lote', class: 'text-left' },
        { label: 'Fecha de Solicitud', key: 'fecha_solicitud', class: 'text-left' }, // Agregamos la fecha de solicitud
        { label: 'Fecha de Entrega', key: 'fecha_entrega', class: 'text-left' },
        { label: 'Fecha de Caducidad', key: 'fecha_caducidad', class: 'text-left' },
        { label: 'Descripción', key: 'descripcion', class: 'text-left' }, // Nuevo campo de Descripción
        { label: 'Acciones', key: 'acciones', class: 'text-center' }
      ],

      rows: [
        {
          id: 1,
          codigo: 'MED001',
          nombre_generico: 'Paracetamol',
          nombre_comercial: 'Panadol',
          tipo_presentacion: 'Tableta',
          via_administracion: 'Oral',
          cantidad: 100,
          precio_costo: 10,
          precio_venta: 15,
          numero_lote: 'LOTE001',
          fecha_solicitud: new Date(2024, 3, 20), // Ejemplo de fecha de solicitud
          fecha_entrega: new Date(2024, 3, 25), // Ejemplo de fecha de entrega
          fecha_caducidad: new Date(2025, 3, 17),
          descripcion: 'Descripción del medicamento',
          editable: false
        },
        // Otros elementos del inventario
      ]

    }
  }
}
</script>

<style scoped>
/* Estilos CSS si es necesario */
</style>
