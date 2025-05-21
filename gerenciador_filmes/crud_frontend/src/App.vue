<template>
  <div id="app">
    <h1>🎬 Gerenciador de Filmes</h1>
    <nav>
      <router-link to="/create">Criar Filme</router-link> |
      <router-link to="/list">Listar Filmes</router-link> |
      <router-link to="/update">Atualizar Filme</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body {
  font-family: Arial, sans-serif;
  padding: 20px;
}
nav a {
  margin: 0 10px;
}
</style>
