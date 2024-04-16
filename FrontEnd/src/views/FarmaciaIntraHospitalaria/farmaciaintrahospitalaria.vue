<template>
  <b-container fluid>
    <b-row>
      <b-col lg="12">
        <iq-card>
          <template v-slot:headerTitle>
            <div class="d-flex justify-content-between align-items-center">
              <h4 class="card-title">Escoger el tipo de transacción</h4>
              <div class="form-check form-check-inline">
                <b-form-radio v-model="selectedOption" name="option" value="option1">Paciente</b-form-radio>
              </div>
              <div class="form-check form-check-inline">
                <b-form-radio v-model="selectedOption" name="option" value="option2">Hospital</b-form-radio>
              </div>
              <div class="ms-auto">
                <b-button variant="btn btn-sm iq-bg-success" @click="redirectToDetailsDispencer">Detalles de
                  dispensación</b-button>
              </div>
            </div>
          </template>
          <template v-slot:body>

            <!-- Formulario correspondiente a la opción seleccionada -->
            <template v-if="selectedOption === 'option1'">
              <b-row>
                <b-col sm="12">
                  <iq-card no-body>
                    <template v-slot:body>
                      <div class="stepwizard mt-4">
                        <ul class="stepwizard-row setup-panel">
                          <div id="user" class="wizard-step active"
                            :class="`${currentindex == 1 ? 'active' : ''} ${currentindex > 1 ? 'done active' : ''}`">
                            <a href="#user-detail" class="active btn"> <i
                                class="ri-lock-unlock-line text-primary"></i><span>Receta</span> </a>
                          </div>
                          <div id="document" class="wizard-step"
                            :class="`${currentindex == 2 ? 'active' : ''} ${currentindex > 2 ? 'done active' : ''}`">
                            <a href="#document-detail" class="btn btn-default disabled active"> <i
                                class="ri-user-fill text-danger"></i><span>Receta detalles</span> </a>
                          </div>
                          <div id="bank" class="wizard-step"
                            :class="`${currentindex == 3 ? 'active' : ''} ${currentindex > 3 ? 'done active' : ''}`">
                            <a href="#bank-detail" class="btn btn-default disabled active"> <i
                                class="ri-camera-fill text-success"></i><span>Receta dispensacion</span> </a>
                          </div>
                          <div id="confirm" class="wizard-step"
                            :class="`${currentindex == 4 ? 'active' : ''} ${currentindex > 4 ? 'done active' : ''}`">
                            <a href="#cpnfirm-data" class="btn btn-default disabled active"> <i
                                class="ri-check-fill text-warning"></i><span>Confirmacion</span> </a>
                          </div>
                        </ul>
                      </div>
                      <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ errors }" class="text-center mt-3">
                        <!-- <b-form id="form-wizard1" class="text-center mt-3"> -->
                        <div :class="`${currentindex == 1 ? 'show' : 'd-none'}`">
                          <fieldset>
                            <div class="form-card text-start">
                              <b-row>
                                <div class="col-7">
                                  <h3 class="mb-4">ID de Receta Médica:</h3>
                                </div>
                              </b-row>
                              <b-row>
                                <b-col md="6">
                                  <b-form-group label="ID de Receta Médica: *">
                                    <!-- Utilizamos un componente de selección -->
                                    <b-form-select v-model="idReceta" :options="options" :rules="isRequire"
                                      :class="{ 'is-invalid': errors.idReceta }"></b-form-select>
                                    <div class="invalid-feedback">
                                      <span>{{ errors.idReceta }}</span>
                                    </div>
                                  </b-form-group>
                                </b-col>
                              </b-row>
                            </div>
                            <a href="#" class="btn btn-primary next action-button float-end" @click="changeTab(2)"
                              value="Next">Next</a>
                          </fieldset>
                        </div>
                        <div :class="`${currentindex == 2 ? 'show' : 'd-none'}`">
                          <fieldset v-if="recetaMedica">
                            <div class="form-card text-start">
                              <h3 class="mb-4">Detalles de la Receta Médica:</h3>
                              <b-row>
                                <b-col md="6">
                                  <b-form-group label="Nombre:">
                                    <b-form-input v-model="patientName" readonly></b-form-input>
                                  </b-form-group>
                                </b-col>
                                <b-col md="6">
                                  <b-form-group label="Primer Apellido:">
                                    <b-form-input v-model="patientLastName" readonly></b-form-input>
                                  </b-form-group>
                                </b-col>
                                <b-col md="6">
                                  <b-form-group label="Segundo Apellido:">
                                    <b-form-input v-model="patientSecondLastName" readonly></b-form-input>
                                  </b-form-group>
                                </b-col>
                                <b-col md="6">
                                  <b-form-group label="Fecha de Nacimiento:">
                                    <b-form-input v-model="patientDateOfBirth" readonly></b-form-input>
                                  </b-form-group>
                                </b-col>
                              </b-row>
                            </div>
                            <a href="#payment" @click="changeTab(3)"
                              class="btn btn-primary next action-button float-end" value="Next">Next</a>
                            <a href="#account" @click="changeTab(1)"
                              class="btn btn-dark previous action-button-previous float-end me-1"
                              value="Previous">Previous</a>
                          </fieldset>

                        </div>
                        <div id="payment" :class="`${currentindex == 3 ? 'show' : 'd-none'}`">
                          <fieldset>
                            <div class="form-card text-start">
                              <h3 class="mb-4">Detalles de la Receta Médica:</h3>
                              <b-table striped bordered hover :items="recetaMedicaDetails" :fields="columns">
                                <!-- Define las columnas de la tabla aquí -->
                                <template v-slot:cell(ID)="data">
                                  {{ data.item.ID }}
                                </template>
                                <template v-slot:cell(MEDICAMENTO_ID)="data">
                                  {{ medicamentos[data.item.MEDICAMENTO_ID] }}
                                </template>

                                <template v-slot:cell(SOLICITADO)="data">
                                  {{ data.item.SOLICITADO }}
                                </template>
                                <!-- Columna editable para la cantidad -->
                                <template v-slot:cell(CANTIDAD)="data">
                                  <b-form-input v-model="data.item.CANTIDAD" type="number" min="0"
                                    @input="updateCantidad(data.item)"></b-form-input>
                                </template>

                                <!-- Columna no editable para el precio -->
                                <template v-slot:cell(PRECIO)="data">
                                  {{ data.item.PRECIO }}
                                </template>

                                <template v-slot:cell(IMPORTE)="data">
                                  {{ (data.item.CANTIDAD * data.item.PRECIO).toFixed(2) }}
                                </template>
                                <template v-slot:cell(ESTATUS)="data">
                                  {{ calcularEstado(data.item) }}
                                </template>
                              </b-table>
                              
                            </div>
                            <!-- Ventana fija para mostrar el total -->
                            <div class="fixed-bottom bg-light p-3">
                              <h4 class="text-center">Venta Total: {{ totalVenta }}</h4>
                            </div>

                            <a href="#payment" @click="changeTab(4)"
                              class="btn btn-primary next action-button float-end" value="Next">Next</a>
                            <a href="#account" @click="changeTab(2)"
                              class="btn btn-dark previous action-button-previous float-end me-1"
                              value="Previous">Previous</a>
                          </fieldset>
                        </div>

                        <div id="confirm" :class="`${currentindex == 4 ? 'show' : 'd-none'}`">
                          <fieldset>
                            <div class="form-card">
                              <b-row>
                                <div class="col-7">
                                  <h3 class="mb-4 text-start">Finish:</h3>
                                </div>
                              </b-row>
                              <br /><br />
                              <h2 class="text-success text-center">
                                <strong>Venta realizada !</strong>
                              </h2>
                              <br />
                              <b-row class="justify-content-center">
                                <div class="col-3">
                                  <img src="../../assets/images/page-img/img-success.png" class="img-fluid"
                                    alt="fit-image" />
                                </div>
                              </b-row>
                              <br /><br />
                              <b-row class="justify-content-center">
                                <div class="col-7 text-center">
                                  <h5 class="purple-text text-center">You Have Successfully Signed Up</h5>
                                </div>
                              </b-row>
                            </div>
                          </fieldset>
                        </div>
                        <!-- </b-form> -->
                      </Form>
                    </template>
                  </iq-card>
                </b-col>
              </b-row>
              <!-- Agrega aquí el formulario correspondiente a la opción 1 -->
            </template>

            <template v-else-if="selectedOption === 'option2'">
              <b-row>
                <b-col sm="12">
                  <iq-card no-body>

                    <template v-slot:body>
                      <div class="stepwizard mt-4">
                        <ul class="stepwizard-row setup-panel">
                          <div id="user" class="wizard-step active"
                            :class="`${currentindex == 1 ? 'active' : ''} ${currentindex > 1 ? 'done active' : ''}`">
                            <a href="#user-detail" class="active btn"> <i
                                class="ri-lock-unlock-line text-primary"></i><span>Validacion de Personal Medico
                              </span> </a>
                          </div>
                          <div id="document" class="wizard-step"
                            :class="`${currentindex == 2 ? 'active' : ''} ${currentindex > 2 ? 'done active' : ''}`">
                            <a href="#document-detail" class="btn btn-default disabled active"> <i
                                class="ri-user-fill text-danger"></i><span>Datos del personal medico</span> </a>
                          </div>
                          <div id="bank" class="wizard-step"
                            :class="`${currentindex == 3 ? 'active' : ''} ${currentindex > 3 ? 'done active' : ''}`">
                            <a href="#bank-detail" class="btn btn-default disabled active"> <i
                                class="ri-camera-fill text-success"></i><span>Solicitud</span> </a>
                          </div>
                          <div id="confirm" class="wizard-step"
                            :class="`${currentindex == 4 ? 'active' : ''} ${currentindex > 4 ? 'done active' : ''}`">
                            <a href="#cpnfirm-data" class="btn btn-default disabled active"> <i
                                class="ri-check-fill text-warning"></i><span>Confirmacion</span> </a>
                          </div>
                        </ul>
                      </div>
                      <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ errors }" class="text-center mt-3">
                        <!-- <b-form id="form-wizard1" class="text-center mt-3"> -->
                        <div :class="`${currentindex == 1 ? 'show' : 'd-none'}`">
                          <fieldset>
                            <div class="form-card text-start">
                              <b-row>
                                <div class="col-7">
                                  <h3 class="mb-4">User Information:</h3>
                                </div>
                              </b-row>
                              <b-row>
                                <b-col md="6">
                                  <b-form-group label="Personal Médico ID *">
                                    <b-form-select v-model="personalMedicoId" :options="optionsPersonal"
                                      :rules="isRequire"
                                      :class="{ 'is-invalid': errors.personalMedicoId }"></b-form-select>
                                    <div class="invalid-feedback">
                                      <span>{{ errors.personalMedicoId }}</span>
                                    </div>
                                  </b-form-group>

                                </b-col>
                              </b-row>
                            </div>
                            <a href="#" class="btn btn-primary next action-button float-end" @click="changeTab(11)"
                              value="Next">Next</a>
                          </fieldset>
                        </div>
                        <div :class="`${currentindex == 11 ? 'show' : 'd-none'}`">

                          <fieldset>
                            <div class="form-card text-start">
                              <h3 class="mb-4">Detalles del Personal Medico:</h3>
                              <b-row v-if="pedidosHospital">
                                <b-col md="6">
                                  <b-form-group label="Departamento ID:">
                                    <b-form-input v-model="pedidosHospital.Departamento_ID" readonly></b-form-input>
                                  </b-form-group>
                                </b-col>
                                <b-col md="6">
                                  <b-form-group label="Especialidad:">
                                    <b-form-input v-model="pedidosHospital.Especialidad" readonly></b-form-input>
                                  </b-form-group>
                                </b-col>
                                <b-col md="6">
                                  <b-form-group label="Tipo:">
                                    <b-form-input v-model="pedidosHospital.Tipo" readonly></b-form-input>
                                  </b-form-group>
                                </b-col>
                                <b-col md="6">
                                  <b-form-group label="Cedula Profesional:">
                                    <b-form-input v-model="pedidosHospital.Cedula_Profesional" readonly></b-form-input>
                                  </b-form-group>
                                </b-col>
                                <b-col md="6">
                                  <b-form-group label="Estatus:">
                                    <b-form-input v-model="pedidosHospital.Estatus" readonly></b-form-input>
                                  </b-form-group>
                                </b-col>
                              </b-row>

                            </div>
                            <a href="#payment" @click="changeTab(12)"
                              class="btn btn-primary next action-button float-end" value="Next">Next</a>
                            <a href="#account" @click="changeTab(1)"
                              class="btn btn-dark previous action-button-previous float-end me-1"
                              value="Previous">Previous</a>
                          </fieldset>

                        </div>
                        <div id="payment" :class="`${currentindex == 12 ? 'show' : 'd-none'}`">
                          <fieldset>
                            <div class="form-card text-start">
                              <h3 class="mb-4">Detalles de la Venta:</h3>
                              <b-table striped bordered hover :items="personalMedicoDetails" :fields="personalcolumns">
                                <!-- Define las columnas de la tabla aquí -->
                                <template v-slot:cell(ID)="data">
                                  {{ data.item.ID }}
                                </template>
                                <template v-slot:cell(MEDICAMENTO_ID)="data">
                                  {{ medicamentosPersonal[data.item.MEDICAMENTO_ID] }}
                                </template>
                                <template v-slot:cell(Departamento_ID)="data">
                                  {{ data.item.Departamento_ID }}
                                </template>
                                <!-- Agrega otras columnas aquí -->
                                <template v-slot:cell(PRECIO)="data">
                                  {{ data.item.PRECIO }}
                                </template>
                                <template v-slot:cell(CANTIDAD)="data">
                                  <b-form-input v-model="data.item.CANTIDAD" type="number" min="0"
                                    @input="updateCantidad(data.item)"></b-form-input>
                                </template><!--  -->
                                <template v-slot:cell(IMPORTE)="data">
                                  {{ (data.item.CANTIDAD * data.item.PRECIO).toFixed(2) }}
                                </template>
                                <template v-slot:cell(ESTATUS)="data">
                                  {{ calcularEstado(data.item) }}
                                </template>
                              </b-table>
                            </div>
                            <!-- Ventana fija para mostrar el total -->
                            <div class="fixed-bottom bg-light p-3">
                              <h4 class="text-center">Venta Total: {{ totalVenta }}</h4>
                            </div>

                            <a href="#payment" @click="changeTab(4)"
                              class="btn btn-primary next action-button float-end" value="Next">Next</a>
                            <a href="#account" @click="changeTab(11)"
                              class="btn btn-dark previous action-button-previous float-end me-1"
                              value="Previous">Previous</a>
                          </fieldset>
                        </div>
                        <div id="confirm" :class="`${currentindex == 4 ? 'show' : 'd-none'}`">
                          <fieldset>
                            <div class="form-card">
                              <b-row>
                                <div class="col-7">
                                  <h3 class="mb-4 text-start">Finish:</h3>
                                </div>
                              </b-row>
                              <br /><br />
                              <h2 class="text-success text-center">
                                <strong>Venta exitosa!</strong>
                              </h2>
                              <br />
                              <b-row class="justify-content-center">
                                <div class="col-3">
                                  <img src="../../assets/images/page-img/img-success.png" class="img-fluid"
                                    alt="fit-image" />
                                </div>
                              </b-row>
                              <br /><br />
                              <b-row class="justify-content-center">
                                <div class="col-7 text-center">
                                  <h5 class="purple-text text-center">You Have Successfully Signed Up</h5>
                                </div>
                              </b-row>
                            </div>
                          </fieldset>
                        </div>
                        <!-- </b-form> -->
                      </Form>
                    </template>
                  </iq-card>
                </b-col>
              </b-row>
            </template>
          </template>
        </iq-card>
      </b-col>
    </b-row>
  </b-container>
</template>


<script>
import { xray } from '../../config/pluginInit'
import iqCard from '../../components/xray/cards/iq-card'


import { Form } from 'vee-validate'
import { useRouter } from 'vue-router'

export default {
  name: 'ValidateWizard',
  components: {
    iqCard,
    Form,
  },
  setup() {
    const router = useRouter()

    const redirectToDetailsDispencer = () => {
      router.push('/farmaDis')
    }

    return { redirectToDetailsDispencer }
  },
  data() {

    return {
      selectedOption: 'option1', // Opción predeterminada seleccionada
      idReceta: null, // Variable para almacenar la ID de receta seleccionada
      cedula: null, // Variable para almacenar la ID de receta seleccionada
      currentindex: 1,
      users: [],
      recetaMedicaDetails: [],
      patientName: '',
      patientLastName: '',
      patientSecondLastName: '',
      patientDateOfBirth: '',
      columns: [
        { key: 'MEDICAMENTO_ID', label: 'Medicamento', formatter: 'nombreMedicamento' },
        { key: 'DOSIS', label: 'Dosis' },
        { key: 'RECOMENDACIONES', label: 'Recomendaciones' },
        { key: 'SOLICITADO', label: 'Solicitado' },
        { key: 'CANTIDAD', label: 'Cantidad', editable: true },
        { key: 'PRECIO', label: 'Precio', editable: false }, // Nuevo campo de precio
        { key: 'IMPORTE', label: 'Importe' }, // Nueva columna para el importe
        { key: 'ESTATUS', label: 'Estatus' } // Columna para el estado



      ],


      options: [
        { value: 'idReceta1', text: 'ID Receta 1' },
        { value: 'idReceta2', text: 'ID Receta 2' },
        { value: 'idReceta3', text: 'ID Receta 3' }
      ],

      personalMedicoDetails: [],
      personalcolumns: [
        { key: 'MEDICAMENTO_ID', label: 'Medicamento', formatter: 'nombreMedicamento' },
        { key: 'SOLICITADO', label: 'Solicitado' },
        { key: 'CANTIDAD', label: 'Cantidad', editable: true },
        { key: 'PRECIO', label: 'Precio', editable: false }, // Nuevo campo de precio
        { key: 'IMPORTE', label: 'Importe' }, // Nueva columna para el importe
        { key: 'ESTATUS', label: 'Estatus' } // Columna para el estado
      ],


      optionsPersonal: [
        { value: '1', text: '1' },
        { value: '2', text: '2' },
        { value: '3', text: '3' }
      ],

      medicamentos: {
        101: 'Paracetamol',
        102: 'Ibuprofeno',
        103: 'Tempra',
        104: 'Agrifen',
        105: 'PeptoBismol',
        106: 'Sal de uvas',
        // Agrega más medicamentos según sea necesario
      },
      medicamentosPersonal: {
        11: 'Tempra',
        12: 'Buscapina',
        // Agrega más medicamentos según sea necesario
      }
    }
  }, mounted() {
    xray.index()
  },
  methods: {
    onSubmit() {
      this.$router.replace('/user/user-list')
    },
    isRequire(value) {
      if (value && value.trim()) {
        return true
      }
      return 'This field is required'
    }, resetPaymentForm() {
      // Aquí restableces los valores de los campos de la segunda parte del formulario
      this.$refs.paymentForm.reset(); // Suponiendo que tengas una referencia al formulario
    }, updateCantidad(item) {
      let cantidad = parseInt(item.CANTIDAD);
      const cantidadSolicitada = parseInt(item.SOLICITADO);

      if (isNaN(cantidad)) {
        cantidad = 0; // Establecer un valor por defecto de 0 si la cantidad es nula o no definida
      }

      if (cantidad > cantidadSolicitada) {
        // Si la cantidad ingresada es mayor a la cantidad solicitada, establecer la cantidad igual a la cantidad solicitada
        cantidad = cantidadSolicitada;
      }

      item.CANTIDAD = cantidad;
    }
    ,
    calcularEstado(item) {
      const cantidad = parseInt(item.CANTIDAD);
      const cantidadSolicitada = parseInt(item.SOLICITADO);

      if (isNaN(cantidad) || isNaN(cantidadSolicitada)) {
        return 'Datos incorrectos';
      }

      if (cantidad === cantidadSolicitada) {
        return 'Abastecido';
      } else if (cantidad > 0 && cantidad < cantidadSolicitada) {
        return 'Parcialmente abastecido';
      } else {
        return 'Parcialmente abastecido'; // Cambiamos 'No abastecido' por 'Parcialmente abastecido'
      }
    }
    ,

    changeTab(val) {


      // Verifica si se ha seleccionado una ID de receta
      //if (val === 2 && !this.idReceta) {
      // Si no se ha seleccionado una ID de receta y ya se ha ingresado la cédula, no hagas nada y devuelve
      //return;
      //}


      this.currentindex = val;

      if (val === 2) {
        // Simular los detalles de la receta médica (sustituir con datos reales de la base de datos más adelante)
        if (this.idReceta === 'idReceta1') { // Verificar la ID seleccionada
          this.recetaMedica = {
            ID: 1,
            CITA_ID: 123,
            FECHA_HORA_REGISTRO: '2024-03-16 12:00:00',
            ESTATUS: 'Solicitada'
          };
        } else if (this.idReceta === 'idReceta2') { // Verificar la ID seleccionada
          this.recetaMedica = {
            ID: 2,
            CITA_ID: 245,
            FECHA_HORA_REGISTRO: '2024-02-16 10:00:00',
            ESTATUS: 'Solicitada'
          };
        } else if (this.idReceta === 'idReceta3') { // Verificar la ID seleccionada
          this.recetaMedica = {
            ID: 3,
            CITA_ID: 456,
            FECHA_HORA_REGISTRO: '2024-03-17 09:30:00',
            ESTATUS: 'Subrogada'
          };
        }
      }
      else if (val === 1) {
        // Si el usuario regresa a la segunda parte del formulario, asegúrate de restablecer los detalles de la receta médica
        this.recetaMedica = null;
      }





      if (val === 2) {
        this.obtenerDatosPacientePorCitaId(this.recetaMedica.CITA_ID)
        // Simular los detalles de la receta médica (sustituir con datos reales de la base de datos más adelante)
        if (this.personalMedicoId === '1') { // Verificar la cédula profesional seleccionada
          this.pedidosHospital = {
            Persona_ID: 1,
            Departamento_ID: 1,
            Especialidad: 'Cardiología',
            Tipo: 'Médico',
            Cedula_Profesional: '12345678',
            Estatus: 'Activo',
            Fecha_Contratacion: '2023-01-15',
            Fecha_Terminacion_Contrato: null
          };
        } else if (this.personalMedicoId === '2') { // Verificar la cédula profesional seleccionada
          this.pedidosHospital = {
            Persona_ID: 2,
            Departamento_ID: 2,
            Especialidad: 'Pediatría',
            Tipo: 'Médico',
            Cedula_Profesional: '23456789',
            Estatus: 'Activo',
            Fecha_Contratacion: '2022-09-20',
            Fecha_Terminacion_Contrato: null
          };
        } else if (this.personalMedicoId === '3') { // Verificar la cédula profesional seleccionada
          this.pedidosHospital = {
            Persona_ID: 3,
            Departamento_ID: 3,
            Especialidad: 'Oftalmología',
            Tipo: 'Médico',
            Cedula_Profesional: '34567890',
            Estatus: 'Inactivo',
            Fecha_Contratacion: '2024-02-10',
            Fecha_Terminacion_Contrato: '2024-12-10'
          };
        }
      } else if (val === 1) {
        // Si el usuario regresa a la segunda parte del formulario, asegúrate de restablecer los detalles de la receta médica
        this.pedidosHospital = null;
      }
      if (val === 2 && !this.cedula) {
        // Si el usuario intenta avanzar al paso 2 sin seleccionar una ID de receta, no hagas nada
        return;
      }



      if (val === 3) {
        // Simula los detalles de la receta médica
        if (this.idReceta === 'idReceta1') {
          this.recetaMedicaDetails = [
            { ID: 1, receta_id: 1, MEDICAMENTO_ID: 101, DOSIS: '1 comprimido cada 12 horas', RECOMENDACIONES: 'Tomar con comida', SOLICITADO: 5, CANTIDAD: 0, PRECIO: 5.99 },
            { ID: 2, receta_id: 1, MEDICAMENTO_ID: 102, DOSIS: '2 comprimidos antes de dormir', RECOMENDACIONES: 'Tomar con agua', SOLICITADO: 1, CANTIDAD: 0, PRECIO: 8.99 }
          ];
        } else if (this.idReceta === 'idReceta2') {
          this.recetaMedicaDetails = [
            { ID: 3, receta_id: 2, MEDICAMENTO_ID: 103, DOSIS: '1 cápsula cada 8 horas', RECOMENDACIONES: 'Tomar con leche', SOLICITADO: 3, CANTIDAD: 0, PRECIO: 12.99 },
            { ID: 4, receta_id: 2, MEDICAMENTO_ID: 104, DOSIS: '1 inyección semanal', RECOMENDACIONES: 'Aplicar en el brazo', SOLICITADO: 2, CANTIDAD: 0, PRECIO: 24.99 }
          ];
        } else if (this.idReceta === 'idReceta3') {
          this.recetaMedicaDetails = [
            { ID: 5, receta_id: 3, MEDICAMENTO_ID: 105, DOSIS: '1 tableta diaria', RECOMENDACIONES: 'Tomar con agua tibia', SOLICITADO: 1, CANTIDAD: 0, PRECIO: 9.99 },
            { ID: 6, receta_id: 3, MEDICAMENTO_ID: 106, DOSIS: '2 comprimidos cada 6 horas', RECOMENDACIONES: 'Tomar con comida', SOLICITADO: 8, CANTIDAD: 0, PRECIO: 17.99 }
          ];
        }
      } else if (val === 2) {
        // Si el usuario regresa al paso 1, limpia los detalles de la receta médica
        this.recetaMedicaDetails = [];
      }
      if (val === 12) {
        // Simular los detalles de la receta médica (sustituir con datos reales de la base de datos más adelante)
        if (this.personalMedicoId === '1') { // Verificar la cédula profesional seleccionada
          this.personalMedicoDetails = [
            { ID: 1, Departamento_ID: 1, Cedula_Profesional: '12345678', MEDICAMENTO_ID: 11, SOLICITADO: 5, CANTIDAD: 0, PRECIO: 5.99 },
            { ID: 2, Departamento_ID: 1, Cedula_Profesional: '12345678', MEDICAMENTO_ID: 12, SOLICITADO: 1, CANTIDAD: 0, PRECIO: 8.99 }
          ];
        } else if (this.personalMedicoId === '2') { // Verificar la cédula profesional seleccionada
          this.personalMedicoDetails = [
            { ID: 3, Departamento_ID: 2, Cedula_Profesional: '23456789', MEDICAMENTO_ID: 11, SOLICITADO: 3, CANTIDAD: 0, PRECIO: 12.99 },
            { ID: 4, Departamento_ID: 2, Cedula_Profesional: '23456789', MEDICAMENTO_ID: 12, SOLICITADO: 2, CANTIDAD: 0, PRECIO: 24.99 }
          ];
        } else if (this.personalMedicoId === '3') { // Verificar la cédula profesional seleccionada
          this.personalMedicoDetails = [
            { ID: 5, Departamento_ID: 3, Cedula_Profesional: '34567890', MEDICAMENTO_ID: 11, SOLICITADO: 1, CANTIDAD: 0, PRECIO: 9.99 },
            { ID: 6, Departamento_ID: 3, Cedula_Profesional: '34567890', MEDICAMENTO_ID: 12, SOLICITADO: 8, CANTIDAD: 0, PRECIO: 17.99 }
          ];
        }
      } else if (val === 11) {
        // Si el usuario regresa a la segunda parte del formulario, asegúrate de restablecer los detalles de la receta médica
        this.personalMedicoDetails = [];
      }

      if (val === 11) {
        // Simular los detalles de la receta médica (sustituir con datos reales de la base de datos más adelante)
        if (this.personalMedicoId === '1') { // Verificar la cédula profesional seleccionada
          this.pedidosHospital = {
            Persona_ID: 1,
            Departamento_ID: 1,
            Especialidad: 'Cardiología',
            Tipo: 'Médico',
            Cedula_Profesional: '12345678',
            Estatus: 'Activo',
            Fecha_Contratacion: '2023-01-15',
            Fecha_Terminacion_Contrato: null
          };
        } else if (this.personalMedicoId === '2') { // Verificar la cédula profesional seleccionada
          this.pedidosHospital = {
            Persona_ID: 2,
            Departamento_ID: 2,
            Especialidad: 'Pediatría',
            Tipo: 'Médico',
            Cedula_Profesional: '23456789',
            Estatus: 'Activo',
            Fecha_Contratacion: '2022-09-20',
            Fecha_Terminacion_Contrato: null
          };
        } else if (this.personalMedicoId === '3') { // Verificar la cédula profesional seleccionada
          this.pedidosHospital = {
            Persona_ID: 3,
            Departamento_ID: 3,
            Especialidad: 'Oftalmología',
            Tipo: 'Médico',
            Cedula_Profesional: '34567890',
            Estatus: 'Inactivo',
            Fecha_Contratacion: '2024-02-10',
            Fecha_Terminacion_Contrato: '2024-12-10'
          };
        }
      } else if (val === 1) {
        // Si el usuario regresa a la segunda parte del formulario, asegúrate de restablecer los detalles de la receta médica
        this.pedidosHospital = null;
      }
      if (val === 2 && !this.cedula) {
        // Si el usuario intenta avanzar al paso 2 sin seleccionar una ID de receta, no hagas nada
        return;
      }
    },
    obtenerDatosPacientePorCitaId(citaId) {
      if (citaId === 123) {
        this.patientName = 'Juan';
        this.patientLastName = 'Pérez';
        this.patientSecondLastName = 'Gómez';
        this.patientDateOfBirth = '1990-05-15';
      } else if (citaId === 245) {
        this.patientName = 'María';
        this.patientLastName = 'González';
        this.patientSecondLastName = 'López';
        this.patientDateOfBirth = '1985-09-25';
      } else if (citaId === 456) {
        this.patientName = 'Carlos';
        this.patientLastName = 'Martínez';
        this.patientSecondLastName = 'Rodríguez';
        this.patientDateOfBirth = '1978-12-10';
      }

    },
  },
  computed: {
    totalVenta() {
      return this.recetaMedicaDetails.reduce((total, item) => {
        return total + (item.CANTIDAD * item.PRECIO);
      }, 0).toFixed(2);
    }
  },
  watch: {
    selectedOption: function(){
      this.changeTab(1)
    }
  }
}

</script>