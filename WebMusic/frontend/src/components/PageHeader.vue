<script>
import Sign_in from '../Signin.vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { watch } from 'vue';
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
            this.$router.push({ name: "Search", query: { musicName: this.musicName ,userName : this.userName} });
        },
        showsign(){
            this.showSignIn = true;
        }
    },
    components: { 
        Sign_in,
        FontAwesomeIcon,
    },
    mounted:function(){
        this.$router.push( {name : 'LikesHots',query:{userName:this.userName}});
    },
    watch:{
        userName:function(){
            this.$router.push({name : 'LikesHots',query:{userName:this.userName}});
        }
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
        <font-awesome-icon icon="fa-solid fa-magnifying-glass" class="searchIcon" @click="searchMusic"/>
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
.searchInput{
    z-index: 100;
    left: 527px;
    top: 95px;
    width: 295px;
    height: 28px;
    color: rgba(136, 136, 136, 1);
    background-color: rgba(32, 74, 102, 0);
    font-size: 25px;
    text-align: left;
    font-family: Microsoft Yahei;
    outline: none;
    border: 0;
    outline:none;
    position: fixed;
    border: 1px solid #d3e7ec75;
    border-radius: 30px;

}
.searchIcon{
    z-index: 100;
    left: 862px;
    top: 95px;
    width: 33px;
    height: 33px;
    position: fixed;
}
.signin{
    z-index: 100;
    left: 1160px;
    top: 82px;
    width: 100px;
    height: 50px;
    text-align: center;
    position: fixed;
    font-size: 30px;
    border-radius: 20px;
    border: 1px solid #d3e7ec75;
    font-style: normal;
    font-family: Microsoft Yahei;
    color: rgb(44, 40, 40);
    
}
</style>
