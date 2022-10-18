<script setup>

</script>
<template>
    <div>
        <div class="cover">
            <slot name="cover"></slot>
        </div>
        <div class="songTitle">
            <slot name="title"></slot>
        </div>
        
    </div>
</template>
<style scoped>
.cover{
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.songTitle{
    padding-top: 205px;
    width: 160px;
    height: 49px;
    color: rgba(16, 16, 16, 1);
    font-size: 28px;
    text-align: left;
    font-family: SourceHanSansSC-regular;
    position: absolute;
}
@media (min-width: 1024px) {
}
</style>