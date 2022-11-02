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
            this.artist1 = res.data.music[0].artists;
            this.artist2 = res.data.music[1].artists;
            this.artist3 = res.data.music[2].artists;
            this.artist4 = res.data.music[3].artists;
            this.artist5 = res.data.music[4].artists;
            this.artist6 = res.data.music[5].artists;
          }
        )
      }
    },
    mounted:function(){
      this.getsearch();
    }
  }

</script>
  
<template>
  <div>
    <PageHeader />
      <SearchResults>
        <template #song1>
          <Song>
            <template #cover>
              <img :src="img1" class ="cover"/>
            </template>
            <template #title>
              {{name1 , artist1}}
            </template>
          </Song>
        </template>
        <template #song2>
          <Song>
            <template #cover>
              <img :src="img2" class ="cover"/>
            </template>
            <template #title>
              {{name2 , artist2}}
            </template>
          </Song>
        </template>
        <template #song3>
          <Song>
            <template #cover>
              <img :src="img3" class ="cover"/>
            </template>
            <template #title>
              {{name3 , artist3}}
            </template>
          </Song>
        </template>
        <template #song4>
          <Song>
            <template #cover>
              <img :src="img4" class ="cover"/>
            </template>
            <template #title>
              {{name4 , artist4}}
            </template>
          </Song>
        </template>
        <template #song5>
          <Song>
            <template #cover>
              <img :src="img5" class ="cover"/>
            </template>
            <template #title>
              {{name5 , artist5}}
            </template>
          </Song>
        </template>
        <template #song6>
          <Song>
            <template #cover>
              <img :src="img6" class ="cover"/>
            </template>
            <template #title>
              {{name6 , artist6}}
            </template>
          </Song>
        </template>
        <template #pg_cover1>
        </template>
      </SearchResults>
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
