<script setup>

</script>
<template>
    <div>
        <div class="titleContainer">
            <div class="title">
                <slot name="title"></slot>
            </div>
        </div>      
        <div>        
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
        </div>
    </div>   
</template>
<style scoped>
.titleContainer{
    padding-left: 250px;
    padding-right: 250px;
}
.title{
    padding-top: 27px;
    width: 205px;
    height: 55px;
    line-height: 28px;
    border-radius: 30px;
    background-color: rgba(255, 255, 255, 1);
    color: rgba(16, 16, 16, 1);
    font-size: 28px;
    text-align: center;
    font-family: Roboto;
    border: 1px solid rgba(240, 240, 240, 1);
    position: absolute;
}
.song1{
    left: 138px;
    top: 99px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.song2{
    left: 398px;
    top: 99px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.song3{
    left: 138px;
    top: 398px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}
.song4{
    left: 398px;
    top: 398px;
    width: 160px;
    height: 160px;
    line-height: 20px;
    text-align: center;
    position: absolute;
}

</style>