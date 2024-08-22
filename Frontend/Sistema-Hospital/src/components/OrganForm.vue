<template>
  <form @submit.prevent="addOrgano">
    <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 rounded-lg shadow-lg overflow-hidden mt-5">
      <div class="flex justify-between flex-col items-center">
        <label class="block text-gray-700 text-3xl font-normal mb-2">Datos del órgano</label>
      </div>

      <!-- Nombre -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Nombre</label>
        </div>
        <input v-model="selectedOrgano.Nombre"
          class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
          type="text" placeholder="Introduce el nombre" required />
      </div>

      <!-- Edad del Donante -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Edad del Donante</label>
        </div>
        <input v-model="selectedOrgano.Edad_Donante"
          class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
          type="number" placeholder="Introduce la edad del donante" required />
      </div>

      <!-- Fecha de Extracción -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Fecha de Extracción</label>
        </div>
        <input v-model="selectedOrgano.Fecha_Extraccion"
          class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
          type="datetime-local" required />
      </div>

      <!-- Aparato y Sistema -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Aparato y Sistema</label>
        </div>
        <select v-model="selectedOrgano.Aparato_Sistema"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center"
          required>
          <option value="">-- Selecciona una opción --</option>
          <option v-for="aparato in aparatosSistemas" :key="aparato" :value="aparato">
            {{ aparato }}
          </option>
        </select>
      </div>

      <!-- Tipo -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Tipo</label>
        </div>
        <select v-model="selectedOrgano.Tipo"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center"
          required>
          <option value="">-- Selecciona una opción --</option>
          <option v-for="tipo in tipos" :key="tipo" :value="tipo">
            {{ tipo }}
          </option>
        </select>
      </div>

      <!-- Grupo Sanguíneo -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Grupo Sanguíneo</label>
        </div>
        <select v-model="selectedOrgano.Grupo_Sanguineo"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center"
          required>
          <option value="">-- Selecciona una opción --</option>
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
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Estado de Salud</label>
        </div>
        <select v-model="selectedOrgano.Estado_Salud"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center"
          required>
          <option value="">-- Selecciona una opción --</option>
          <option v-for="estado in estadosSalud" :key="estado" :value="estado">
            {{ estado }}
          </option>
        </select>
      </div>

      <!-- Disponibilidad -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Disponibilidad</label>
        </div>
        <select v-model="selectedOrgano.Disponibilidad"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center"
          required>
          <option value="">-- Selecciona una opción --</option>
          <option v-for="disponibilidad in disponibilidades" :key="disponibilidad" :value="disponibilidad">
            {{ disponibilidad }}
          </option>
        </select>
      </div>

      <!-- Detalles Adicionales -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Detalles Adicionales</label>
        </div>
        <textarea v-model="selectedOrgano.Detalles_Adicionales"
          class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
          rows="4" placeholder="Escribe detalles adicionales"></textarea>
      </div>



      <!-- Enfermedades Transmisibles -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Enfermedades Transmisibles</label>
        </div>
        <select v-model="selectedOrgano.Enfermedades_Transmisibles"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center"
          required>
          <option :value="null">-- Selecciona una opción --</option> <!-- Cambiado a :value="null" -->
          <option :value="true">Sí</option>
          <option :value="false">No</option>
        </select>
      </div>



      <!-- Estatus -->
      <div class="mt-4">
        <div class="flex justify-between">
          <label class="block text-gray-700 text-sm font-bold mb-2">Estatus</label>
        </div>
        <select v-model="selectedOrgano.Estatus"
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center"
          required>
          <option value="">-- Selecciona una opción --</option>
          <option :value="true">Activo</option>
          <option :value="false">Inactivo</option>
        </select>
      </div>

      <!-- Botón de Envío -->
      <div class="mt-8">
        <button type="submit" class="bg-blue-500 text-white font-bold py-2 px-4 w-full rounded hover:bg-blue-600 mb-5">
          Agregar Órgano
        </button>
      </div>
    </div>
  </form>
</template>

<script>
import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:8000/",
});

export default {
  data() {
    return {
      selectedOrgano: {
        Nombre: "",
        Aparato_Sistema: "",
        Detalles_Adicionales: "",
        Disponibilidad: "",
        Tipo: "",
        Estado: "",
        Fecha_Extraccion: "",
        Edad_Donante: null,
        Grupo_Sanguineo: "",
        Estado_Salud: "",
        Enfermedades_Transmisibles: null,
        Estatus: "",
      },
      aparatosSistemas: [
        "Circulatorio",
        "Digestivo",
        "Respiratorio",
        "Nervioso",
        "Muscular",
        "Esquelético",
        "Endocrino",
        "Linfático",
        "Inmunológico",
        "Reproductor",
        "Urinario",
        "Sensorial",
      ],
      disponibilidades: ["En Proceso", "Disponible", "No Disponible", "Reservado", "Entregado"],
      tipos: ["Vital", "No Vital"],
      estadosSalud: ["Excelente", "Bueno", "Regular", "Pobre", "Crítico"], // Opciones dinámicas para el Estado de Salud
    };
  },
  methods: {
    async addOrgano() {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        };

        // Validación adicional (opcional) de campos antes de enviar
        if (!this.selectedOrgano.Nombre || !this.selectedOrgano.Aparato_Sistema) {
          alert("Todos los campos son obligatorios.");
          return;
        }

        const response = await apiClient.post("organo/", this.selectedOrgano, config);
        console.log("Respuesta del servidor:", response.data); // Añadir este log para ver la respuesta del servidor

        alert("Órgano agregado con éxito");
        this.resetForm();
      } catch (error) {
        console.error("Error al agregar el órgano", error.response ? error.response.data : error.message); // Mostrar errores detallados
        alert(`Error al agregar el órgano: ${error.response ? error.response.data.detail : error.message}`);
      }
    },
    resetForm() {
      this.selectedOrgano = {
        Nombre: "",
        Aparato_Sistema: "",
        Detalles_Adicionales: "",
        Disponibilidad: "",
        Tipo: "",
        Estado: "",
        Fecha_Extraccion: "",
        Edad_Donante: null,
        Grupo_Sanguineo: "",
        Estado_Salud: "",
        Enfermedades_Transmisibles: null,
        Estatus: "",
      };
    },
  },
};
</script>


<style scoped>
/* Add your component-specific styles here */
</style>