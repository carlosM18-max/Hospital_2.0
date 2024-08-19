<template>
  <form @submit.prevent="actualizarSolicitud">
    <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 rounded-lg shadow-lg overflow-hidden mt-5">
      <!-- Información del Solicitante -->
      <div class="flex justify-between flex-col items-center">
        <label class="block text-gray-700 text-3xl font-normal mb-2">Información del Solicitante</label>
      </div>
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Seleccione a un Paciente</label>
        <select v-model="formData.Paciente_ID"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
          <option v-for="persona in personas" :key="persona.ID" :value="persona.ID">
            {{ persona.Nombre }} {{ persona.Primer_Apellido }} {{ persona.Segundo_Apellido }}
          </option>
        </select>
      </div>
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Seleccione a un Médico</label>
        <select v-model="formData.Medico_ID"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
          <option v-for="medico in medicos" :key="medico.ID" :value="medico.ID">
            {{ medico.Titulo }} {{ medico.Nombre }} {{ medico.Primer_Apellido }} {{ medico.Segundo_Apellido }}
          </option>
        </select>
      </div>
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Seleccione un Servicio</label>
        <select v-model="formData.Servicio_ID"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
          <option v-for="servicio in servicios" :value="servicio.ID" :key="servicio.ID">
            {{ servicio.Nombre }}
          </option>
        </select>
      </div>
      <!-- Detalles de la Solicitud -->
      <div class="flex justify-between flex-col items-center mt-5">
        <label class="block text-gray-700 text-3xl font-normal mb-2">Detalles de la Solicitud</label>
      </div>
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Prioridad</label>
        <select v-model="formData.Prioridad"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
          <option value="Urgente">Urgente</option>
          <option value="Alta">Alta</option>
          <option value="Moderada">Moderada</option>
          <option value="Normal">Normal</option>
        </select>
      </div>
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Descripción</label>
        <textarea v-model="formData.Descripcion"
          class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"></textarea>
      </div>
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Situación o Estatus</label>
        <select v-model="formData.Estatus"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
          <option value="Registrada">Registrada</option>
          <option value="Programada">Programada</option>
          <option value="Cancelada">Cancelada</option>
          <option value="Reprogramada">Reprogramada</option>
          <option value="En_Proceso">En Proceso</option>
          <option value="Realizada">Realizada</option>
        </select>
      </div>
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Aprobación</label>
        <select v-model="formData.Estatus_Aprobacion"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
          <option value="">-- Selecciona una Opción --</option>
          <option value="1">Aprobado</option>
          <option value="0">Rechazado</option>
        </select>
      </div>

      <!-- Enviar Formulario -->
      <div class="mt-8">
        <button type="submit"
          class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-500 mb-5">Actualizar
          Solicitud</button>
      </div>
    </div>
  </form>
</template>

<script>
import { obtenerSolicitudPorId, actualizarSolicitud } from '@/api/solicitud';
import { obtenerPersonas } from '@/api/pacientes';
import { obtenerServiciosMedicos } from '@/api/servicios';

export default {
  data() {
    return {
      formData: {
        Paciente_ID: null,
        Medico_ID: null,
        Servicio_ID: null,
        Prioridad: '',
        Descripcion: '',
        Estatus: '',
        Estatus_Aprobacion: false,
        Fecha_Registro: '',
        Fecha_Actualizacion: ''
      },
      personas: [],
      medicos: [],
      servicios: [],
    };
  },
  async created() {
    const solicitudId = this.$route.params.id; // Captura el ID de la solicitud desde la URL

    try {
      // Cargar los datos de la solicitud
      const solicitud = await obtenerSolicitudPorId(solicitudId);
      this.formData = solicitud;

      // Cargar listas de personas, médicos y servicios
      const personas = await obtenerPersonas();
      this.personas = personas.filter(persona => persona.Titulo !== 'Dr.' && persona.Titulo !== 'Dra.');
      this.medicos = personas.filter(persona => persona.Titulo === 'Dr.' || persona.Titulo === 'Dra.');
      this.servicios = await obtenerServiciosMedicos();
    } catch (error) {
      console.error('Error al obtener los datos:', error.message);
    }
  },
  methods: {
    async actualizarSolicitud() {
      const id = this.$route.params.id;
      try {
        const response = await fetch(`http://127.0.0.1:8000/solicitudes/${id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.formData),
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(`Error al actualizar la solicitud: ${errorData.detail}`);
        }

        alert('Solicitud actualizada correctamente');
        this.$router.push('/TableTransplante');
      } catch (error) {
        console.error(error.message);
        alert('Error al actualizar la solicitud');
      }
    },
  }
};
</script>