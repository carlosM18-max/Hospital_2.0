<template>
    <form @submit.prevent="submitForm"
        class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 rounded-lg shadow-lg overflow-hidden mt-5">
        <!-- Información del Solicitante -->
        <div class="flex justify-between flex-col items-center">
            <label class="block text-gray-700 text-3xl font-normal mb-2">Información del Solicitante</label>
        </div>
        <!-- Personas -->
        <div class="mt-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Seleccione a un Paciente</label>
            <select v-model="selectedPersona"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
                <option value="">-- Selecciona una Opción --</option>
                <option v-for="persona in personas" :key="persona.Curp" :value="persona.Curp">
                    {{ persona.Nombre }} {{ persona.Primer_Apellido }} {{ persona.Segundo_Apellido }}
                </option>
            </select>
        </div>
        <!-- Medicos -->
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Seleccione a un Médico</label>
            </div>
            <select v-model="selectedMedico"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
                <option value="">-- Selecciona una Opción --</option>
                <option v-for="medico in medicos" :key="medico.Persona_ID" :value="medico.Persona_ID">
                    {{ medico.Titulo }} {{ medico.Nombre }} {{ medico.Primer_Apellido }} {{ medico.Segundo_Apellido }}
                </option>
            </select>
        </div>
        <!-- Servicios -->
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Seleccione un Servicio</label>
            </div>
            <select v-model="form.prioridad"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
                <option value="">-- Selecciona una Opción --</option>
            </select>
        </div>
        <!-- Detalles de la Solicitud -->
        <div class="flex justify-between flex-col items-center mt-5">
            <label class="block text-gray-700 text-3xl font-normal mb-2">Detalles de la Solicitud</label>
        </div>
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Prioridad</label>
            </div>
            <select v-model="form.prioridad"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
                <option value="">-- Selecciona una Opción --</option>
                <option value="Urgente">Urgente</option>
                <option value="Alta">Alta</option>
                <option value="Moderada">Moderada</option>
                <option value="Normal">Normal</option>
            </select>
        </div>
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Descripción</label>
            </div>
            <textarea v-model="form.descripcion"
                class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"></textarea>
        </div>
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Situación o Estatus</label>
            </div>
            <select v-model="form.estatus"
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
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Aprobación</label>
            </div>
            <select v-model="form.aprobacion"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
                <option value="">-- Selecciona una Opción --</option>
                <option value="Aprobado">Aprobado</option>
                <option value="Pendiente">Pendiente</option>
                <option value="Rechazado">Rechazado</option>
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
import { registrarSolicitud, obtenerDatosSolicitud } from '@/api/solicitud';
// import { obtenerPersonalMedico } from '@/api/medicos';

export default {
    data() {
        return {
            personas: [],
            medicos: [],
            selectedPersona: null,
            selectedMedico: null,
            selectedPrioridada: null,
            selectedEstatus : null,
            form: {
                descripcion: '',
                aprobacion: '',
                fechaRegistro: new Date().toISOString(),
            }
        };
    },
    created() {
        this.fetchPersonas();
        this.fetchMedicos();
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
                console.error(`Error: ${error}`);
            }
        },
        async fetchMedicos() {
            try {
                // this.medicos = await obtenerPersonalMedico();
                console.log(this.medicos);
            } catch (error) {
                console.error(`Error: ${error}`);
            }
        },
        async submitForm() {
            try {
                const solicitud = {
                    personaId: this.selectedPersona,
                    medicoId: this.selectedMedico,
                    prioridad: this.form.prioridad,
                    descripcion: this.form.descripcion,
                    estatus: this.form.estatus,
                    aprobacion: this.form.aprobacion,
                    fechaRegistro: this.form.fechaRegistro,
                };
                await registrarSolicitud(solicitud);
                alert('Solicitud registrada con éxito');
            } catch (error) {
                console.error('Error al registrar solicitud:', error.message);
                alert('Error al registrar solicitud');
            }
        }
    }
};
</script>
