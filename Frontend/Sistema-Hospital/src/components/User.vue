<template>
  <form @submit.prevent="registerUser">
    <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 rounded-lg shadow-lg overflow-hidden mt-5">
      <!-- Información de la Persona -->
      <div class="flex justify-between flex-col items-center">
        <label class="block text-gray-700 text-3xl font-normal mb-2">Registro de Persona</label>
      </div>
      
      <!-- Título de Cortesía -->
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Título de Cortesía</label>
        <input v-model="person.Titulo"
               class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
               type="text" 
               placeholder="Sr., Sra., Dr., etc." 
               required />
      </div>

      <!-- Nombre -->
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Nombre</label>
        <input v-model="person.Nombre"
               class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
               type="text" 
               placeholder="Introduce tu nombre" 
               required />
      </div>

      <!-- Primer Apellido -->
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Primer Apellido</label>
        <input v-model="person.Primer_Apellido" 
               class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
               type="text" 
               placeholder="Introduce tu primer apellido" 
               required />
      </div>

      <!-- Segundo Apellido -->
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Segundo Apellido</label>
        <input v-model="person.Segundo_Apellido" 
               class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
               type="text" 
               placeholder="Introduce tu segundo apellido" />
      </div>
      <!-- Segundo CURP -->
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">CURP</label>
        <input v-model="person.Curp" 
               class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
               type="text" 
               placeholder="Introduce tu segundo apellido" />
      </div>

      <!-- Fecha de Nacimiento -->
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Fecha de Nacimiento</label>
        <input v-model="person.Fecha_Nacimiento" 
               class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
               type="date" 
               required />
      </div>

      <!-- Género -->
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Género</label>
        <select v-model="person.Genero" 
                class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
                required>
          <option value="Masculino">Masculino</option>
          <option value="Femenino">Femenino</option>
          <option value="Otro">Otro</option>
        </select>
      </div>

      <!-- Tipo de Sangre -->
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Tipo de Sangre</label>
        <select v-model="person.Tipo_Sangre" 
                class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
                required>
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

      <!-- Fotografía -->
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Fotografía</label>
        <input v-model="person.Fotografia" 
               class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
               type="text" 
               placeholder="URL de la fotografía" />
      </div>

       <!-- Segundo Telefono -->
       <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Telefono</label>
        <input v-model="person.Telefono" 
               class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
               type="text" 
               placeholder="Introduce tu segundo apellido" />
      </div>

       <!-- Segundo Correo -->
       <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Correo_Electronico</label>
        <input v-model="person.Correo_Electronico" 
               class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
               type="text" 
               placeholder="Introduce tu segundo apellido" />
      </div>

      <!-- Información del Usuario -->
      <div class="flex justify-between flex-col items-center mt-10">
        <label class="block text-gray-700 text-3xl font-normal mb-2">Información de Usuario</label>
      </div>

      <!-- Nombre de Usuario -->
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Nombre de Usuario</label>
        <input v-model="user.Nombre_Usuario" 
               class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
               type="text" 
               placeholder="Introduce tu nombre de usuario" 
               required />
      </div>

      <!-- Correo Electrónico -->
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Correo Electrónico</label>
        <input v-model="user.Correo_Electronico" 
               class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
               type="email" 
               placeholder="Introduce tu correo electrónico" 
               required />
      </div>

      <!-- Contraseña -->
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Contraseña</label>
        <input v-model="user.Contrasena" 
               class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
               type="password" 
               placeholder="Introduce tu contraseña" 
               required />
      </div>

      <!-- Confirmar Contraseña -->
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Confirmar Contraseña</label>
        <input v-model="confirmPassword" 
               class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
               type="password" 
               placeholder="Confirma tu contraseña" 
               required />
      </div>

      <!-- Número Telefónico Móvil -->
      <div class="mt-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Número Telefónico Móvil</label>
        <input v-model="user.Numero_Telefonico_Movil" 
               class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
               type="tel" 
               placeholder="Introduce tu número telefónico móvil" 
               required />
      </div>

       <!-- Botones de Envío y Cancelar -->
      <div class="mt-8 flex justify-between">
        <button @click="registerUser" 
                class="bg-gray-700 text-white font-bold py-2 px-4 rounded hover:bg-gray-500 mb-5">
          Crear Cuenta
        </button>

        <a href="/">
        <button  
                type="button" 
                class="bg-red-500 text-white font-bold py-2 px-4 rounded hover:bg-red-400 mb-5">
          Cancelar
        </button>
      </a>
      </div>
    </div>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      person: {
        Titulo: '',
        Nombre: '',
        Primer_Apellido: '',
        Segundo_Apellido: '',
        Curp: '',
        Fecha_Nacimiento: '',
        Fotografia: '',
        Telefono: '',
        Correo_Electronico: '',
        Genero: 'Masculino',
        Tipo_Sangre: 'A+',
        Estatus: true,
        Fecha_Registro: new Date().toISOString(),
        Fecha_Actualizacion: new Date().toISOString(),
      },
      user: {
        Nombre_Usuario: '',
        Correo_Electronico: '',
        Contrasena: '',
        Numero_Telefonico_Movil: '',
        Rol: 'Usuario', // Asignar un rol predeterminado si es necesario
        Estatus: true,
        Fecha_Registro: new Date().toISOString(),
        Fecha_Actualizacion: new Date().toISOString(),
      },
      confirmPassword: '',
    };
  },
  methods: {
    async registerUser() {
      if (this.user.Contrasena !== this.confirmPassword) {
        alert('Las contraseñas no coinciden.');
        return;
      }

      try {
        // Crear Persona
        const personResponse = await axios.post('http://127.0.0.1:8000/person/', this.person);
        const personId = personResponse.data.Persona_ID;

        // Crear Usuario con el ID de la Persona
        this.user.Persona_ID = personId;
        const userResponse = await axios.post('http://127.0.0.1:8000/users/', this.user);

        if (userResponse.status === 201) {
          alert('Cuenta creada exitosamente');
          this.clearForm();
        } else {
          alert('Error al crear la cuenta');
        }
      } catch (error) {
        console.error('Error al crear la cuenta:', error);
        if (error.response && error.response.data) {
          alert(`Hubo un problema al crear tu cuenta: ${JSON.stringify(error.response.data)}`);
        } else {
          alert('Hubo un problema al crear tu cuenta. Inténtalo de nuevo.');
        }
      }
    },
    cancelRegistration() {
      // Implementa la lógica para cancelar el registro
      this.clearForm();
    },
    clearForm() {
      // Limpia los formularios
      this.person = {
        Titulo: '',
        Nombre: '',
        Primer_Apellido: '',
        Segundo_Apellido: '',
        Curp: '',
        Fecha_Nacimiento: '',
        Fotografia: '',
        Telefono: '',
        Correo_Electronico: '',
        Genero: 'Masculino',
        Tipo_Sangre: 'A+',
        Estatus: true,
        Fecha_Registro: new Date().toISOString(),
        Fecha_Actualizacion: new Date().toISOString(),
      };
      this.user = {
        Nombre_Usuario: '',
        Correo_Electronico: '',
        Contrasena: '',
        Numero_Telefonico_Movil: '',
        Rol: 'Usuario', // Asignar un rol predeterminado si es necesario
        Estatus: true,
        Fecha_Registro: new Date().toISOString(),
        Fecha_Actualizacion: new Date().toISOString(),
      };
      this.confirmPassword = '';
    },
  },
};
</script>

<style scoped>
/* Agrega tus estilos personalizados aquí si es necesario */
</style>
