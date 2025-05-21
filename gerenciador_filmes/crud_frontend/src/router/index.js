import Vue from 'vue'
import Router from 'vue-router'

// Importaremos os componentes Vue depois que eles forem criados
import Create from '../components/Create.vue'
import List from '../components/List.vue'
import Update from '../components/Update.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/create',
      name: 'Create',
      component: Create
    },
    {
      path: '/list',
      name: 'List',
      component: List
    },
    {
      path: '/update',
      name: 'Update',
      component: Update
    }
  ]
})
