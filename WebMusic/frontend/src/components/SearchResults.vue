<script setup>

</script>
<template>        
        <div class="song1">
            <slot name="song1"></slot>
        </div>
        <div class="song2">
            <slot name="song2"></slot>
        </div>
        <div class="song3">
            <slot name="song3"></slot>
        </div>
        <div class="song4">
            <slot name="song4"></slot>
        </div>
        <div class="song5">
            <slot name="song5"></slot>
        </div>
        <div class="song6">
            <slot name="song6"></slot>
        </div>
        <div class="pg_cover1">
        </div>
</template>
<style scoped>
.song1{
    z-index: 101;
    left: 300px;
    top: 300px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.song2{
    z-index: 101;
    left: 700px;
    top: 300px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.song3{
    z-index: 101;
    left: 1100px;
    top: 300px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.song4{
    z-index: 101;
    left: 300px;
    top: 600px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.song5{
    z-index: 101;
    left: 700px;
    top: 600px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.song6{
    z-index: 101;
    left: 1100px;
    top: 600px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.pg_cover1{
    left: 600px;
    top: 800px;
    width: 350px;
    height: 45px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}

</style>
