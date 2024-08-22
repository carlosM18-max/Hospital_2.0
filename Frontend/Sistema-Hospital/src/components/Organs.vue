<template>
    <div>
        <!-- Tabla de Órganos -->
        <form>
            <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
                <div
                    class="flex flex-column sm:flex-row flex-wrap space-y-4 sm:space-y-0 items-center justify-between pb-4">
                    <!-- Búsqueda -->
                    <div class="relative">
                        <div
                            class="absolute inset-y-0 left-0 rtl:inset-r-0 rtl:right-0 flex items-center ps-3 pointer-events-none">
                            <svg class="w-5 h-5 text-gray-500 dark:text-gray-400" aria-hidden="true" fill="currentColor"
                                viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd"
                                    d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                                    clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <input type="text" v-model="searchQuery" @input="searchOrgano"
                            class="block p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder="Buscar órgano...">
                    </div>


                    <div>
                        <RouterLink to="/organform">
                            <button id="dropdownRadioButton" data-dropdown-toggle="dropdownRadio"
                                class="inline-flex items-center text-white bg-blue-500 border border-blue-300 focus:outline-none hover:bg-blue-400 focus:ring-4 focus:ring-blue-100 font-medium rounded-lg text-sm px-3 py-1.5 dark:bg-blue-800 dark:text-white dark:border-blue-600 dark:hover:bg-blue-700 dark:hover:border-blue-600 dark:focus:ring-blue-700"
                                type="button">
                                Agregar Órgano
                            </button>
                        </RouterLink>
                    </div>

                    <label for="table-search" class="sr-only">Buscar</label>
                </div>
                <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        <tr>
                            <th scope="col" class="p-4"></th>
                            <th scope="col" class="px-6 py-3">NOMBRE</th>
                            <th scope="col" class="px-6 py-3">EDAD DEL DONANTE</th>
                            <th scope="col" class="px-6 py-3">FECHA DE EXTRACCIÓN</th>
                            <th scope="col" class="px-6 py-3">APARATOS Y SISTEMAS</th>
                            <th scope="col" class="px-6 py-3">TIPO</th>
                            <th scope="col" class="px-6 py-3">GRUPO SANGUÍNEO</th>
                            <th scope="col" class="px-6 py-3">ESTADO DE SALUD</th>
                            <th scope="col" class="px-6 py-3">ENFERMEDADES TRANSMISIBLES</th>
                            <th scope="col" class="px-6 py-3">DETALLES ADICIONALES</th>
                            <th scope="col" class="px-6 py-3">DISPONIBILIDAD</th>

                            <th scope="col" class="px-6 py-3">FECHA DE ACTUALIZACIÓN</th>
                            <th scope="col" class="px-6 py-3">FECHA DE REGISTRO</th>
                            <th scope="col" class="px-6 py-3">ESTATUS</th>
                            <th scope="col" class="px-6 py-3">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="organo in filteredOrganos" :key="organo.ID"
                            class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                            <td class="w-4 p-4"></td>
                            <td class="px-6 py-4">{{ organo.Nombre }}</td>
                            <td class="px-6 py-4">{{ organo.Edad_Donante }}</td>
                            <td class="px-6 py-4">{{ organo.Fecha_Extraccion }}</td>
                            <td class="px-6 py-4">{{ organo.Aparato_Sistema }}</td>
                            <td class="px-6 py-4">{{ organo.Tipo }}</td>
                            <td class="px-6 py-4">{{ organo.Grupo_Sanguineo }}</td>
                            <td class="px-6 py-4">{{ organo.Estado_Salud }}</td>
                            <td class="px-6 py-4">{{ organo.Enfermedades_Transmisibles ? 'Sí' : 'No' }}</td>
                            <td class="px-6 py-4">{{ organo.Detalles_Adicionales }}</td>
                            <td class="px-6 py-4">{{ organo.Disponibilidad }}</td>
                            <td class="px-6 py-4">{{ organo.Fecha_Actualizacion }}</td>
                            <td class="px-6 py-4">{{ organo.Fecha_Registro }}</td>
                            <td class="px-6 py-4">{{ organo.Estatus }}</td>
                            <td class="px-6 py-4">
                                <a href="#" @click.prevent="editOrgano(organo)"
                                    class="font-medium text-blue-600 dark:text-blue-500 hover:underline mr-2">
                                    <span class="material-symbols-outlined">edit</span>
                                </a>
                                <a href="#" @click="confirmDeleteOrgano(organo.ID)"
                                    class="font-medium text-red-600 dark:text-red-500 hover:underline">
                                    <span class="material-symbols-outlined">delete</span>
                                </a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </form>

        <!-- Modal de Edición -->
        <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
            <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg w-full max-w-2xl max-h-[80vh] overflow-auto">
                <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">Editar Órgano</h3>
                <form @submit.prevent="updateOrgano" class="grid grid-cols-1 sm:grid-cols-2 gap-4">

                    <!-- Nombre -->
                    <div class="col-span-1">
                        <label for="nombre"
                            class="block text-sm font-medium text-gray-700 dark:text-gray-300">Nombre</label>
                        <input v-model="selectedOrgano.Nombre" type="text" id="nombre"
                            class="mt-1 block w-full p-2 border border-gray-300 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white">
                    </div>

                    <!-- Edad del Donante -->
                    <div class="col-span-1">
                        <label for="edad_donante"
                            class="block text-sm font-medium text-gray-700 dark:text-gray-300">Edad del
                            Donante</label>
                        <input v-model="selectedOrgano.Edad_Donante" type="number" id="edad_donante"
                            class="mt-1 block w-full p-2 border border-gray-300 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white">
                    </div>

                    <!-- Fecha de Extracción -->
                    <div class="col-span-2">
                        <label for="fecha_extraccion"
                            class="block text-sm font-medium text-gray-700 dark:text-gray-300">Fecha de
                            Extracción</label>
                        <input v-model="selectedOrgano.Fecha_Extraccion" type="datetime-local" id="fecha_extraccion"
                            class="mt-1 block w-full p-2 border border-gray-300 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white">
                    </div>

                    <!-- Aparato Sistema -->
                    <div class="col-span-1">
                        <label for="aparatosistema"
                            class="block text-sm font-medium text-gray-700 dark:text-white">Aparato
                            Sistema</label>
                        <select v-model="selectedOrgano.Aparato_Sistema" id="aparatosistema"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option v-for="sistema in aparatosSistemas" :key="sistema" :value="sistema">{{ sistema }}
                            </option>
                        </select>
                    </div>

                    <!-- Tipo -->
                    <div class="col-span-1">
                        <label for="tipo" class="block text-sm font-medium text-gray-700 dark:text-white">Tipo</label>
                        <select v-model="selectedOrgano.Tipo" id="tipo"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option v-for="tipo in tipos" :key="tipo" :value="tipo">{{ tipo }}</option>
                        </select>
                    </div>

                    <!-- Grupo Sanguíneo -->
                    <div class="col-span-1">
                        <label for="grupo_sanguineo"
                            class="block text-sm font-medium text-gray-700 dark:text-gray-300">Grupo
                            Sanguíneo</label>
                        <select v-model="selectedOrgano.Grupo_Sanguineo" id="grupo_sanguineo"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option value="A+">A+</option>
                            <option value="A-">A-</option>
                            <option value="B+">B+</option>
                            <option value="B-">B-</option>
                            <option value="AB+">AB+</option>
                            <option value="AB-">AB-</option>
                            <option value="O+">O+</option>
                            <option value="O-">O-</option>
                        </select>
                    </div>

                    <!-- Estado de Salud -->
                    <div class="col-span-1">
                        <label for="estado_salud"
                            class="block text-sm font-medium text-gray-700 dark:text-gray-300">Estado de
                            Salud</label>
                        <select v-model="selectedOrgano.Estado_Salud" id="estado_salud"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option value="">-- Selecciona una opción --</option>
                            <option value="Excelente">Excelente</option>
                            <option value="Bueno">Bueno</option>
                            <option value="Regular">Regular</option>
                            <option value="Pobre">Pobre</option>
                            <option value="Crítico">Crítico</option>
                        </select>
                    </div>


                    <!-- Enfermedades Transmisibles -->
                    <div class="col-span-1">
                        <label for="enfermedades_transmisibles"
                            class="block text-sm font-medium text-gray-700 dark:text-gray-300">Enfermedades
                            Transmisibles</label>
                        <select v-model="selectedOrgano.Enfermedades_Transmisibles" id="enfermedades_transmisibles"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option :value="true">Sí</option>
                            <option :value="false">No</option>
                        </select>
                    </div>

                    <!-- Disponibilidad -->
                    <div class="col-span-1">
                        <label for="disponibilidad"
                            class="block text-sm font-medium text-gray-700 dark:text-gray-300">Disponibilidad</label>
                        <select v-model="selectedOrgano.Disponibilidad" id="disponibilidad"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option v-for="disponibilidad in disponibilidades" :key="disponibilidad"
                                :value="disponibilidad">{{
                                disponibilidad }}</option>
                        </select>
                    </div>

                    <!-- Detalles Adicionales -->
                    <div class="col-span-2">
                        <label for="detalles_adicionales"
                            class="block text-sm font-medium text-gray-700 dark:text-gray-300">Detalles
                            Adicionales</label>
                        <textarea v-model="selectedOrgano.Detalles_Adicionales" id="detalles_adicionales" rows="4"
                            class="mt-1 block w-full p-2 border border-gray-300 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white"></textarea>
                    </div>

                    <!-- Estatus -->
                    <div class="col-span-2">
                        <label for="estatus"
                            class="block text-sm font-medium text-gray-700 dark:text-gray-300">Estatus</label>
                        <select v-model="selectedOrgano.Estatus" id="estatus"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option value="">-- Selecciona una opción --</option>
                            <option :value="true">Activo</option>
                            <option :value="false">Inactivo</option>
                        </select>
                    </div>

                    <!-- Botones -->
                    <div class="col-span-2 flex justify-end">
                        <button @click="closeModal" type="button"
                            class="mr-4 px-4 py-2 bg-gray-300 dark:bg-gray-600 text-gray-800 dark:text-white rounded-lg">Cancelar</button>
                        <button type="submit"
                            class="px-4 py-2 bg-blue-500 dark:bg-blue-700 text-white rounded-lg">Guardar</button>
                    </div>
                </form>
            </div>
        </div>


    </div>
</template>

<script>
import axios from "axios";

const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
});

export default {
    name: "CreacionDeTablaOrganos",
    data() {
        return {
            organos: [],
            filteredOrganos: [], // Para la búsqueda
            searchQuery: '', // Modelo para la búsqueda
            selectedOrgano: {
                Nombre: '',
                Edad_Donante: 0,
                Aparato_Sistema: '',
                Detalles_Adicionales: '',
                Disponibilidad: '',
                Tipo: '',
                Estatus: false,

                Fecha_Extraccion: '',

                Grupo_Sanguineo: '',
                Estado_Salud: '',
                Enfermedades_Transmisibles: false,
                ID: null
            },
            showModal: false,
            api: "organos/",
            aparatosSistemas: [
                'Circulatorio',
                'Digestivo',
                'Respiratorio',
                'Nervioso',
                'Muscular',
                'Esquelético',
                'Endocrino',
                'Linfático',
                'Inmunológico',
                'Reproductor',
                'Urinario',
                'Sensorial'
            ],
            disponibilidades: ['En Proceso', 'Disponible', 'No Disponible', 'Reservado', 'Entregado'],
            tipos: ['Vital', 'No Vital']
        };
    },
    methods: {
        editOrgano(organo) {
            this.selectedOrgano = { ...organo };
            this.showModal = true;
        },

        async updateOrgano() {
            try {
                const organoId = this.selectedOrgano.ID;
                if (organoId === null) {
                    console.error("ID del órgano no definido.");
                    return;
                }
                await apiClient.put(`http://127.0.0.1:8000/organo/${organoId}`, this.selectedOrgano);
                console.log("Órgano actualizado con éxito");

                this.fetchOrganos();  // Refresca la lista de órganos después de la actualización
                this.closeModal();    // Cierra el modal después de la actualización
            } catch (error) {
                console.error("Error al actualizar el órgano", error);
            }
        },

        closeModal() {
            this.showModal = false;
        },

        async fetchOrganos() {
            try {
                const response = await apiClient.get(this.api);
                console.log("Datos obtenidos del servidor:", response.data); // Debugging
                this.organos = response.data;
                this.filteredOrganos = this.organos; // Inicialmente muestra todos los órganos
            } catch (error) {
                console.error("Error al obtener los órganos", error);
            }
        },

        async deleteOrgano() {
            try {
                const organoId = this.selectedOrgano.ID;
                if (organoId === null) {
                    console.error("ID del órgano no definido.");
                    return;
                }
                const response = await axios.delete(`http://127.0.0.1:8000/organo/${organoId}`);
                console.log("Órgano eliminado con éxito", response.data);
                this.fetchOrganos(); // Refrescar la lista después de eliminar
                this.closeModal(); // Cerrar el modal después de eliminar
            } catch (error) {
                console.error("Error al eliminar el órgano", error);
            }
        },

        confirmDeleteOrgano(organoId) {
            if (confirm("¿Estás seguro de que deseas eliminar este órgano?")) {
                this.selectedOrgano.ID = organoId;
                this.deleteOrgano();
            }
        },

        searchOrgano() {
            if (this.searchQuery) {
                const query = this.searchQuery.toLowerCase();
                this.filteredOrganos = this.organos.filter(organo => {
                    return (
                        organo.Nombre.toLowerCase().includes(query)
                    );
                });
            } else {
                this.filteredOrganos = this.organos;
            }
        }
    },

    mounted() {
        this.fetchOrganos(); // Llama al método una vez al montar el componente
    }
};
</script>

<style scoped>
.modal {
    display: block;
}

.close {
    cursor: pointer;
}
</style>