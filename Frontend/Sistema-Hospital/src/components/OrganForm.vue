<template>
    <form>
        <div class="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8 rounded-lg shadow-lg overflow-hidden">
            <!-- Done Information -->
            <div class="flex justify-between flex flex-col items-center">
                <label class="block text-gray-700 text-3xl font-normal mb-2">Informacion del Donatario</label>
            </div>
            
           
           
           
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Organo</label>
                </div>
                <select
                    className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-center">
                    <option value="">-- Seleciona un Organo --</option>
                </select>
            </div>
            
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Fecha de Registro</label>
                </div>
                <input
                    class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                    type="date" />
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Hora de Registro</label>
                </div>
                <input
                    class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                    type="time" />
            </div>
            <!-- Summary Information -->
            <div class="flex justify-between flex flex-col items-center mt-5">
                <label class="block text-gray-700 text-3xl font-normal mb-2">Resumen de la Donacion</label>
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Nombre del Donador</label>
                </div>
                <input
                    class=" bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                    type="text" disabled />
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Nombre del Donatario</label>
                </div>
                <input
                    class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                    type="text" disabled />
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Nombre del Medico</label>
                </div>
                <input
                    class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                    type="text" disabled />
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Organo</label>
                </div>
                <input
                    class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                    type="text" disabled />
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Prioidad</label>
                </div>
                <input
                    class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                    type="text" disabled />
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Fecha de Registro</label>
                </div>
                <input
                    class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                    type="text" disabled />
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Hora de Registro</label>
                </div>
                <input
                    class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
                    type="text" disabled />
            </div>
            <!-- Send Form -->
            <div class="mt-8">
                <RouterLink to="/TableTransplante">
                    <button class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-500 mb-5">Generar
                        Solicitud</button>
                </RouterLink>
            </div>
        </div>
    </form>
</template>