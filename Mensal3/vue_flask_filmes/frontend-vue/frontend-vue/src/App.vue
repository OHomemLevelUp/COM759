<template>
  <div id="app">
    <LoginPage v-if="!autenticado" @logado="autenticado = true" />
    <FilmesView v-else />
  </div>
</template>

<script>
import LoginPage from './components/LoginPage.vue'
import FilmesView from './components/FilmesView.vue'

export default {
  components: { LoginPage, FilmesView },
  data() {
    return {
      autenticado: false
    }
  }
}
</script>
