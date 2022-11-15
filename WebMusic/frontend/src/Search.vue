<script >
  import HelloWorld from './components/HelloWorld.vue'
  import PageHeader from './components/PageHeader.vue'
  import SearchResults from './components/SearchResults.vue'
  import Song from './components/Song.vue'
  import { searchMusic } from './api/api'
  export default{
    components:{
      PageHeader,
      SearchResults,
      Song,
    },
    data(){

      return {
        music :[],
      }
    },
    methods:{
      getsearch(){
        searchMusic(this.$route.query.musicName).then(
          (res)=>{
            console.log(res)
            for(let i = 0; i < 6; i = i + 1){
              this.music.push(res.data.music[i]);
            }
          }
        )
      },
      playMusic(index){
         
         this.$router.push({name:'Play',query:{userName:this.$route.userName,id: this.music[index].id, cover: this.music[index].pic_url, playUrl: this.music[index].url}});
       },
    },
    mounted:function(){
      this.getsearch();
    },
    watch:{
      $route:function(){
        this.getsearch();
      }
    }
  }

</script>
  
<template>
  <div>
    <div v-for="(song,index) in music" :key="index">
      <SearchResults>
        
          <template #song1>
            <div v-if="index==0"  @click="playMusic(0)">
              <Song>
                <template #cover>
                  <img :src="song.pic_url" class ="cover"/>
                </template>
                <template #title>
                  {{song.name}}
                  <p>{{song.artists[0]}}</p>
                </template>
              </Song>
          </div>
          </template>

          <template #song2>
            <div v-if="index==1 "  @click="playMusic(1)">
              <Song>
                <template #cover>
                  <img :src="song.pic_url" class ="cover"/>
                </template>
                <template #title>
                  {{song.name}}
                  <p>{{song.artists[0]}}</p>
                </template>
              </Song>
          </div>
          </template>

          <template #song3>
            <div v-if="index==2"  @click="playMusic(2)">
              <Song>
                <template #cover>
                  <img :src="song.pic_url" class ="cover"/>
                </template>
                <template #title>
                  {{song.name}}
                  <p>{{song.artists[0]}}</p>
                </template>
              </Song>
          </div>
          </template>

          <template #song4>
            <div v-if="index==3"  @click="playMusic(3)">
              <Song>
                <template #cover>
                  <img :src="song.pic_url" class ="cover"/>
                </template>
                <template #title>
                  {{song.name}}
                  <p>{{song.artists[0]}}</p>
                </template>
              </Song>
          </div>
          </template>

          <template #song5>
            <div v-if="index==4"  @click="playMusic(4)">
              <Song>
                <template #cover>
                  <img :src="song.pic_url" class ="cover"/>
                </template>
                <template #title>
                  {{song.name}}
                  <p>{{song.artists[0]}}</p>
                </template>
              </Song>
          </div>
          </template>

          <template #song6>
            <div v-if="index==5"  @click="playMusic(5)">
              <Song>
                <template #cover>
                  <img :src="song.pic_url" class ="cover"/>
                </template>
                <template #title>
                  {{song.name}}
                  <p>{{song.artists[0]}}</p>
                </template>
              </Song>
          </div>
          </template>
      </SearchResults>
      </div>
  </div>
</template>
  

<style scoped>
@media (min-width: 1024px) {

}
.cover{
  width: 160px;
  height: 160px;
}
</style>
