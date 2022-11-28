<script>
import Animation from './components/Animation.vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { getLyric } from './api/api';
export default{
    components:{
    Animation,
    FontAwesomeIcon,
    Lyric
},
    data(){
        return{
            musicId: '',
            cover: '',
            playUrl: '',
            likeshow:true,
            starshow:true,
            lyricshow:false,
            currentMusicLyric:[],


            musicLyric: '[00:00.000] 作词 : 张军磊\
                [00:01.000] 作曲 : 李亚洲\
                [00:02.000] 编曲 : 李博\
                [00:03.000] 制作人 : 李亚洲\
                [00:29.98]风越过高高的山岗',
            lyric: {}, // 歌词枚举对象(需要在js拿到歌词写代码处理后, 按照格式保存到这个对象)
            curLyric: '', // 当前显示哪句歌词
            lastLy: '' ,// 记录当前播放歌词
            playState: false, // 音乐播放状态(true暂停, false播放)
        }


    },
    async created(){
  //  // 获取歌曲详情, 和歌词方法
  //     const res = await getSongByIdAPI({id:this.id})
  //     this.songInfo = res.data.data[0];

  //     // 获取歌曲详情
  //     const musicInfo =await getMusicByIdAPI({ids:this.id});
  //     this.musicInfo = musicInfo.data.songs[0];

  //     // 获取-并调用formatLyric方法, 处理歌词
  //     const lyrContent  = await getLyricByIdAPI({id:this.id});
  //     const lyricStr = lyrContent.data.lrc.lyric
      this.lyric = this.formatLyric(this.musicLyric)
       // 初始化完毕先显示零秒歌词
      this.curLyric = this.lyric[0]

  },
    methods:{
        changelike(){
            this.likeshow = !this.likeshow;
        },
        changestar(){
            this.starshow = !this.starshow;
        },

        getlyric(){
            getLyric(this.$route.query.id).then(
            (res) =>{
                console.log(res);
                this.musicLyric = res.data.lyric.musicLyric;
            })
            //this.hot.push({'id': '865632948', 'name': '若把你', 'artists': ['Kirsty刘瑾睿'], 'url': 'http://music.163.com/song/media/outer/url?id=865632948.mp3', 'pic_url': 'http://p2.music.126.net/M877M2-VhWZiLPVFORf9iQ==/109951163401482434.jpg'});
        },

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
          this.currentMusicLyric.push(contentArr[index])
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

      // 播放按钮 - 点击事件
      audioStart() {
        if (!this.playState) { // 如果状态为false
          this.$refs.audio.play() // 调用audio标签的内置方法play可以继续播放声音
        } else {
          this.$refs.audio.pause() // 暂停audio的播放
        }
        this.playState = !this.playState // 点击设置对立状态
      },
      lyricShow() {
        this.lyricshow = true;
      },
      lyricHide() {
        this.lyricshow = false;
      }
    },
    mounted:function(){


        this.musicId = this.$route.query.id;
        this.cover = this.$route.query.cover;
        this.playUrl = this.$route.query.playUrl;
        console.log(this.playUrl);
        console.log(this.$route.query.id);
        this.getlyric();
    }
}
</script>


<template>
  <div>
    <div>


        <!--TODO:change the background to an opaque picture><!-->
    </div>
    <div class="leftWave">
        <Animation />
    </div>
    <div class="rightWave">
        <Animation />
    </div>
    <img class="cover" :src="cover" />
    <div class="lyric">

    </div>
    <div class="circleButtonLike" @click="changelike">
        <font-awesome-icon icon = "far fa-heart" v-if="likeshow"/>
        <font-awesome-icon icon = "fas fa-heart" v-if="!likeshow"/>
    </div>
    <div class="circleButtonStar" @click="changestar">
        <font-awesome-icon icon = "far fa-star" v-if="starshow"/>
        <font-awesome-icon icon = "fas fa-star" v-if="!starshow"/>
    </div>
    <div class="circleButtonDownload">
        <font-awesome-icon icon="fa-solid fa-cloud-arrow-down" />
    </div>
    <div class="circleButtonShare">
        <font-awesome-icon icon="fa-solid fa-share" />
    </div>
    <div class="player">
        <div @click="lyricShow()">
          <p class="lrc" >{{ curLyric }}</p>
        </div>
        <audio ref = "audio" preload = "true" :src="playUrl" @timeupdate = "timeupdate" controls="controls"></audio>
    </div>
    <div class="alllyric" v-if="lyricshow">
      <font-awesome-icon @click="lyricHide()" class="closelyric" icon="fa-solid fa-circle-xmark" />
      <div>
        <ul>
            <li v-for="value in currentMusicLyric">
                {{value}}
            </li>
        </ul>
        <!-- {{currentMusicLyric}} -->
        <!-- {{musicLyric}} -->
      </div>
    </div>
  </div>
</template>

<style scoped>

<style scoped>
.logo{
    z-index: 100;
    left: 100px;
    top: 30px;
    width: 150px;
    height: 150px;
    background-color: rgba(255, 255, 255, 0);
    position: fixed;
}
.title{
    z-index: 100;
    left: 250px;
    top: 90px;
    width: 180px;
    height: 50px;
    color: rgba(64, 149, 229, 1);
    font-size: 36px;
    text-align: left;
    font-family: 方正综艺体-标准;
    position: fixed;
}
.background{
    z-index: 100;
    left: 0px;
    top: 0px;
    width: 100%;
    height: 203px;
    background-color: rgb(255, 255, 255);
    position: fixed;
}
.shade{
    z-index: 100;
    left: 0px;
    top: 201px;
    width: 100%;
    height: 19px;
    position: fixed;
}
.leftWave{
    position: absolute;
    top: 212px;
}
.rightWave{
    position: absolute;
    top: 212px;
    margin-left: auto;
    transform: scale(-1,1);
    right: 0;
}
.cover{
    z-index: 101;
    left: 326px;
    top: 226px;
    width: 330px;
    height: 330px;
    position: absolute;
}
.lyric{
    z-index: 101;
    left: 763px;
    top: 226px;
    width: 408px;
    height: 460px;
    line-height: 20px;
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: absolute;
}
.LikeIcon{
    z-index: 101;
    top: 13px;
    left: -1px;
    width: 36px;
    height: 36px;
    position: relative;
}
.StarIcon{
    z-index: 101;
    top: 12px;
    width: 36px;
    height: 36px;
    position: relative;
}
.DownloadIcon{
    z-index: 101;
    top: 12px;
    top: 12px;
    width: 36px;
    height: 36px;
    position: relative;
}
.ShareIcon{
    z-index: 101;
    top: 13px;
    left: -1px;
    width: 36px;
    height: 36px;
    position: relative;
}
.circleButtonLike{
    z-index: 101;
    left: 345px;
    top: 612px;
    width: 60px;
    height: 60px;
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: absolute;
    border-radius: 50%;
    font-size: 45px;
}
.circleButtonStar{
    z-index: 101;
    left: 418px;
    top: 612px;
    width: 60px;
    height: 60px;
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: absolute;
    border-radius: 50%;
    font-size: 43px;
}
.circleButtonDownload{
    z-index: 101;
    left: 491px;
    top: 612px;
    width: 60px;
    height: 60px;
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: absolute;
    border-radius: 50%;
    font-size: 40px;
}
.circleButtonShare{
    z-index: 101;
    left: 564px;
    top: 612px;
    width: 60px;
    height: 60px;
    text-align: center;
    border: 1px solid rgba(187, 187, 187, 1);
    position: absolute;
    border-radius: 50%;
    font-size: 40px;
}
.player{
    z-index:101;
    left: 564px;
    top: 700px;
    width: 300px;
    height: 60px;
    text-align: center;
    position: absolute;

}
.lrc {
  font-size: 20px;
  color: rgb(114, 217, 23);
  text-align: center;
  font-family: 方正综艺体-标准;
}
.alllyric{
    z-index: 101;
    left: 760px;
    top: 226px;
    width: 408px;
    height: 460px;
    line-height: 20px;
    text-align: center;
    text-indent: 0rem;
    color: rgba(106, 26, 219, 0.992);
    border: 1px solid rgba(187, 187, 187, 1);
    position: absolute;
    background-color: rgba(240, 248, 255, 0.507);
    font-family: 方正综艺体-标准;
}
.closelyric{
    z-index: 101;
    top: 0px;
    right: 0px;
    width: 36px;
    height: 36px;
    position: absolute;
}
</style>

