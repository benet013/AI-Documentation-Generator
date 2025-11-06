import axios from 'axios';

const isDevelopment = import.meta.env.MODE === 'development';

const api = axios.create({
    baseURL: isDevelopment? import.meta.env.VITE_API_URL_DEVELOPMENT : import.meta.env.VITE_API_URL_DEPLOYMENT,
})

export default api;