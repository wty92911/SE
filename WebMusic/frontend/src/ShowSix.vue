<script >
  import HelloWorld from './components/HelloWorld.vue'
  import PageHeader from './components/PageHeader.vue'
  import SearchResults from './components/SearchResults.vue'
  import Song from './components/Song.vue'
  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
  export default{
    components:{
      PageHeader,
      SearchResults,
      Song,
      FontAwesomeIcon,
    },
    props:{
        music:Object,
    },
    data(){

      return {
        pageNumber:0,
      }
    },
    methods:{
    
        playMusic(index){
            this.$router.push({name:'Play',query:{userName:this.$route.userName,id: this.music[index].id, cover: this.music[index].pic_url, playUrl: this.music[index].url}});
        },
        nextPage(){
            console.log(this.music.length);
           if(this.pageNumber * 6 + 6 < this.music.length){
            this.pageNumber += 1;
            console.log(this.pageNumber);
           }
           
           
        },
        lastPage(){
            if(this.pageNumber > 0){
                this.pageNumber -= 1;
            }
            console.log(this.pageNumber);
        },
    },
    mounted:function(){
       
    },
  }

</script>
  
<template>

    <font-awesome-icon @click="nextPage()" class="righticon" icon="fa-solid fa-circle-chevron-right" />
    <font-awesome-icon @click="lastPage()" class="lefticon" icon="fa-solid fa-circle-chevron-left" />
    <div>
    <div v-for="(song,index) in music" :key="index">
      <SearchResults>
        
          <template #song1>
            <div v-if="index==pageNumber + 0"  @click="playMusic(pageNumber + 0)">
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
            <div v-if="index==pageNumber + 1 "  @click="playMusic(pageNumber + 1)">
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
            <div v-if="index==pageNumber + 2"  @click="playMusic(pageNumber + 2)">
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
            <div v-if="index==pageNumber + 3"  @click="playMusic(pageNumber + 3)">
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
            <div v-if="index==pageNumber + 4"  @click="playMusic(pageNumber + 4)">
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
            <div v-if="index==pageNumber + 5"  @click="playMusic(pageNumber + 5)">
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
.righticon{
    z-index: 101;
    left: 1350px;
    top: 530px;
    width: 60px;
    height: 60px;
    line-height: 20px;
    text-align: center;
    position: absolute;
    font-size: 40px;
}
.lefticon{
    z-index: 101;
    left: 150px;
    top: 530px;
    width: 60px;
    height: 60px;
    line-height: 20px;
    text-align: center;
    position: absolute;
    font-size: 40px;
}
</style>
