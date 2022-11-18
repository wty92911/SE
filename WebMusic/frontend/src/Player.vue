<script setup lang="ts">
import { ref } from 'vue'
import { useAVBars, useAVCircle } from 'vue-audio-visual/dist/vue-audio-visual'
const player = ref(null)
const canvas = ref(null)
const props = defineProps(['mySource'])
// composable function useAVBars

//useAVBars(player, canvas, { src: props.mySource, canvHeight: 40, canvWidth: 200, barColor: 'lime' })
useAVCircle(player,canvas,{ src:props.mySource})
</script>

<template>
  <div>
    <audio ref="player" crossOrigin="anonymous" :src="props.mySource" controls></audio>
    <canvas ref="canvas" ></canvas>
  </div>
</template>