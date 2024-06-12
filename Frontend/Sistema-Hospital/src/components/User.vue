<template>
    <form>
        <!-- user section -->
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Usuario</label>
            </div>
            <input
                class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                type="text" />
        </div>
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Contraseña</label>
            </div>
            <input
                class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                type="password" />
        </div>
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Confirmar Contraseña</label>
            </div>
            <input
                class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                type="password" />
        </div>
        <div class="mt-8">
            <button class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600">Crear
                Cuenta</button>
        </div>
        <div class="mt-8">
            <button class="bg-red-500 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600">Cancelar</button>
        </div>
        <div class="mt-4 flex items-center justify-between">
            <span class="border-b w-1/5 md:w-1/4"></span>
            <a href="/" class="text-xs text-gray-500 uppercase text-center">Ya tienes una cuenta? Inicia Sesion</a>
            <span class="border-b w-1/5 md:w-1/4"></span>
        </div>
    </form>
</template>