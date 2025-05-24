<template>
  <div>
    <h2>Lista de Filmes</h2>
    <ul>
      <li v-for="filme in filmes" :key="filme._id">
        {{ filme.titulo }} - {{ filme.diretor }} ({{ filme.ano }})
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      filmes: []
    }
  },
  created() {
    const token = localStorage.getItem('token');
    this.$http.get('http://localhost:5000/filmes', {
      headers: { Authorization: `Bearer ${token}` }
    }).then(res => {
      this.filmes = res.body;
    });
  }
}
</script>
