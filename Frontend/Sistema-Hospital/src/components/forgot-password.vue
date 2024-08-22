<template>
    <div class="py-16">
      <div class="flex bg-white rounded-lg shadow-lg overflow-hidden mx-auto max-w-sm lg:max-w-4xl">
        <div class="hidden lg:block lg:w-1/2 bg-cover"
          style="background-image:url('https://images.unsplash.com/photo-1546514714-df0ccc50d7bf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=667&q=80')">
        </div>
        <div class="w-full p-8 lg:w-1/2">
          <h2 class="text-2xl font-semibold text-gray-700 text-center">Recuperar Contraseña</h2>
          <p class="text-xl text-gray-600 text-center">Introduce tu correo electrónico</p>
          <div class="mt-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Correo Electrónico</label>
            <input v-model="email" 
                   class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
                   type="email" />
          </div>
          <div class="mt-8">
            <button @click="sendRecoveryEmail" 
                    class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600">
              Enviar Enlace de Recuperación
            </button>
          </div>
          <div class="mt-4 flex items-center justify-between">
            <router-link to="/" class="text-xs text-gray-500 uppercase">Volver al Inicio de Sesión</router-link>
        </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        email: ''
      };
    },
    methods: {
      async sendRecoveryEmail() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/password-reset/', { email: this.email });
  
          if (response.status === 200) {
            alert('Hemos enviado un enlace de recuperación a tu correo.');
          } else {
            alert('No se pudo enviar el correo de recuperación. Verifica tu correo electrónico.');
          }
        } catch (error) {
          console.error('Error al enviar el correo de recuperación:', error);
          alert('Hubo un problema al enviar el correo de recuperación. Inténtalo de nuevo.');
        }
      }
    }
  };
  </script>
  