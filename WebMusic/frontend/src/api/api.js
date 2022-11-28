// appfront/src/api/api.js
import axiosInstance from './index'

const axios = axiosInstance

//export const search = (name) => {return axios.post('http://47.94.92.103:80/demo/',{'musicname' : name})};
export const searchMusic = (name) => {return axios.post('getMusic',{'musicname':name})};
export const getHotlist = () => {return axios.post('getHotlist')};
export const mySignIn = (username,password) =>{return axios.post('mySignIn',{'username':username,'password':password})};
export const mySignUp = (username,password) =>{return axios.post('mySignUp',{'username':username,'password':password})};
export const getLyric = (id) => {return axios.post('getLyric', {'id':id})};
// // axios发送ajax请求网络请求
// import axios from "axios";

// // axios.create()创建一个axios对象
// const request = axios.create({
//     //基础路径，发请求的时候，路径当中会出现api，不用你手写
// 	baseURL:'http://localhost:3000',
// 	//请求时间超过5秒
// 	timeout:5000
// });

// //获取音乐播放地址
// export const getSongByIdAPI = (params)=>request({url:"/song/url/v1",params});

// //获取歌词
// export const getLyricByIdAPI = (params)=>request({url:'/lyric',params});

// //获取歌曲详情
// export const getMusicByIdAPI = (params)=>request({url:'/song/detail',params});
