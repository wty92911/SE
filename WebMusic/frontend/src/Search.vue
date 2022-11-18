<script >
  import HelloWorld from './components/HelloWorld.vue'
  import PageHeader from './components/PageHeader.vue'
  import SearchResults from './components/SearchResults.vue'
  import Song from './components/Song.vue'
  import { searchMusic } from './api/api'
  import ShowSix from './ShowSix.vue'
  
  export default{
    components:{
      PageHeader,
      SearchResults,
      Song,
      ShowSix,
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
            for(let i = 0; i < res.data.music.length; i = i + 1){
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
  
  <ShowSix :music="music"></ShowSix>
</template>
  

<style scoped>
@media (min-width: 1024px) {

}
.cover{
  width: 160px;
  height: 160px;
}
</style>
