<template>
    <form>
        <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
            <div class="flex flex-column sm:flex-row flex-wrap space-y-4 sm:space-y-0 items-center justify-between pb-4">
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
                    <input type="text" id="table-search"
                        class="block p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        placeholder="Search for items">
                </div>
                <div>
                    <RouterLink to="/organform">
                    <button id="dropdownRadioButton" data-dropdown-toggle="dropdownRadio"
                        class="inline-flex items-center text-white bg-blue-500 border border-blue-300 focus:outline-none hover:bg-blue-400 focus:ring-4 focus:ring-blue-100 font-medium rounded-lg text-sm px-3 py-1.5 dark:bg-blue-800 dark:text-white dark:border-blue-600 dark:hover:bg-blue-700 dark:hover:border-blue-600 dark:focus:ring-blue-700"
                        type="button">

                        Agregar Organo
                    </button>
                    </RouterLink>
                </div>
                <label for="table-search" class="sr-only">Search</label>
            </div>
            <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="p-4">
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Donador
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Donatario
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Medico
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Organo
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Prioridad
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Action
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td class="w-4 p-4">
                        </td>
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            Apple MacBook Pro 17"
                        </th>
                        <td class="px-6 py-4">
                            Silver
                        </td>
                        <td class="px-6 py-4">
                            Laptop
                        </td>
                        <td class="px-6 py-4">
                            $2999
                        </td>
                        <td class="px-6 py-4">
                            $2999
                        </td>
                        <td class="px-6 py-4">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline mr-2">
                                <span class="material-symbols-outlined">edit</span>
                            </a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">
                                <span class="material-symbols-outlined">delete</span>
                            </a>
                        </td>
                    </tr>
                    <tr
                        class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td class="w-4 p-4">
                        </td>
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            Microsoft Surface Pro
                        </th>
                        <td class="px-6 py-4">
                            White
                        </td>
                        <td class="px-6 py-4">
                            Laptop PC
                        </td>
                        <td class="px-6 py-4">
                            $1999
                        </td>
                        <td class="px-6 py-4">
                            $1999
                        </td>
                        <td class="px-6 py-4">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline mr-2">
                                <span class="material-symbols-outlined">edit</span>
                            </a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">
                                <span class="material-symbols-outlined">delete</span>
                            </a>
                        </td>
                    </tr>
                    <tr
                        class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td class="w-4 p-4">
                        </td>
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            Magic Mouse 2
                        </th>
                        <td class="px-6 py-4">
                            Black
                        </td>
                        <td class="px-6 py-4">
                            Accessories
                        </td>
                        <td class="px-6 py-4">
                            $99
                        </td>
                        <td class="px-6 py-4">
                            $99
                        </td>
                        <td class="px-6 py-4">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline mr-2">
                                <span class="material-symbols-outlined">edit</span>
                            </a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">
                                <span class="material-symbols-outlined">delete</span>
                            </a>
                        </td>
                    </tr>
                    <tr
                        class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td class="w-4 p-4">
                        </td>
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            Apple Watch
                        </th>
                        <td class="px-6 py-4">
                            Silver
                        </td>
                        <td class="px-6 py-4">
                            Accessories
                        </td>
                        <td class="px-6 py-4">
                            $179
                        </td>
                        <td class="px-6 py-4">
                            $179
                        </td>
                        <td class="px-6 py-4">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline mr-2">
                                <span class="material-symbols-outlined">edit</span>
                            </a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">
                                <span class="material-symbols-outlined">delete</span>
                            </a>
                        </td>
                    </tr>
                    <tr
                        class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td class="w-4 p-4">
                        </td>
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            iPad
                        </th>
                        <td class="px-6 py-4">
                            Gold
                        </td>
                        <td class="px-6 py-4">
                            Tablet
                        </td>
                        <td class="px-6 py-4">
                            $699
                        </td>
                        <td class="px-6 py-4">
                            $699
                        </td>
                        <td class="px-6 py-4">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline mr-2">
                                <span class="material-symbols-outlined">edit</span>
                            </a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">
                                <span class="material-symbols-outlined">delete</span>
                            </a>
                        </td>
                    </tr>
                    <tr class="bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td class="w-4 p-4">
                        </td>
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            Apple iMac 27"
                        </th>
                        <td class="px-6 py-4">
                            Silver
                        </td>
                        <td class="px-6 py-4">
                            PC Desktop
                        </td>
                        <td class="px-6 py-4">
                            $3999
                        </td>
                        <td class="px-6 py-4">
                            $3999
                        </td>
                        <td class="px-6 py-4">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline mr-2">
                                <span class="material-symbols-outlined">edit</span>
                            </a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline">
                                <span class="material-symbols-outlined">delete</span>
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

    </form>
</template>