// appfront/src/api/api.js
import axiosInstance from './index'

const axios = axiosInstance

//export const search = (name) => {return axios.post('http://47.94.92.103:80/demo/',{'musicname' : name})};
export const searchMusic = (name) => {return axios.post('getMusic',{'musicname':name})};
export const getHotlist = () => {return axios.post('getHotlist')};
export const mySignIn = (username,password) =>{return axios.post('mySignIn',{'username':username,'password':password})};
export const mySignUp = (username,password) =>{return axios.post('mySignUp',{'username':username,'password':password})};
export const getLyric = (id) => {return axios.post('getLyric', {'id':id})};
export const myLikes = (username,opt,id) => {return axios.post('myLikes',{'username':username,'opt':opt,'id':id})};
export const getComment = (id) => {return axios.post('getComment',{"id":id})}
