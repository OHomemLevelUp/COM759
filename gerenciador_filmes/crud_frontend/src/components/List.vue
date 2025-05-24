<template>
  <div class="container">
    <h2>Lista de Filmes</h2>

    <div class="botoes-acoes">
      <button @click="irParaCriar">Adicionar Filme</button>
      <button @click="logout" class="link">Sair</button>
    </div>

    <template v-if="filmes.length > 0">
      <div class="tabela-filmes">
        <table>
          <thead>
            <tr>
              <th>Título</th>
              <th>Diretor</th>
              <th>Gênero</th>
              <th>Duração</th>
              <th>Ano</th>
              <th>Avaliação</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="filme in filmes" :key="filme._id">
              <td>{{ filme.titulo }}</td>
              <td>{{ filme.diretor }}</td>
              <td>{{ filme.genero }}</td>
              <td>{{ filme.duracao }}</td>
              <td>{{ filme.ano }}</td>
              <td>{{ filme.avaliacao }}/10</td>
            </tr>
          </tbody>
        </table>
      </div>
    </template>

    <p v-else>Nenhum filme encontrado.</p>
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
  },
  methods: {
    irParaCriar() {
      this.$router.push('/create');
    },
    logout() {
      localStorage.removeItem('token');
      this.$router.push('/login');
    }
  }
}
</script>
