<template>
    <form @submit.prevent="submitForm"
        class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 rounded-lg shadow-lg overflow-hidden mt-5">
        <!-- Información del Solicitante -->
        <div class="flex justify-between flex-col items-center">
            <label class="block text-gray-700 text-3xl font-normal mb-2">Información del Solicitante</label>
        </div>
        <!-- Pacientes -->
        <div class="mt-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Seleccione a un Paciente</label>
            <select v-model="selectedPersona"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
                <option value="">-- Selecciona una Opción --</option>
                <option v-for="persona in personas" :key="persona.ID" :value="persona.ID">
                    {{ persona.Nombre }} {{ persona.Primer_Apellido }} {{ persona.Segundo_Apellido }}
                </option>
            </select>
        </div>
        <!-- Médicos -->
        <div class="mt-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Seleccione a un Médico</label>
            <select v-model="selectedMedico"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
                <option value="">-- Selecciona una Opción --</option>
                <option v-for="medico in medicos" :key="medico.ID" :value="medico.ID">
                    {{ medico.Titulo }} {{ medico.Nombre }} {{ medico.Primer_Apellido }} {{ medico.Segundo_Apellido }}
                </option>
            </select>
        </div>
        <!-- Servicios -->
        <div class="mt-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Seleccione un Servicio</label>
            <select v-model="selectedServicio"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
                <option value="">-- Selecciona una Opción --</option>
                <option v-for="servicio in servicios" :key="servicio.ID" :value="servicio.ID">
                    {{ servicio.Nombre }}
                </option>
            </select>
        </div>
        <!-- Detalles de la Solicitud -->
        <div class="flex justify-between flex-col items-center mt-5">
            <label class="block text-gray-700 text-3xl font-normal mb-2">Detalles de la Solicitud</label>
        </div>
        <!-- Prioridad -->
        <div class="mt-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Prioridad</label>
            <select v-model="form.Prioridad"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
                <option value="">-- Selecciona una Opción --</option>
                <option value="Urgente">Urgente</option>
                <option value="Alta">Alta</option>
                <option value="Moderada">Moderada</option>
                <option value="Normal">Normal</option>
            </select>
        </div>
        <!-- Descripción -->
        <div class="mt-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Descripción</label>
            <textarea v-model="form.Descripcion"
                class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"></textarea>
        </div>
        <!-- Estatus -->
        <div class="mt-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Situación o Estatus</label>
            <select v-model="form.Estatus"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
                <option value="">-- Selecciona una Opción --</option>
                <option value="Registrada">Registrada</option>
                <option value="Programada">Programada</option>
                <option value="Cancelada">Cancelada</option>
                <option value="Reprogramada">Reprogramada</option>
                <option value="En_Proceso">En Proceso</option>
                <option value="Realizada">Realizada</option>
            </select>
        </div>
        <!-- Aprobación -->
        <div class="mt-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Aprobación</label>
            <select v-model="form.Estatus_Aprobacion"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
                <option value="">-- Selecciona una Opción --</option>
                <option value="true">Aprobado</option>
                <option value="false">Rechazado</option>
            </select>
        </div>
        <!-- Enviar Formulario -->
        <div class="mt-8">
            <button type="submit"
                class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-500 mb-5">Generar
                Solicitud</button>
        </div>
    </form>
</template>

<script>
import { obtenerPersonas } from '@/api/pacientes';
import { registrarSolicitud } from '@/api/solicitud';
import { obtenerServiciosMedicos } from '@/api/servicios';

export default {
    data() {
        return {
            personas: [],
            medicos: [],
            servicios: [],
            selectedPersona: null,
            selectedMedico: null,
            selectedServicio: null,
            form: {
                Prioridad: '',
                Descripcion: '',
                Estatus: '',
                Estatus_Aprobacion: '',
                Fecha_Registro: new Date().toISOString(),
                Fecha_Actualizacion: new Date().toISOString()
            },
            isModalVisible: false
        };
    },
    created() {
        this.fetchPersonas();
        this.fetchServiciosMedicos();
    },
    methods: {
        async fetchPersonas() {
            try {
                const personas = await obtenerPersonas();
                this.personas = personas.filter(persona => persona.Titulo !== 'Dr.' && persona.Titulo !== 'Dra.');
                this.medicos = personas.filter(persona => persona.Titulo === 'Dr.' || persona.Titulo === 'Dra.');
                console.log('Personas:', this.personas);
                console.log('Médicos:', this.medicos);
            } catch (error) {
                console.error(`Error al obtener personas: ${error}`);
            }
        },
        async fetchServiciosMedicos() {
            try {
                this.servicios = await obtenerServiciosMedicos();
                console.log('Servicios Médicos:', this.servicios);
            } catch (error) {
                console.error(`Error al obtener servicios médicos: ${error}`);
            }
        },
        resetForm() {
            this.selectedPersona = '';
            this.selectedMedico = '';
            this.selectedServicio = '';
            this.form.Prioridad = '';
            this.form.Descripcion = '';
            this.form.Estatus = '';
            this.form.Estatus_Aprobacion = '';
        },
        async submitForm() {
            try {
                const solicitud = {
                    Paciente_ID: this.selectedPersona ? Number(this.selectedPersona) : undefined,
                    Medico_ID: this.selectedMedico ? Number(this.selectedMedico) : undefined,
                    Servicio_ID: this.selectedServicio ? Number(this.selectedServicio) : undefined,
                    Prioridad: this.form.Prioridad,
                    Descripcion: this.form.Descripcion,
                    Estatus: this.form.Estatus,
                    Estatus_Aprobacion: this.form.Estatus_Aprobacion === 'true',
                    Fecha_Registro: this.form.Fecha_Registro,
                    Fecha_Actualizacion: this.form.Fecha_Actualizacion,
                };
                console.log('Paciente_ID:', solicitud.Paciente_ID);
                console.log('Medico_ID:', solicitud.Medico_ID);
                console.log('Servicio_ID:', solicitud.Servicio_ID);

                await registrarSolicitud(solicitud);
                alert('Solicitud registrada con éxito');
                this.$router.push('/TableTransplante');
            } catch (error) {
                console.error('Error al registrar solicitud:', error.message);
                alert('Error al registrar solicitud');
            }
        },
    }
};
</script>