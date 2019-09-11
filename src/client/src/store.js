import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    jwt:''
  },
  mutations: {
    updateJWT(state, payload) {
      state.jwt = payload
    }
  },
  actions: {
    updateJWT(state, payload) {
      state.jwt = payload
    }
  },
  getters: {
    header: state => {
      return `JWT ${state.jwt.access_token}` 
    },
    token: state => {

      return state? state.jwt.access_token :null
    },
    res: state => {

      return state.jwt
    }
    //store.getters.jwt to get the jwt 
  }
})
