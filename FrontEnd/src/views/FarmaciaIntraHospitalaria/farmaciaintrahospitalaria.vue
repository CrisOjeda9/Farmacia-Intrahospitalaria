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
                                class="ri-file-fill text-success"></i><span>Receta dispensacion</span> </a>
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
                                  <b-form-select v-model="idReceta" :options="recetaMedica" :rules="isRequire"
                                    :class="{ 'is-invalid': errors.idReceta }">
                                  </b-form-select>
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
                                  {{ data.item.Medicamento.nombre_generico }}
                                </template>
                                <template v-slot:cell(DOSIS)="data">
                                  {{ data.item.DOSIS }}
                                </template>
                                <template v-slot:cell(RECOMENDACIONES)="data">
                                  {{ data.item.RECOMENDACIONES }}
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
                                class="ri-file-fill text-success"></i><span>Solicitud</span> </a>
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
                                  <b-form-select v-model="personalMedicoId" :options="cedulaMedica" :rules="isRequire"
                                    :class="{ 'is-invalid': errors.personalMedicoId }">
                                  </b-form-select>


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
                              <h3 class="mb-4">Detalles del Personal Médico:</h3>
                              <b-row v-if="medicoDetalles">
                                <b-col md="6">
                                  <b-form-group label="Persona ID:">
                                    <b-form-input v-model="medicoDetalles.persona" readonly></b-form-input>
                                  </b-form-group>
                                </b-col>
                                <b-col md="6">
                                  <b-form-group label="Especialidad:">
                                    <b-form-input v-model="medicoDetalles.especialidad" readonly></b-form-input>
                                  </b-form-group>
                                </b-col>
                                <b-col md="6">
                                  <b-form-group label="Tipo:">
                                    <b-form-input v-model="medicoDetalles.tipo" readonly></b-form-input>
                                  </b-form-group>
                                </b-col>
                                <b-col md="6">
                                  <b-form-group label="Cedula Profesional:">
                                    <b-form-input v-model="medicoDetalles.cedula_profesional" readonly></b-form-input>
                                  </b-form-group>
                                </b-col>
                                <b-col md="6">
                                  <b-form-group label="Estatus:">
                                    <b-form-input v-model="medicoDetalles.estatus" readonly></b-form-input>
                                  </b-form-group>
                                </b-col>
                                <b-col md="6">
                                  <b-form-group label="Fecha Contratación:">
                                    <b-form-input v-model="medicoDetalles.fecha_contratacion" readonly></b-form-input>
                                  </b-form-group>
                                </b-col>
                                <b-col md="6">
                                  <b-form-group label="Departamento:">
                                    <b-form-input v-model="medicoDetalles.departamento" readonly></b-form-input>
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
                                  {{ data.item.Medicamento.nombre_generico }}
                                </template>
                                <template v-slot:cell(Departamento_ID)="data">
                                  {{ data.item.Departamento_ID }}
                                </template>
                                <!-- Agrega otras columnas aquí -->
                                <template v-slot:cell(PRECIO)="data">
                                  {{ data.item.PRECIO }}
                                </template>
                                <template v-slot:cell(SOLICITADO)="data">
                                  {{ data.item.SOLICITADO }}
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
                              <h4 class="text-center">Venta Total: {{ totalVentaCalculada }}</h4>
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
import axios from 'axios'
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
      idReceta: '', // Variable para almacenar la ID de receta seleccionada
      recetas: [], // Array para almacenar las opciones de las recetas
      cedula: null, // Variable para almacenar la ID de receta seleccionada
      currentindex: 1,
      users: [],
      patientName: '',
      patientLastName: '',
      patientSecondLastName: '',
      patientDateOfBirth: '',
      personalMedicoId: '',
      recetaMedicaDetails: [ // Datos estáticos para la tabla
        { ID: 1, Medicamento: { nombre_generico: 'Medicamento A' }, DOSIS: '1 comprimido', RECOMENDACIONES: 'Tomar con comida', SOLICITADO: 10, CANTIDAD: 0, PRECIO: 5, ESTATUS: 'Activo' },
        { ID: 2, Medicamento: { nombre_generico: 'Medicamento B' }, DOSIS: '2 comprimidos', RECOMENDACIONES: 'Tomar antes de dormir', SOLICITADO: 5, CANTIDAD: 0, PRECIO: 8, ESTATUS: 'Inactivo' },
        // Agrega más objetos de datos según sea necesario
      ], medicoDetalles: [],
      persona: '',
      especialidad: '',
      tipo: '',
      cedula_profesional: '',
      estatus: '',
      fecha_contratacion: '',
      fecha_terminacion_contrato: '',
      departamento: '',
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

      personalMedicoDetails: [
  // Datos estáticos para la tabla
  { 
    ID: 1, 
    Medicamento:{ nombre_generico: 'Medicamento A' },
    DOSIS: '1 comprimido', 
    RECOMENDACIONES: 'Tomar con comida', 
    SOLICITADO: 10, 
    CANTIDAD: 0, 
    PRECIO: 5, 
    ESTATUS: 'Activo' // Agregamos el dato de estatus
  },
  { 
    ID: 2, 
    Medicamento: { nombre_generico: 'Medicamento B' },
    DOSIS: '2 comprimidos', 
    RECOMENDACIONES: 'Tomar antes de dormir', 
    SOLICITADO: 5, 
    CANTIDAD: 0, 
    PRECIO: 8, 
    ESTATUS: 'Inactivo' // Agregamos el dato de estatus
  },
  // Puedes agregar más objetos de datos según sea necesario
],

      personalcolumns: [
        { key: 'MEDICAMENTO_ID', label: 'Medicamento', formatter: 'nombreMedicamento' },
        { key: 'SOLICITADO', label: 'Solicitado' },
        { key: 'CANTIDAD', label: 'Cantidad', editable: true },
        { key: 'PRECIO', label: 'Precio', editable: false }, // Nuevo campo de precio
        { key: 'IMPORTE', label: 'Importe' }, // Nueva columna para el importe
        { key: 'ESTATUS', label: 'Estatus' } // Columna para el estado
      ],


      cedulaMedica: [

      ],
      recetaMedica: [

      ],


    }
  }, mounted() {
    xray.index()
    this.selectMedicos()
    this.selectRecetas()
  },





  methods: {

    async selectMedicos() {
      try {
        const apiPersonalMedico = await axios.get('http://127.0.0.1:8000/hospital/api/v1personal_medico/');

        // Mapear los datos de la API para mostrar las cédulas y guardar las IDs
        this.cedulaMedica = apiPersonalMedico.data.map(item => ({
          value: item.id, // Aquí guardamos la ID del personal médico
          text: item.cedula_profesional, // Aquí mostramos la cédula profesional
        }));
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    async mostrarMedicoDetalles(cedulaSeleccionada) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/hospital/api/v1personal_medico/?cedula_profesional=${cedulaSeleccionada}`)
        const medicoSeleccionado = response.data[0]; // Suponiendo que la API devuelve un solo resultado

        // Actualizar los detalles del personal médico con los datos obtenidos
        this.medicoDetalles.persona = medicoSeleccionado.persona;
        this.medicoDetalles.especialidad = medicoSeleccionado.especialidad;
        this.medicoDetalles.tipo = medicoSeleccionado.tipo;
        this.medicoDetalles.cedula_profesional = medicoSeleccionado.cedula_profesional;
        this.medicoDetalles.estatus = medicoSeleccionado.estatus;
        this.medicoDetalles.fecha_contratacion = medicoSeleccionado.fecha_contratacion;
        this.medicoDetalles.fecha_terminacion_contrato = medicoSeleccionado.fecha_terminacion_contrato;
        this.medicoDetalles.departamento = medicoSeleccionado.departamento;

      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
    ,













    async selectRecetas() {
      try {
        const apiRecetaMedica = await axios.get('http://127.0.0.1:8000/hospital/api/v1receta_medica/');

        // Mapear los datos de la API para mostrar las cédulas y guardar las IDs
        this.recetaMedica = apiRecetaMedica.data.map(item => ({
          value: item.id, // Aquí guardamos la ID del personal médico
          text: item.cita, // Aquí mostramos la cédula profesional
        }));
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    async cargarDatosPersona() {
      try {
        // Realizar llamada a la API para obtener los datos de la persona basados en el ID de la receta
        const response = await fetch(`http://127.0.0.1:8000/hospital/api/v1receta_medica/${this.idReceta}`);
        const data = await response.json();

        // Obtener el ID de cita de la receta
        const citaId = data.cita;

        // Realizar llamada a la API para obtener los datos de la cita
        const citaResponse = await fetch(`http://127.0.0.1:8000/hospital/api/v1citas/${citaId}`);
        const citaData = await citaResponse.json();

        // Obtener el ID de la persona de la cita
        const personaId = citaData.personas;

        // Realizar llamada a la API para obtener los datos de la persona
        const personaResponse = await fetch(`http://127.0.0.1:8000/hospital/api/v1personas/${personaId}`);
        const personaData = await personaResponse.json();

        // Asignar los datos de la persona a las variables del componente
        this.patientName = personaData.nombre;
        this.patientLastName = personaData.primer_apellido;
        this.patientSecondLastName = personaData.segundo_apellido;
        this.patientDateOfBirth = personaData.fecha_nacimiento;
      } catch (error) {
        console.error('Error al cargar los datos de la persona:', error);
      }
    },






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

      console.log(val);
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
        this.mostrarMedicoDetalles(this.idReceta);

        console.log(this.idReceta)
      }
      else if (val === 11) {
        this.mostrarMedicoDetalles(this.personalMedicoId);

        console.log(this.personalMedicoId)

      }

      if (val === 2) {
        this.obtenerDatosPacientePorCitaId(this.recetaMedica.CITA_ID)
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
    },
    
    totalVentaCalculada() {
    return this.personalMedicoDetails.reduce((total, item) => {
      return total + (item.CANTIDAD * item.PRECIO);
    }, 0).toFixed(2);
  }
 
  },
  watch: {
    selectedOption: function () {
      this.changeTab(1)
    },
    idReceta() {
      // Cuando se selecciona un nuevo ID de receta, cargar los datos de la persona
      this.cargarDatosPersona();
    }
  }
}

</script>