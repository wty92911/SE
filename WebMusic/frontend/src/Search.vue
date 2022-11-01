<script setup>
  import HelloWorld from './components/HelloWorld.vue'
  import PageHeader from './components/PageHeader.vue'
  import Recommendations from './components/Recommendations.vue'
  import Song from './components/Song.vue'
  import PG_NUM from './components/PG_NUM.vue'
</script>
  
<template>
  <div>
    <PageHeader />
      <Recommendations>
        <template #song1>
          <Song>
            <template #cover>
              <img src="./assets/Search/歌曲封面.png" />
            </template>
            <template #title>
              {{hotname5}}
            </template>
          </Song>
        </template>
        <template #song2>
          <Song>
            <template #cover>
              <img src="./assets/Search/歌曲封面.png" />
            </template>
            <template #title>
              {{hotname6}}
            </template>
          </Song>
        </template>
        <template #song3>
          <Song>
            <template #cover>
              <img src="./assets/Search/歌曲封面.png" />
            </template>
            <template #title>
              {{hotname7}}
            </template>
          </Song>
        </template>
        <template #song4>
          <Song>
            <template #cover>
              <img src="./assets/Search/歌曲封面.png" />
            </template>
            <template #title>
              {{hotname8}}
            </template>
          </Song>
        </template>
        <template #song5>
          <Song>
            <template #cover>
              <img src="./assets/Search/歌曲封面.png" />
            </template>
            <template #title>
              歌曲名5
            </template>
          </Song>
        </template>
        <template #song6>
          <Song>
            <template #cover>
              <img src="./assets/Search/歌曲封面.png" />
            </template>
            <template #title>
              歌曲名6
            </template>
          </Song>
        </template>
        <template #pg_cover1>
          <PG_NUM>
            <template #pg_cover>
              <img src="./assets/Search/分页图.png" />
            </template>
          </PG_NUM>
        </template>
      </Recommendations>
    </div>
</template>
  

<style scoped>
@media (min-width: 1024px) {

}
</style>
