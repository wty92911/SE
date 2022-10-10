<script setup>
  import HelloWorld from './components/HelloWorld.vue'
  import PageHeader from './components/PageHeader.vue'
  import Recommendations from './components/Recommendations.vue'
  import Song from './components/Song.vue'
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
              <img src="./assets/HomePage/歌曲封面.png" />
            </template>
            <template #title>
              歌曲名1
            </template>
          </Song>
        </template>
        <template #song2>
          <Song>
            <template #cover>
              <img src="./assets/HomePage/歌曲封面.png" />
            </template>
            <template #title>
              歌曲名2
            </template>
          </Song>
        </template>
        <template #song3>
          <Song>
            <template #cover>
              <img src="./assets/HomePage/歌曲封面.png" />
            </template>
            <template #title>
              歌曲名3
            </template>
          </Song>
        </template>
        <template #song4>
          <Song>
            <template #cover>
              <img src="./assets/HomePage/歌曲封面.png" />
            </template>
            <template #title>
              歌曲名4
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
              <img src="./assets/HomePage/歌曲封面.png" />
            </template>
            <template #title>
              歌曲名1
            </template>
          </Song>
        </template>
        <template #song2>
          <Song>
            <template #cover>
              <img src="./assets/HomePage/歌曲封面.png" />
            </template>
            <template #title>
              歌曲名2
            </template>
          </Song>
        </template>
        <template #song3>
          <Song>
            <template #cover>
              <img src="./assets/HomePage/歌曲封面.png" />
            </template>
            <template #title>
              歌曲名3
            </template>
          </Song>
        </template>
        <template #song4>
          <Song>
            <template #cover>
              <img src="./assets/HomePage/歌曲封面.png" />
            </template>
            <template #title>
              歌曲名4
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

@media (min-width: 1024px) {
}
</style>
  