<template>
    <form>
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Nombre</label>
            </div>
            <input
                class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                type="text" />
        </div>
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Primer Apellido</label>
            </div>
            <input
                class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                type="text" />
        </div>
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Segundo Apellido</label>
            </div>
            <input
                class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                type="text" />
        </div>
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">CURP</label>
            </div>
            <input
                class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                type="text" />
        </div>
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Genero</label>
            </div>
            <select
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
                <option value="">-- Selecione su genero --</option>
                <option>Hombre</option>
                <option>Mujer</option>
                <option>Otro</option>
            </select>
        </div>
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Sangre</label>
            </div>
            <select
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
                <option value="">-- Selecione su tipo de sangre --</option>
                <option>A+</option>
                <option>A-</option>
                <option>B+</option>
                <option>B-</option>
                <option>AB+</option>
                <option>AB-</option>
                <option>O+</option>
                <option>O-</option>
            </select>
        </div>
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Fecha de Nacimiento</label>
            </div>
            <input
                class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                type="date" />
        </div>
        <div class="mt-4">
            <div class="flex justify-between">
                <label class="block text-gray-700 text-sm font-bold mb-2">Telefono</label>
            </div>
            <input
                class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                type="text" />
        </div>
        <div class="mt-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Correo electronico</label>
            <input
                class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                type="email" />
        </div>
        <div class="mt-8">
            <button class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600">Crear
                Cuenta</button>
        </div>
    </form>
</template>