<script>
import { dataType } from 'element-plus/es/components/table-v2/src/common';
import LikesHotsVue from './components/LikesHots.vue';
import PageHeaderVue from './components/PageHeader.vue';
export default{
  components:{
    LikesHotsVue,
    PageHeaderVue,
  },
  data(){
    return{
      userName:'123',
    }
  },
  methods:{

  },
}
</script>
  
<template>
  <PageHeaderVue></PageHeaderVue>
  <router-view></router-view>
  
 
</template>
  
<style scoped>  
</style>
  
