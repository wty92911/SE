<script setup>
  import HelloWorld from './components/HelloWorld.vue'
  import PageHeader from './components/PageHeader.vue'
  import Recommendations from './components/Recommendations.vue'
  import Song from './components/Song.vue'
  import {ref} from 'vue'
  import {getHotlist} from './api/api.js'
  const hotListData = ref([]);
  const hotpic1 = ref("./assets/HomePage/歌曲封面.png");
  const hotpic2 = ref("./assets/HomePage/歌曲封面.png");
  const hotpic3 = ref("./assets/HomePage/歌曲封面.png");
  const hotpic4 = ref("./assets/HomePage/歌曲封面.png");
  const hotpic5 = ref("./assets/HomePage/歌曲封面.png");
  const hotpic6 = ref("./assets/HomePage/歌曲封面.png");
  const hotpic7 = ref("./assets/HomePage/歌曲封面.png");
  const hotpic8 = ref("./assets/HomePage/歌曲封面.png");
  const hotname1 = ref("");
  const hotname2 = ref("");
  const hotname3 = ref("");
  const hotname4 = ref("");
  const hotname5 = ref("");
  const hotname6 = ref("");
  const hotname7 = ref("");
  const hotname8 = ref("");
  function gethot(){
    getHotlist().then(
      (res) =>{
        console.log(res);
        hotListData.value = res.data;
        hotpic1.value = res.data.music[0].pic_url;
        hotpic2.value = res.data.music[1].pic_url;
        hotpic3.value = res.data.music[2].pic_url;
        hotpic4.value = res.data.music[3].pic_url;
        hotpic5.value = res.data.music[4].pic_url;
        hotpic6.value = res.data.music[5].pic_url;
        hotpic7.value = res.data.music[6].pic_url;
        hotpic8.value = res.data.music[7].pic_url;
        hotname1.value = res.data.music[0].name;
        hotname2.value = res.data.music[1].name;
        hotname3.value = res.data.music[2].name;
        hotname4.value = res.data.music[3].name;
        hotname5.value = res.data.music[4].name;
        hotname6.value = res.data.music[5].name;
        hotname7.value = res.data.music[6].name;
        hotname8.value = res.data.music[7].name;
      }
    )
  }
  gethot();
  
  
</script>
  
<template>
  <div>
    <PageHeader />
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
  