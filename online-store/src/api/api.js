import axios from 'axios';


//let host = 'http://shop.projectsedu.com';
let host = '127.0.0.1:8000';

//product category information
export const queryCategorygoods = params => {
  return axios.get(`${host}/indexgoods/`)
}

//new goods
export const newGoods = params => {
  return axios.get(`${host}/newgoods/`)
}

//banner images
export const bannerGoods = params => {
  return axios.get(`${host}/banners/`)
}

//categories
export const getCategory = params => {
  if ('id' in params) {
    return axios.get(`${host}/categorys/` + params.id + '/');
  } else {
    return axios.get(`${host}/categorys/`, params);
  }
};


//hot search words
export const getHotSearch = params => {
  return axios.get(`${host}/hotsearchs/`)
}

//goods list
export const getGoods = params => {
  return axios.get(`${host}/goods/`, {params: params})
}

//goods detail
export const getGoodsDetail = goodId => {
  return axios.get(`${host}/goods/${goodId}` + '/')
}

//goods from shopping cart
export const getShopCarts = params => {
  return axios.get(`${host}/shopcarts/`)
}
//add to shopping cart
export const addShopCart = params => {
  return axios.post(`${host}/shopcarts/`, params)
}
//update shopping cart
export const updateShopCart = (goodsId, params) => {
  return axios.patch(`${host}/shopcarts/` + goodsId + '/', params)
}
//delete shopping cart
export const deleteShopCart = goodsId => {
  return axios.delete(`${host}/shopcarts/` + goodsId + '/')
}

//add to favorite
export const addFav = params => {
  return axios.post(`${host}/userfavs/`, params)
}

//remove favorite
export const delFav = goodsId => {
  return axios.delete(`${host}/userfavs/` + goodsId + '/')
}

//get all favorites
export const getAllFavs = () => {
  return axios.get(`${host}/userfavs/`)
}

//get if good in favorite
export const getFav = goodsId => {
  return axios.get(`${host}/userfavs/` + goodsId + '/')
}

//login
export const login = params => {
  return axios.post(`${host}/login/`, params)
}

//register
export const register = parmas => {
  return axios.post(`${host}/users/`, parmas)
}

//message
export const getMessage = parmas => {
  return axios.post(`${host}/code/`, parmas)
}


//get user detail
export const getUserDetail = () => {
  return axios.get(`${host}/users/1/`)
}

//update user detail
export const updateUserInfo = params => {
  return axios.patch(`${host}/users/1/`, params)
}


//get orders
export const getOrders = () => {
  return axios.get(`${host}/orders/`)
}
//delete order
export const delOrder = orderId => {
  return axios.delete(`${host}/orders/` + orderId + '/')
}
//create order
export const createOrder = params => {
  return axios.post(`${host}/orders/`, params)
}
//get order detail
export const getOrderDetail = orderId => {
  return axios.get(`${host}/orders/` + orderId + '/')
}


//get messages
export const getMessages = () => {
  return axios.get(`${host}/messages/`)
}

//add messages
export const addMessage = params => {
  return axios.post(`${host}/messages/`, params, {headers: {'Content-Type': 'multipart/form-data'}})
}

//delete messages
export const delMessages = messageId => {
  return axios.delete(`${host}/messages/` + messageId + '/')
}

//add new address
export const addAddress = params => {
  return axios.post(`${host}/address/`, params)
}

//delete address
export const delAddress = addressId => {
  return axios.delete(`${host}/address/` + addressId + '/')
}

//update address
export const updateAddress = (addressId, params) => {
  return axios.patch(`${host}/address/` + addressId + '/', params)
}

//get all addresses
export const getAddress = () => {
  return axios.get(`${host}/address/`)
}
