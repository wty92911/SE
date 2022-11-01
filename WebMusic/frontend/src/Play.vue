<script setup>
  import Animation from './components/Animation.vue'

</script>
  
<template>
  <div>
    <div>
        <img class="background" src="./assets/HomePage/页面上方底色.png" />
        <!--TODO:change the background to an opaque picture><!-->
        <img class="shade" src="./assets/HomePage/阴影.png"/>
        <img class="logo" src="./assets/HomePage/logo.png" />
        <img class="title" src="./assets/HomePage/WebMusic.png" />
    </div>
    <div class="leftWave">
        <Animation />
    </div>
    <div class="rightWave">
        <Animation />
    </div>
    <img class="cover" src="./assets/播放/专辑封面.png" />
    <div class="lyric">
    </div>
    <div class="circleButtonLike">
        <img class="LikeIcon" src="./assets/播放/喜欢button.png" />
    </div>
    <div class="circleButtonStar">
        <img class="StarIcon" src="./assets/播放/收藏button.png" />
    </div>
    <div class="circleButtonDownload">
        <img class="DownloadIcon" src="./assets/播放/下载button.png" />
    </div>
    <div class="circleButtonShare">
        <img class="ShareIcon" src="./assets/播放/分享button.png" />
    </div>
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
.leftWave{
    position: absolute;
    top: 212px;
}
.rightWave{
    position: absolute;
    top: 212px;
    margin-left: auto;
    transform: scale(-1,1);
    right: 0;
}
.cover{
    left: 326px;
    top: 226px;
    width: 330px;
    height: 330px;
    position: absolute;
}
.lyric{
    left: 763px;
    top: 226px;
    width: 408px;
    height: 460px;
    line-height: 20px;
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: absolute;
}
.LikeIcon{
    top: 13px;
    left: -1px;
    width: 36px;
    height: 36px;
    position: relative;
}
.StarIcon{
    top: 12px;  
    width: 36px;
    height: 36px;
    position: relative;
}
.DownloadIcon{
    top: 12px;  
    width: 36px;
    height: 36px;
    position: relative;
}
.ShareIcon{
    top: 13px;  
    left: -1px;
    width: 36px;
    height: 36px;
    position: relative;
}
.circleButtonLike{
    left: 345px;
    top: 612px;
    width: 60px;
    height: 60px;
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: absolute;
    border-radius: 50%;
}
.circleButtonStar{
    left: 418px;
    top: 612px;
    width: 60px;
    height: 60px;
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: absolute;
    border-radius: 50%;
}
.circleButtonDownload{
    left: 491px;
    top: 612px;
    width: 60px;
    height: 60px;
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: absolute;
    border-radius: 50%;
}
.circleButtonShare{
    left: 564px;
    top: 612px;
    width: 60px;
    height: 60px;
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: absolute;
    border-radius: 50%;
}
</style>
  