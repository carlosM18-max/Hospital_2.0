<template>
    <div class="py-16">
      <div class="flex bg-white rounded-lg shadow-lg overflow-hidden mx-auto max-w-sm lg:max-w-4xl">
        <div class="hidden lg:block lg:w-1/2 bg-cover"
          style="background-image:url('https://images.unsplash.com/photo-1546514714-df0ccc50d7bf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=667&q=80')">
        </div>
        <div class="w-full p-8 lg:w-1/2">
          <h2 class="text-2xl font-semibold text-gray-700 text-center">Privilage Care</h2>
          <p class="text-xl text-gray-600 text-center">Bienvenido de vuelta!</p>
          <div class="mt-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Usuario</label>
            <input v-model="username" 
                   class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
                   type="text" />
          </div>
          <div class="mt-4">
            <div class="flex justify-between">
              <label class="block text-gray-700 text-sm font-bold mb-2">Contraseña</label>
              <router-link to="/forgot-password" class="text-xs text-gray-500">Olvidaste tu contraseña?</router-link>
            </div>
            <input v-model="password" 
                   class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" 
                   type="password" />
          </div>
          <div class="mt-8">
            <button @click="login" 
                    class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600">
              Iniciar Sesion
            </button>
          </div>
          <div class="mt-4 flex items-center justify-between">
            <span class="border-b w-1/5 md:w-1/4"></span>
            <router-link to="/register" class="text-xs text-gray-500 uppercase">Crear Cuenta</router-link>
            <span class="border-b w-1/5 md:w-1/4"></span>
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
        username: '',
        password: ''
      };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/login/', {
            Nombre_Usuario: this.username,
            Contrasena: this.password
          });
  
          if (response.status === 200) {
            const token = response.data; // El token recibido del backend
            localStorage.setItem('token', token); // Guarda el token en localStorage
            this.$router.push('/dashboard'); // Redirige al dashboard
          } else {
            alert('Usuario o contraseña incorrectos');
          }
        } catch (error) {
          console.error('Error al iniciar sesión:', error);
          alert('Error al iniciar sesión, verifica tus credenciales');
        }
      }
    }
  };
  </script>
  