<script setup>
  import {ref} from 'vue'
  import HelloWorld from '../components/HelloWorld.vue';
  let musicName = ref('')
  function searchMusic(){
    console.log(musicName);
  }
  function change(e){
    this.$forceUpdate()
  }
</script>
<template>
    <div>
        <img class="background" src="../assets/HomePage/页面上方底色.png" />
        <img class="shade" src="../assets/HomePage/阴影.png"/>
        <img class="logo" src="../assets/HomePage/logo.png" />
        <img class="title" src="../assets/HomePage/WebMusic.png" />
        <img class="searchFrame" src="../assets/HomePage/输入外框.png" />
        <img class="searchIcon" @click="searchMusic" src="../assets/HomePage/搜索图标.png" />
        <input class="searchInput" type = "text" v-model="musicName" placeholder="请输入歌曲名">
        <img class="avatar" src="../assets/HomePage/头像.png" />
        <img class="signin" src="../assets/HomePage/登录注册.png" />
    </div>  
</template>

<style scoped>
.logo{
    left: 100px;
    top: 30px;
    width: 150px;
    height: 150px;
    background-color: rgba(255, 255, 255, 0);
    position: fixed;
}
.title{
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
    left: 0px;
    top: 0px;
    width: 100%;
    height: 203px;
    line-height: 20px;
    background-color: rgba(180, 253, 255, 0.25);
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: fixed;
}
.shade{
    left: 0px;
    top: 201px;
    width: 100%;
    height: 19px;
    position: fixed;
}
.searchFrame{
    left: 280px;
    top: -155px;
    width: 817px;
    height: 817px;
    position: fixed;
}
.searchInput{
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
    left: 862px;
    top: 95px;
    width: 33px;
    height: 33px;
    position: fixed;
}
.avatar{
    left: 1370px;
    top: 55px;
    width: 100px;
    height: 100px;
    line-height: 20px;
    text-align: center;
    position: fixed;
}
.signin{
    left: 1160px;
    top: 82px;
    width: 172px;
    height: 50px;
    line-height: 20px;
    background-color: rgba(255, 255, 255, 1);
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: fixed;
}
@media (min-width: 1440px) {
    .logo{
    left: 100px;
    top: 30px;
    width: 150px;
    height: 150px;
    background-color: rgba(255, 255, 255, 0);
    position: fixed;
}
.title{
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
    left: 0px;
    top: 0px;
    width: 100%;
    height: 203px;
    line-height: 20px;
    background-color: rgba(180, 253, 255, 0.25);
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: fixed;
}
.shade{
    left: 0px;
    top: 201px;
    width: 100%;
    height: 19px;
    position: fixed;
}
.searchFrame{
    left: 280px;
    top: -155px;
    width: 817px;
    height: 817px;
    position: fixed;
}
.searchInput{
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
    left: 862px;
    top: 95px;
    width: 33px;
    height: 33px;
    position: fixed;
}
.avatar{
    left: 1370px;
    top: 55px;
    width: 100px;
    height: 100px;
    line-height: 20px;
    text-align: center;
    position: fixed;
}
.signin{
    left: 1160px;
    top: 82px;
    width: 172px;
    height: 50px;
    line-height: 20px;
    background-color: rgba(255, 255, 255, 1);
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: fixed;
}
}
</style>