<script>
import Animation from './components/Animation.vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { myLikes } from './api/api';
import { AVWaveform } from 'vue-audio-visual/dist/vue-audio-visual'
import {AVLine} from 'vue-audio-visual/dist/vue-audio-visual'
import {useAVBars} from 'vue-audio-visual/dist/vue-audio-visual'
import Player from '../src/Player.vue'
export default{
    components:{
      Animation,
      FontAwesomeIcon,
      myLikes,
      AVWaveform,
      AVLine,
      useAVBars,
      Player,
    },
    data(){
        return{
            musicId: '',
            cover: '',
            playUrl: '',
            userName:'',
            likeshow:true,
            starshow:true,
        }
        
    },
    methods:{
        changelike(){
            if(this.likeshow){
                myLikes(this.userName,'del',this.musicId).then(
                    (res) =>{
                        console.log(res.data);
                    }
                )
            }else{
                myLikes(this.userName,'add',this.musicId).then(
                    (res) =>{
                        console.log(res.data);
                    }
                )
            }
            this.likeshow = !this.likeshow;
        },
        changestar(){
            this.starshow = !this.starshow;
        },
        show(){
            console.log(this.$refs.foo);
        }
    },
    mounted:function(){
       
        this.musicId = this.$route.query.id;
        this.cover = this.$route.query.cover;
        this.playUrl = this.$route.query.playUrl;
        this.userName = this.$route.query.userName;
        myLikes(this.userName,'queryid',this.musicId).then(
            (res) => {
                console.log(res.data);
                this.likeshow = res.data.exist;
            }
        )
        console.log(this.playUrl);
        console.log(this.$route.query.id);
        }
}
</script>
  
<template>
  <div>
    <div>
        
        <!--TODO:change the background to an opaque picture><!-->
    </div>
    <div class="leftWave">
        <Animation />
    </div>
    <div class="rightWave">
        <Animation />
    </div>
    <img class="cover" :src="cover" />
    <div class="lyric">
    </div>
    <div class="circleButtonLike" @click="changelike">
        <font-awesome-icon icon = "far fa-heart" v-if="!likeshow"/>
        <font-awesome-icon icon = "fas fa-heart" v-if="likeshow"/>
    </div>
    <div class="circleButtonStar" @click="changestar">
        <font-awesome-icon icon = "far fa-star" v-if="starshow"/>
        <font-awesome-icon icon = "fas fa-star" v-if="!starshow"/>
    </div>
    <div class="circleButtonDownload">
        <font-awesome-icon icon="fa-solid fa-cloud-arrow-down" />
    </div>
    <div class="circleButtonShare">
        <font-awesome-icon icon="fa-solid fa-share" />
    </div>
    <div class="player">
        <Player :my-source="playUrl"></Player>
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
    z-index: 101;
    left: 326px;
    top: 226px;
    width: 330px;
    height: 330px;
    position: absolute;
}
.lyric{
    z-index: 101;
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
    z-index: 101;
    top: 13px;
    left: -1px;
    width: 36px;
    height: 36px;
    position: relative;
}
.StarIcon{
    z-index: 101;
    top: 12px;  
    width: 36px;
    height: 36px;
    position: relative;
}
.DownloadIcon{
    z-index: 101;
    top: 12px;  
    width: 36px;
    height: 36px;
    position: relative;
}
.ShareIcon{
    z-index: 101;
    top: 13px;  
    left: -1px;
    width: 36px;
    height: 36px;
    position: relative;
}
.circleButtonLike{
    z-index: 101;
    left: 345px;
    top: 612px;
    width: 60px;
    height: 60px;
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: absolute;
    border-radius: 50%;
    font-size: 45px;
}
.circleButtonStar{
    z-index: 101;
    left: 418px;
    top: 612px;
    width: 60px;
    height: 60px;
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: absolute;
    border-radius: 50%;
    font-size: 43px;
}
.circleButtonDownload{
    z-index: 101;
    left: 491px;
    top: 612px;
    width: 60px;
    height: 60px;
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: absolute;
    border-radius: 50%;
    font-size: 40px;
}
.circleButtonShare{
    z-index: 101;
    left: 564px;
    top: 612px;
    width: 60px;
    height: 60px;
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: absolute;
    border-radius: 50%;
    font-size: 40px;
}
.player{
    z-index:101;
    left: 564px;
    top: 762px;
    width: 300px;
    height: 60px;
    text-align: center;
    position: absolute;
   
}
</style>
  