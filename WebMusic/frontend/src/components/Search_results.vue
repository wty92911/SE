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
    padding-left: 200px;
    padding-top: 300px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.song2{
    padding-left: 600px;
    padding-top: 300px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.song3{
    padding-left: 1000px;
    padding-top: 300px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.song4{
    padding-left: 200px;
    padding-top: 600px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.song5{
    padding-left: 600px;
    padding-top: 600px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.song6{
    padding-left: 1000px;
    padding-top: 600px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.pg_cover1{
    padding-left: 600px;
    padding-top: 800px;
    width: 350px;
    height: 45px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}

</style>
