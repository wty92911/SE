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
        img1 : "./assets/Search/歌曲封面.png",
        img2 : "./assets/Search/歌曲封面.png",
        img3 : "./assets/Search/歌曲封面.png",
        img4 : "./assets/Search/歌曲封面.png",
        img5 : "./assets/Search/歌曲封面.png",
        img6 : "./assets/Search/歌曲封面.png",
        name1 : '',
        name2 : '',
        name3 : '',
        name4 : '',
        name5 : '',
        name6 : '',
        artist1 : '',
        artist2 : '',
        artist3 : '',
        artist4 : '',
        artist5 : '',
        artist6 : '',
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
            this.img1 = res.data.music[0].pic_url;
            this.img2 = res.data.music[1].pic_url;
            this.img3 = res.data.music[2].pic_url;
            this.img4 = res.data.music[3].pic_url;
            this.img5 = res.data.music[4].pic_url;
            this.img6 = res.data.music[5].pic_url;
            this.name1 = res.data.music[0].name;
            this.name2 = res.data.music[1].name;
            this.name3 = res.data.music[2].name;
            this.name4 = res.data.music[3].name;
            this.name5 = res.data.music[4].name;
            this.name6 = res.data.music[5].name;
            this.artist1 = res.data.music[0].artists[0];
            this.artist2 = res.data.music[1].artists[0];
            this.artist3 = res.data.music[2].artists[0];
            this.artist4 = res.data.music[3].artists[0];
            this.artist5 = res.data.music[4].artists[0];
            this.artist6 = res.data.music[5].artists[0];
          }
        )
      },
      playMusic(index){

         this.$router.push({name:'Play',query:{id: this.music[index].id, cover: this.music[index].pic_url, playUrl: this.music[index].url}});
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
