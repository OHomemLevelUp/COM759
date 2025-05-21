import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueResource from 'vue-resource'

Vue.config.productionTip = false

Vue.use(VueResource) // permite usar this.$http para fazer requisições HTTP

new Vue({
  router,       // importa as rotas definidas em src/router/index.js
  render: h => h(App),  // renderiza o componente App.vue
}).$mount('#app')
