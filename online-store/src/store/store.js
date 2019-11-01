import Vue from 'vue'
import Vuex from 'vuex';

import mutations from './mutations';
import * as actions from './actions';
import * as getters from './getters';
import cookie from '../static/js/cookie';

Vue.use(Vuex);

const userInfo = {
  name: cookie.getCookie('name') || '',
  token: cookie.getCookie('token') || ''
};
const goods_list = {
  totalPrice: '',
  goods_list: []

}
const state = {
  userInfo,
  goods_list
}
export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters
});
