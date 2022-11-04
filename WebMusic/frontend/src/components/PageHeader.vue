<script>
import Sign_in from '../Sign_in.vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

export default{
    data() {
        return {
            musicName: "",
            showSignIn : true,
            userName : '',
        };
    },
    methods: {
        searchMusic() {
            this.$router.push({ name: "Search", query: { musicName: this.musicName } });
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
        <img class="background" src="../assets/HomePage/页面上方底色.png" />
        <!--TODO:change the background to an opaque picture><!-->
        <img class="shade" src="../assets/HomePage/阴影.png"/>
        <img class="logo" src="../assets/HomePage/logo.png" />
        <img class="title" src="../assets/HomePage/WebMusic.png" />
        <img class="searchFrame" src="../assets/HomePage/输入外框.png" />
        <img class="searchIcon" @click="searchMusic" src="../assets/HomePage/搜索图标.png" />
        <input class="searchInput" type = "text" v-model="musicName" placeholder="请输入歌曲名">
        <img class="avatar" src="../assets/HomePage/头像.png" />
        <div class ="signin">
            LOGIN 
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
    z-index: 100;
    left: 0px;
    top: 0px;
    width: 100%;
    height: 203px;
    background-color: rgb(255, 255, 255);
    position: fixed;
}
.shade{
    z-index: 100;
    left: 0px;
    top: 201px;
    width: 100%;
    height: 19px;
    position: fixed;
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
    border: 2px solid #0e92b3;
    
}
</style>
