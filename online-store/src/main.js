//global file

//global vue
import Vue from 'vue';
//global css
import './styles/common.scss';
//global font style
import './styles/fonts/iconfont.css';
//global router
import router from './router';
//global state control
import store from './store/store';
//global resource interceptor
import './axios/';
import Axios from 'axios';
import App from './App';

Vue.prototype.$http = Axios


//create a global instance
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: {App}
})

