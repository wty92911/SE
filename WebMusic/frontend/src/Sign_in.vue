<script setup>
import { ref } from 'vue'

const text1 = ref('')
const text2 = ref('')

</script>

<template>
    <div>
        <img class = "background" src = "./assets/sign_in/矩形 3 Copy@1x.png" />
        <img class = "logo" src = "./assets/HomePage/logo.png" />
        <img class = "title" src = "./assets/sign_in/WebMusic@1x.png" />
    </div>
    <div class = "sign_in_button">
        <img class = "sign_in_icon" src = "./assets/sign_in/按钮2@1x.png" />
    </div>
    <div class = "username">
        <input v-model="text1" placeholder="username">
        <p>{{ text1 }}</p>
    </div>
    <div>
        <img 
    </div>
    <div class = "password">
        <input v-model="text2" placeholder="password">
        <p>{{ text2 }}</p>
    </div>
</template>

