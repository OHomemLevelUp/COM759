<template>
  <div>
    <h2>Lista de Filmes</h2>
    <ul v-if="filmes.length > 0">
      <li v-for="filme in filmes" :key="filme._id.$oid">
        <strong>{{ filme.titulo }}</strong> ({{ filme.ano }})<br/>
        Diretor: {{ filme.diretor }}<br/>
        Gênero: {{ filme.genero }}<br/><br/>
      </li>
    </ul>
    <p v-else>Nenhum filme encontrado.</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      filmes: []
    };
  },
  mounted() {
    this.$http.get('http://localhost:5000/')
      .then(response => {
        this.filmes = response.body;
      })
      .catch(error => {
        console.log("Erro ao buscar filmes:", error);
      });
  }
}
</script>

<style scoped>
li {
  border-bottom: 1px solid #ccc;
  margin-bottom: 10px;
  padding-bottom: 10px;
}
</style>
