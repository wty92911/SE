// appfront/src/api/api.js
import axiosInstance from './index'

const axios = axiosInstance

export const search = (name) => {return axios.post('http://localhost:8000/demo/',{'musicname' : name})}
//export const getbooks = () => {return 0}
//export const addbook  = () => {return 0}