import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Search from './views/Search.vue'
import store from './store'

Vue.use(Router)

export const router= new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Search
    },
    {
      path: '/search',
      name: 'search',
      component: Search,
    },
    {
      path: '/login',
      name: 'login',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/Login.vue')
    },
    {
      path: '/Secure',
      name: 'secure',
      component: () => import( './views/Secure.vue'),
           meta: { 
                requiresAuth: true
            }
    },
  ]
})

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/login'];
  const loggedIn = store.getters.res;
  console.log(process.env)
  if (to.meta.requiresAuth && !loggedIn) {
      return next('/login');
  }

  next();
})