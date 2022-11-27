<script>
import { getLyric } from './api/api'


export default{
  data() {
    return {
      lyric: {}, // 歌词枚举对象(需要在js拿到歌词写代码处理后, 按照格式保存到这个对象)
      curLyric: '', // 当前显示哪句歌词
      lastLy: '' ,// 记录当前播放歌词
    }
  },
  async created(){
    // 获取-并调用formatLyric方法, 处理歌词
    // const lyrContent  = await getLyricByIdAPI({id:this.id});
    const lyricStr = getLyric;
    this.lyric = this.formatLyric(lyricStr)
      // 初始化完毕先显示零秒歌词
    this.curLyric = this.lyric[0]
  },

  methods: {
    formatLyric(lyricStr) {
      // 可以看network观察歌词数据是一个大字符串, 进行拆分.
      let reg = /\[.+?\]/g //
      let timeArr = lyricStr.match(reg) // 匹配所有[]字符串以及里面的一切内容, 返回数组
      console.log(timeArr); // ["[00:00.000]", "[00:01.000]", ......]
      let contentArr = lyricStr.split(/\[.+?\]/).slice(1) // 按照[]拆分歌词字符串, 返回一个数组(下标为0位置元素不要,后面的留下所以截取)
      console.log(contentArr);
      let lyricObj = {} // 保存歌词的对象, key是秒, value是显示的歌词
      timeArr.forEach((item, index) => {
        // 拆分[00:00.000]这个格式字符串, 把分钟数字取出, 转换成秒
        let ms = item.split(':')[0].split('')[2] * 60
        // 拆分[00:00.000]这个格式字符串, 把十位的秒拿出来, 如果是0, 去拿下一位数字, 否则直接用2位的值
        let ss = item.split(':')[1].split('.')[0].split('')[0] === '0' ? item.split(':')[1].split('.')[0].split('')[1] : item.split(':')[1].split('.')[0]
        // 秒数作为key, 对应歌词作为value
        lyricObj[ms + Number(ss)] = contentArr[index]
      })
      // 返回得到的歌词对象(可以打印看看)
      console.log(lyricObj);
      return lyricObj
    },

    // 监听播放audio进度, 切换歌词显示
    timeupdate(){
      // console.log(this.$refs.audio.currentTime)
      let curTime = Math.floor(this.$refs.audio.currentTime)
      // 避免空白出现
      if (this.lyric[curTime]) {
        this.curLyric = this.lyric[curTime]
        this.lastLy = this.curLyric
      } else {
        this.curLyric = this.lastLy
      }
    },
  }
}

</script>

<template>
<!-- 歌词部分-随着时间切换展示一句歌词 -->
<div class="lrcContent">
  <p class="lrc">{{ curLyric }}</p>
</div>

<!-- 音乐播放地址 -->
<audio ref="audio" preload="true" :src="songInfo.url" @timeupdate="timeupdate"></audio>
</template>

<style>
/* 歌词显示 */
.scrollLrc {
  position: absolute;
  bottom: 280rpx;
  width: 640rpx;
  height: 120rpx;
  line-height: 120rpx;
  text-align: center;
}
</style>
