<template>
    <form>
        <!-- https://play.tailwindcss.com/MIwj5Sp9pw -->
        <div class="py-16">
            <div class="flex bg-white rounded-lg shadow-lg overflow-hidden mx-auto max-w-sm lg:max-w-6xl">
                <!-- <div class="hidden lg:block lg:w-1/2 bg-cover"
            style="background-image:url('https://images.unsplash.com/photo-1546514714-df0ccc50d7bf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=667&q=80')">
        </div> -->
                <div class="w-full p-8 lg:w-1/2">
                    <h2 class="text-2xl font-semibold text-gray-700 text-center mb-5">Privilage Care</h2>
                    <p class="text-xl text-gray-600 text-center">Crea una Cuenta!</p>
                    <Person></Person>
                </div>
                <div class="w-full p-8 lg:w-1/2 mb-20">
                    <h2 class="text-2xl font-semibold text-gray-700 text-center mb-20"></h2>
                    <p class="text-xl text-gray-600 text-center"></p>
                    <User></User>
                </div>
            </div>
        </div>
    </form>
</template>
<script>
import Person from './Person.vue';
import User from './User.vue';
export default {
    components: {
        Person,
        User
    }
}
</script>