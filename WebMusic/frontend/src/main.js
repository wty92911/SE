import { createApp } from 'vue'
import App from './App.vue'
import ElementUI from 'element-plus'
import Axios from 'axios'
import VueAxios from 'vue-axios'
import './assets/main.css'
const app = createApp(App).use(VueAxios,Axios)
app.use(ElementUI)
app.mount('#app')