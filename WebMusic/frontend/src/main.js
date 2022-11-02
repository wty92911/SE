import { createApp } from 'vue'
import App from './App.vue'
import ElementUI from 'element-plus'
import Axios from 'axios'
import VueAxios from 'vue-axios'
import {createRouter,createWebHashHistory} from 'vue-router'
import Play from './Play.vue'
import Like from './components/LikesHots.vue'
import Search from './Search.vue'
const Player = {template : '<div>Play</div>'}
const app = createApp(App).use(VueAxios,Axios)
const routes = [
    {path :"/LikesHots",name:"LikesHots",component: Like},
    {path :"/Search",name:"Search",component: Search},
]
const router = createRouter({
    // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
    history: createWebHashHistory(),
    routes, // `routes: routes` 的缩写
})
app.use(router)
app.use(ElementUI)
app.mount('#app')
