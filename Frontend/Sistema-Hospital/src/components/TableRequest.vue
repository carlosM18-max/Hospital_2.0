<template>
  <form>
    <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
      <div class="flex flex-column sm:flex-row flex-wrap space-y-4 sm:space-y-0 items-center justify-between pb-4">
        <div class="relative">
          <div class="absolute inset-y-0 left-0 rtl:inset-r-0 rtl:right-0 flex items-center ps-3 pointer-events-none">
            <svg class="w-5 h-5 text-gray-500 dark:text-gray-400" aria-hidden="true" fill="currentColor"
              viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd"
                d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                clip-rule="evenodd"></path>
            </svg>
          </div>
          <input type="text" id="table-search"
            v-model="searchTerm"
            @input="filterSolicitudes"
            class="block p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Buscar ...." />
        </div>
        <div>
          <RouterLink to="/requestTansplant">
            <button id="dropdownRadioButton" data-dropdown-toggle="dropdownRadio"
              class="inline-flex items-center text-white bg-blue-500 border border-blue-300 focus:outline-none hover:bg-blue-400 focus:ring-4 focus:ring-blue-100 font-medium rounded-lg text-sm px-3 py-1.5 dark:bg-blue-800 dark:text-white dark:border-blue-600 dark:hover:bg-blue-700 dark:hover:border-blue-600 dark:focus:ring-blue-700"
              type="button">
              Agregar Solicitud
            </button>
          </RouterLink>
        </div>
        <label for="table-search" class="sr-only">Search</label>
      </div>
      <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th scope="col" class="p-4"></th>
            <th scope="col" class="px-6 py-3 text-center">Paciente</th>
            <th scope="col" class="px-6 py-3 text-center">Medico</th>
            <th scope="col" class="px-6 py-3 text-center">Servicio</th>
            <th scope="col" class="px-6 py-3 text-center">Prioridad</th>
            <th scope="col" class="px-6 py-3 text-center">Descripcion</th>
            <th scope="col" class="px-6 py-3 text-center">Estatus</th>
            <th scope="col" class="px-6 py-3 text-center">Aprobacion</th>
            <th scope="col" class="px-6 py-3 text-center">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="solicitud in paginatedSolicitudes" :key="solicitud.ID"
            class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
            <td class="w-4 p-4"></td>
            <td class="px-6 py-4 font-medium text-white">{{ getPacienteNombre(solicitud.Paciente_ID) }}</td>
            <td class="px-6 py-4 font-medium text-white">{{ getMedicoNombre(solicitud.Medico_ID) }}</td>
            <td class="px-6 py-4 font-medium text-white">{{ getServicioNombre(solicitud.Servicio_ID) }}</td>
            <td class="px-6 py-4 font-medium text-white">{{ solicitud.Prioridad }}</td>
            <td class="px-6 py-4 font-medium text-white text-center">{{ solicitud.Descripcion }}</td>
            <td class="px-6 py-4 font-medium text-white text-center">{{ solicitud.Estatus }}</td>
            <td class="px-6 py-4 font-medium text-white">{{ solicitud.Estatus_Aprobacion ? 'Aprobado' : 'Rechazado' }}</td>
            <td class="px-6 py-4 font-medium text-white">
              <router-link :to="`/UpdateTransplante/${solicitud.ID}`"
                class="font-medium text-blue-600 dark:text-blue-500 hover:underline mr-2">
                <span class="material-symbols-outlined">edit</span>
              </router-link>
              <a href="#" @click.prevent="borrarSolicitud(solicitud.ID)"
                class="font-medium text-red-600 dark:text-red-500 hover:underline">
                <span class="material-symbols-outlined">delete</span>
              </a>
            </td>
          </tr>
        </tbody>
      </table>
      <nav class="flex items-center flex-column flex-wrap md:flex-row justify-between pt-4" aria-label="Table navigation">
        <span class="text-sm font-normal text-gray-500 dark:text-gray-400 mb-4 md:mb-0 block w-full md:inline md:w-auto">
          Mostrando <span class="font-semibold text-gray-500">{{ start + 1 }}-{{ end }}</span> de
          <span class="font-semibold text-gray-500">{{ filteredSolicitudes.length }}</span>
        </span>
        <ul class="inline-flex -space-x-px rtl:space-x-reverse text-sm h-8">
          <li>
            <button @click="prevPage" :disabled="currentPage === 1"
              class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
              Anterior
            </button>
          </li>
          <li>
            <button @click="nextPage" :disabled="end >= filteredSolicitudes.length"
              class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
              Siguiente
            </button>
          </li>
        </ul>
      </nav>
    </div>
  </form>
</template>

<script>
import { obtenerSolicitudes } from '@/api/solicitud';
import { obtenerPersonas } from '@/api/pacientes';
import { obtenerServiciosMedicos } from '@/api/servicios';

export default {
  data() {
    return {
      solicitudes: [],
      filteredSolicitudes: [],
      personas: [],
      medicos: [],
      servicios: [],
      currentPage: 1,
      pageSize: 5,
      searchTerm: '', 
    };
  },
  async created() {
    this.loadData();
  },
  methods: {
    async loadData() {
      try {
        this.solicitudes = await obtenerSolicitudes();
        this.filteredSolicitudes = this.solicitudes;
        const personas = await obtenerPersonas();
        this.personas = personas.filter(persona => persona.Titulo !== 'Dr.' && persona.Titulo !== 'Dra.');
        this.medicos = personas.filter(persona => persona.Titulo === 'Dr.' || persona.Titulo === 'Dra.');
        this.servicios = await obtenerServiciosMedicos();
      } catch (error) {
        console.error('Error al obtener datos:', error.message);
      }
    },
    async borrarSolicitud(id) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/solicitudes/${id}/`, {
          method: 'DELETE',
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(`Error al eliminar la solicitud: ${errorData.detail}`);
        }

        this.solicitudes = this.solicitudes.filter(solicitud => solicitud.ID !== id);
        this.filteredSolicitudes = this.filteredSolicitudes.filter(solicitud => solicitud.ID !== id);
        if (this.start >= this.filteredSolicitudes.length && this.currentPage > 1) {
          this.currentPage--;
        }
      } catch (error) {
        console.error(error.message);
        alert('Error al eliminar la solicitud');
      }
    },
    filterSolicitudes() {
      const searchTermLower = this.searchTerm.toLowerCase();
      this.filteredSolicitudes = this.solicitudes.filter(solicitud => 
        (this.getPacienteNombre(solicitud.Paciente_ID).toLowerCase().includes(searchTermLower) ||
        this.getMedicoNombre(solicitud.Medico_ID).toLowerCase().includes(searchTermLower) ||
        this.getServicioNombre(solicitud.Servicio_ID).toLowerCase().includes(searchTermLower) ||
        solicitud.Descripcion.toLowerCase().includes(searchTermLower))
      );
      this.currentPage = 1; // Reiniciar la página actual después de la búsqueda
    },
    getPacienteNombre(id) {
      const paciente = this.personas.find(p => p.ID === id);
      return paciente ? `${paciente.Nombre} ${paciente.Primer_Apellido} ${paciente.Segundo_Apellido}` : 'Desconocido';
    },
    getMedicoNombre(id) {
      const medico = this.medicos.find(m => m.ID === id);
      return medico ? `${medico.Titulo} ${medico.Nombre} ${medico.Primer_Apellido} ${medico.Segundo_Apellido}` : 'Desconocido';
    },
    getServicioNombre(id) {
      const servicio = this.servicios.find(s => s.ID === id);
      return servicio ? servicio.Nombre : 'Desconocido';
    },
    nextPage() {
      if (this.end < this.filteredSolicitudes.length) {
        this.currentPage++;
      }
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
  },
  computed: {
    paginatedSolicitudes() {
      const start = (this.currentPage - 1) * this.pageSize;
      const end = start + this.pageSize;
      return this.filteredSolicitudes.slice(start, end);
    },
    start() {
      return (this.currentPage - 1) * this.pageSize;
    },
    end() {
      const end = this.currentPage * this.pageSize;
      return end > this.filteredSolicitudes.length ? this.filteredSolicitudes.length : end;
    }
  },
};
</script>