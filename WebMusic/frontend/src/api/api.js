// appfront/src/api/api.js
import axiosInstance from './index'

const axios = axiosInstance

//export const search = (name) => {return axios.post('http://47.94.92.103:80/demo/',{'musicname' : name})};
export const searchMusic = (name) => {return axios.post('getMusic',{'musicname':name})};
export const getHotlist = () => {return axios.post('getHotlist')};