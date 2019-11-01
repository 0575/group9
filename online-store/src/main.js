//global file

//PayPal
import PayPal from 'vue-paypal-checkout';

//global vue
import Vue from 'vue';

//Bootstrap
//import BootstrapVue from 'bootstrap-vue';
//Vue.use(BootstrapVue)

//global css
//import './styles/bootstrap/css/bootstrap.min.css';
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
  data() {
    return {
      paypal: {
        sandbox: 'AbFxEbttlDglxstD3uKGJOHjOY27bQjtP8dIg72NdlFqQfAGUN0h6j4UAq8SCC2eFHjnlfCgbin9lmhI',
        production: 'AbFxEbttlDglxstD3uKGJOHjOY27bQjtP8dIg72NdlFqQfAGUN0h6j4UAq8SCC2eFHjnlfCgbin9lmhI'
      }
    }
  },
  components: {App,PayPal},
})


