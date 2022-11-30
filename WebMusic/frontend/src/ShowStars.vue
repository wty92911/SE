<script>
import ShowSix from './ShowSix.vue';
export default{
    components:{
        ShowSix,
    },
    data(){
        return{
            music:[],
        }
    },
    mounted:function(){
        console.log(this.$route.query.music);
        this.music = JSON.parse(this.$route.query.music);
    }
}
</script>

<template>
  <ShowSix :music="music" :userName="this.$route.query.userName"></ShowSix>
</template>