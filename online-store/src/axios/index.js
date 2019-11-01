//using vue
import axios from 'axios';
//global state control
import store from '../store/store';

// http request interceptor
axios.interceptors.request.use(
  config => {
    if (store.state.userInfo.token) {
      config.headers.Authorization = `JWT ${store.state.userInfo.token}`;
    }
    return config;
  },
  err => {
    return Promise.reject(err);
  });


// http response interceptor
axios.interceptors.response.use(
  undefined,
  error => {
    let res = error.response;
    console.log(error);
    switch (res.status) {
      case 401:
        console.log('Not logged in or token expired');
      case 403:
        console.log('You do not have permission');
      case 404:
        console.log('This webpage is not found');
      case 500:
        console.log('Server Error');
    }
    return Promise.reject(error.response.data)
  });
