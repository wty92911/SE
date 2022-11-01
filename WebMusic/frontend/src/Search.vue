<script setup>
  import HelloWorld from './components/HelloWorld.vue'
  import PageHeader from './components/PageHeader.vue'
  import SearchResults from './components/SearchResults.vue'
  import Song from './components/Song.vue'
</script>
  
<template>
  <div>
    <PageHeader />
      <SearchResults>
        <template #song1>
          <Song>
            <template #cover>
              <img src="./assets/Search/歌曲封面.png" />
            </template>
            <template #title>
              歌曲名1
            </template>
          </Song>
        </template>
        <template #song2>
          <Song>
            <template #cover>
              <img src="./assets/Search/歌曲封面.png" />
            </template>
            <template #title>
              歌曲名2
            </template>
          </Song>
        </template>
        <template #song3>
          <Song>
            <template #cover>
              <img src="./assets/Search/歌曲封面.png" />
            </template>
            <template #title>
              歌曲名3
            </template>
          </Song>
        </template>
        <template #song4>
          <Song>
            <template #cover>
              <img src="./assets/Search/歌曲封面.png" />
            </template>
            <template #title>
              歌曲名4
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
        </template>
      </SearchResults>
    </div>
</template>
  

<style scoped>
@media (min-width: 1024px) {

}
</style>
