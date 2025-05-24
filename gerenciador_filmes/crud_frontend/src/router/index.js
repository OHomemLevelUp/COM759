import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login.vue'
import Register from '@/components/Register.vue'
import List from '@/components/List.vue'
import Create from '@/components/Create.vue'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/', redirect: '/register' },
    { path: '/login', component: Login },
    { path: '/register', component: Register },
    { path: '/list', component: List },
    { path: '/create', component: Create }
  ]
})
