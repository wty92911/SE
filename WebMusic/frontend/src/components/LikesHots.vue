
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
            hotpic1 : "../assets/HomePage/歌曲封面.png",
            hotpic2 : "../assets/HomePage/歌曲封面.png",
            hotpic3 : "../assets/HomePage/歌曲封面.png",
            hotpic4 : "../assets/HomePage/歌曲封面.png",
            hotpic5 : "../assets/HomePage/歌曲封面.png",
            hotpic6 : "../assets/HomePage/歌曲封面.png",
            hotpic7 : "../assets/HomePage/歌曲封面.png",
            hotpic8 : "../assets/HomePage/歌曲封面.png",
            hotname1 : "",
            hotname2 : "",
            hotname3 : "",
            hotname4 : "",
            hotname5 : "",
            hotname6 : "",
            hotname7 : "",
            hotname8 : "",
        }
    },
    methods:{
        gethot(){
            getHotlist().then(
            (res) =>{
                console.log(res);
                this.hotpic1 = res.data.music[0].pic_url;
                this.hotpic2 = res.data.music[1].pic_url;
                this.hotpic3 = res.data.music[2].pic_url;
                this.hotpic4 = res.data.music[3].pic_url;
                this.hotpic5 = res.data.music[4].pic_url;
                this.hotpic6 = res.data.music[5].pic_url;
                this.hotpic7 = res.data.music[6].pic_url;
                this.hotpic8 = res.data.music[7].pic_url;
                this.hotname1 = res.data.music[0].name;
                this.hotname2 = res.data.music[1].name;
                this.hotname3 = res.data.music[2].name;
                this.hotname4 = res.data.music[3].name;
                this.hotname5 = res.data.music[4].name;
                this.hotname6 = res.data.music[5].name;
                this.hotname7 = res.data.music[6].name;
                this.hotname8 = res.data.music[7].name;
            }
            )
        },
    },
    mounted:function(){
        this.gethot();
    }
}
</script>
<template>
  
  <div>
    
    <div class="likesHots">
    <div class="accordingToPreferences">
      <Recommendations>
        
        <template #title>猜你喜欢</template>
        <template #song1>
          <Song>
            <template #cover>
              <img :src="hotpic5" class ="cover"/>
            </template>
            <template #title>
              {{hotname5}}
            </template>
          </Song>
        </template>
        <template #song2>
          <Song>
            <template #cover>
              <img :src="hotpic6" class ="cover"/>
            </template>
            <template #title>
              {{hotname6}}
         
            </template>
          </Song>
        </template>
        <template #song3>
          <Song>
            <template #cover>
              <img :src="hotpic7" class ="cover" />
            </template>
            <template #title>
              {{hotname7}}
            </template>
          </Song>
        </template>
        <template #song4>
          <Song>
            <template #cover>
              <img :src="hotpic8" class ="cover"/>
            </template>
            <template #title>
              {{hotname8}}
            </template>
          </Song>
        </template>
      </Recommendations>
    </div>
    <div class="hotList">
      <Recommendations>
        <template #title>当下热门</template>
        <template #song1>
          <Song>
            <template #cover>
              <img :src="hotpic1" class ="cover"/>
            </template>
            <template #title>
              {{hotname1}}
            </template>
          </Song>
        </template>
        <template #song2>
          <Song>
            <template #cover>
              <img :src="hotpic2" class ="cover"/>
            </template>
            <template #title>
              {{hotname2}}
            </template>
          </Song>
        </template>
        <template #song3>
          <Song>
            <template #cover>
              <img :src="hotpic3" class ="cover"/>
            </template>
            <template #title>
              {{hotname3}}
            </template>
          </Song>
        </template>
        <template #song4>
          <Song>
            <template #cover>
              <img :src="hotpic4" class ="cover"/>
            </template>
            <template #title>
              {{hotname4}}
            </template>
          </Song>
        </template>
      </Recommendations>
    </div>
    </div>
  </div>
</template>
  
<style scoped>  
.accordingToPreferences{
  z-index: 0;
  top: 243px;
  position: absolute;
} 
.hotList{
  z-index: 0;
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
  