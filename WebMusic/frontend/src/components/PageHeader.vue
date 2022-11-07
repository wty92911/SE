<script>
import Sign_in from '../Sign_in.vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { treeEmits } from 'element-plus/es/components/tree-v2/src/virtual-tree';

export default{
    data() {
        return {
            musicName: "",
            showSignIn : false,
            userName : '登录',
        };
    },
    methods: {
        searchMusic() {
            this.$router.push({ name: "Search", query: { musicName: this.musicName } });
        },
        showsign(){
            this.showSignIn = true;
        }
    },
    components: { 
        Sign_in,
        FontAwesomeIcon,
    }
}
</script>
<template>
    <Sign_in :showSignIn="showSignIn" userName="userName"></Sign_in>
    <div> 
        <div class = "shade">
            <img class="background" src="../assets/HomePage/background.jpg" />
        </div>
        
        <!--TODO:change the background to an opaque picture><!-->
       
        <img class="logo" src="../assets/HomePage/logo.png" />
        <img class="title" src="../assets/HomePage/WebMusic.png" />
        <img class="searchFrame" src="../assets/HomePage/输入外框.png" />
        <img class="searchIcon" @click="searchMusic" src="../assets/HomePage/搜索图标.png" />
        <input class="searchInput" type = "text" v-model="musicName" placeholder="请输入歌曲名">
        <div class ="signin" @click="showsign">
            {{userName}}
        </div>
        <!--修改登录注册 美观点-->
    </div> 

</template>

<style scoped>

.logo{
    z-index: 100;
    left: 100px;
    top: 30px;
    width: 150px;
    height: 150px;
    background-color: rgba(255, 255, 255, 0);
    position: fixed;
}
.title{
    z-index: 100;
    left: 250px;
    top: 90px;
    width: 180px;
    height: 50px;
    color: rgba(64, 149, 229, 1);
    font-size: 36px;
    text-align: left;
    font-family: 方正综艺体-标准;
    position: fixed;
}
.background{
    z-index: 99;
    left: 0px;
    top: 0px;
    width: 100%;
    
    opacity: 0.9;
    background-color: rgb(255, 255, 255);
    position: fixed;
}
.shade{
    z-index: 100;
    height: 100%;
    font-family: JetBrains Mono Medium;
    display: flex;
    align-items: center;
    justify-content: center;
    /* background-color: #0e92b3; */
    background-color: rgba(0, 10, 14, 0.532);
    background-size: 100% 100%;
    width: 100%;
    height: 100%;
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
}
.searchFrame{
    z-index: 100;
    left: 280px;
    top: -155px;
    width: 817px;
    height: 817px;
    position: fixed;
}
.searchInput{
    z-index: 100;
    left: 527px;
    top: 95px;
    width: 295px;
    height: 28px;
    color: rgba(136, 136, 136, 1);
    font-size: 28px;
    text-align: left;
    font-family: Microsoft Yahei;
    outline: none;
    border: 0;
    position: fixed;
}
.searchIcon{
    z-index: 100;
    left: 862px;
    top: 95px;
    width: 33px;
    height: 33px;
    position: fixed;
}
.avatar{
    z-index: 100;
    left: 1370px;
    top: 55px;
    width: 100px;
    height: 100px;
    line-height: 20px;
    text-align: center;
    position: fixed;
}
.signin{
    z-index: 101;
    left: 1160px;
    top: 82px;
    width: 100px;
    height: 50px;
    text-align: center;
    position: fixed;
    font-size: 40px;
    border-radius: 20px;
    border: 1px solid #d3e7ec75;
    font-style: normal;
    color: rgb(44, 40, 40);
    
}
</style>
