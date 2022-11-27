<script>
import {mySignIn,mySignUp} from './api/api.js'
export default{
  props:{
    showSignIn:{
      type:Boolean,
      default:true,
    },
    userName:{
      type:String,
    }
  },
  data(){
    return{
      usr : '',
      pwd : '',
      msg : '',
    }
  },
  methods:{
    close(){
      this.$parent.showSignIn = !this.$parent.showSignIn;
    },
    signIn(){
      mySignIn(this.usr,this.pwd).then(
        (res)=>{
          this.msg = res.data.message;
          console.log(res.data);
          if(res.data.auth == true){
            this.$parent.userName = res.data.username;
          }else{
            this.$parent.userName = '登录';
          }
          alert(this.msg);
          this.usr = '';
          this.pwd = '';
          this.close();
        }
      )
    },
    signUp(){
      mySignUp(this.usr,this.pwd).then(
        (res)=>{
          this.msg = res.data.message;
          console.log(res.data);
          if(res.data.auth == true){
            this.$parent.userName = res.data.username;
          }else{
            this.$parent.userName = '登录';
          }
          alert(this.msg)
          this.usr = '';
          this.pwd = '';
          this.close();
        }
      )
    }
  }
}
</script>
<template>
  <!-- 整体背景 -->
  <div class="login-wrap" v-if="showSignIn">
    <!--输入框-->
    <div class="form-wrapper">
      <div class="header">
        WebMusic
      </div>
      <div class="input-wrapper">
        <div class="border-wrapper">
          <input v-model="usr" type="text" name="username" placeholder="username" class="border-item" autocomplete="off" />
        </div>
        <div class="border-wrapper">
          <input v-model="pwd" type="password" name="password" placeholder="password" class="border-item" autocomplete="off" />
        </div>
      </div>
      <div class="action">
        <div class="btn" @click="signIn()">Sign In</div>
        <div class="btn" @click="signUp()">Sign Up</div>
      </div>
    </div>
  </div>
</template>
 
<style scoped>
.login-wrap {
  z-index: 102;
  height: 100%;
  font-family: JetBrains Mono Medium;
  display: flex;
  align-items: center;
  justify-content: center;
  /* background-color: #0e92b3; */
  background-color: rgba(0, 10, 14, 0.58);
  background-size: 100% 100%;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
 
.form-wrapper {
  width: 300px;
  background-color: rgba(41, 45, 62, 0.8);
  color: #fff;
  border-radius: 10px;
  padding: 50px;
}

.form-wrapper .header {
  color :rgb(127, 223, 255);
  text-align: center;
  font-size: 35px;
  line-height: 100px;
}
 
.form-wrapper .input-wrapper input {
  background-color: rgb(41, 45, 62);
  border: 0;
  width: 100%;
  text-align: center;
  font-size: 15px;
  color: #fff;
  outline: none;
}
 
.form-wrapper .input-wrapper input::placeholder {
  text-transform: uppercase;
}
 
.form-wrapper .input-wrapper .border-wrapper {
  background-image: linear-gradient(to right, #e7d6df, #0eb4dd);
  width: 100%;
  height: 50px;
  margin-bottom: 20px;
  border-radius: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
}
 
.form-wrapper .input-wrapper .border-wrapper .border-item {
  height: calc(100% - 4px);
  width: calc(100% - 4px);
  border-radius: 30px;
}
 
.form-wrapper .action {
  display: flex;
  justify-content: center;
}
 
.form-wrapper .action .btn {
  width: 60%;
  text-transform: uppercase;
  border: 2px solid #0e92b3;
  text-align: center;
  line-height: 50px;
  border-radius: 30px;
  cursor: pointer;
}
 
.form-wrapper .action .btn:hover {
  background-image: linear-gradient(120deg, #797e7b 0%, #8fd3f4 100%);
}
 
.form-wrapper .icon-wrapper {
  text-align: center;
  width: 60%;
  margin: 0 auto;
  margin-top: 20px;
  border-top: 1px dashed rgb(146, 146, 146);
  padding: 20px;
}
 
.form-wrapper .icon-wrapper i {
  font-size: 20px;
  color: rgb(187, 187, 187);
  cursor: pointer;
  border: 1px solid #fff;
  padding: 5px;
  border-radius: 20px;
}
 
.form-wrapper .icon-wrapper i:hover {
  background-color: #0e92b3;
}
</style>