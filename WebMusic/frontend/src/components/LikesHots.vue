
<script>
import PageHeader from './PageHeader.vue'
import Recommendations from './Recommendations.vue'
import Song from './Song.vue'
import {getHotlist} from '../api/api.js'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
export default{
    components:{
      PageHeader,
      Recommendations,
      Song,
      FontAwesomeIcon,
    },
    data(){
        return{
            hot : [],
        }
    },
    methods:{
        gethot(){
            /*getHotlist().then(
            (res) =>{
                console.log(res);
                for(let i = 0; i < 8; i = i + 1){
                  this.hot.push(res.data.music[i]);
                }
            }*/
            this.hot.push({'id': '865632948', 'name': '若把你', 'artists': ['Kirsty刘瑾睿'], 'url': 'http://music.163.com/song/media/outer/url?id=865632948.mp3', 'pic_url': 'http://p2.music.126.net/M877M2-VhWZiLPVFORf9iQ==/109951163401482434.jpg'});
        },
        playMusic(index){
         
          this.$router.push({name:'Play',query:{id: this.hot[index].id, cover: this.hot[index].pic_url, playUrl: this.hot[index].url}});
        }
    },
    mounted:function(){
        this.gethot();
    }
}
</script>
<template>
  
  <div>
    
    <div class="likesHots" v-for="(song, index) in hot" :key="index">
    <div class="accordingToPreferences">
          
      <Recommendations>
        <template #title>猜你喜欢</template>
        <template #song1>
          <div v-if="index==0" @click="playMusic(0)">
              <Song>
                <template #cover>                  
                  <img :src="song.pic_url" class ="cover"/>
                </template>
                <template #title>
                  {{song.name}}                  
                </template> 
              </Song>
          </div>
        </template>
        <template #song2>
          <div v-if="index==5">
            <Song>
              <template #cover>
                <img :src="song.pic_url" class ="cover"/>
              </template>
              <template #title>
                {{song.name}}      
              </template>
            </Song>
          </div>
        </template>
        <template #song3>
          <div v-if="index==6">
            <Song>
              <template #cover>
                <img :src="song.pic_url" class ="cover" />
              </template>
              <template #title>
                {{song.name}}  
              </template>
            </Song>
          </div>
        </template>
        <template #song4>
          <div v-if="index==7">
            <Song>
              <template #cover>
                <img :src="song.pic_url" class ="cover" />
              </template>
              <template #title>
                {{song.name}}  
              </template>
            </Song>
          </div>
        </template>
      </Recommendations>
    </div>
    <div class="hotList">
      <Recommendations>
        <template #title>当下热门</template>
        <template #song1>
          <div v-if="index==0">
            <Song>
              <template #cover>
                <img :src="song.pic_url" class ="cover" />
              </template>
              <template #title>
                {{song.name}}  
              </template>
            </Song>
          </div>
        </template>
        <template #song2>
          <div v-if="index==1">
            <Song>
              <template #cover>
                <img :src="song.pic_url" class ="cover" />
              </template>
              <template #title>
                {{song.name}}  
              </template>
            </Song>
          </div>
        </template>
        <template #song3>
          <div v-if="index==2">
            <Song>
              <template #cover>
                <img :src="song.pic_url" class ="cover" />
              </template>
              <template #title>
                {{song.name}}  
              </template>
            </Song>
          </div>
        </template>
        <template #song4>
          <div v-if="index==3">
            <Song>
              <template #cover>
                <img :src="song.pic_url" class ="cover" />
              </template>
              <template #title>
                {{song.name}}  
              </template>
            </Song>
          </div>
        </template>
      </Recommendations>
    </div>
    </div>
  </div>
</template>
  
<style scoped>  
.accordingToPreferences{
  z-index: 101;
  top: 243px;
  position: absolute;
} 
.hotList{
  z-index: 101;
  top: 243px;
  left: 798px;
  position: absolute;
}
.cover{
  width: 160px;
  height: 160px;
}
@media (min-width: 1024px) {
}
</style>
  