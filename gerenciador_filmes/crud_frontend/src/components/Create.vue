<template>
  <div>
    <h2>Adicionar Filme</h2>
    <form @submit.prevent="criarFilme">
      <input v-model="titulo" placeholder="Título" />
      <input v-model="diretor" placeholder="Diretor" />
      <input v-model="ano" placeholder="Ano" type="number" />
      <button type="submit">Salvar</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      titulo: '',
      diretor: '',
      ano: ''
    }
  },
  methods: {
    criarFilme() {
      const token = localStorage.getItem('token');
      this.$http.post('http://localhost:5000/filmes', {
        titulo: this.titulo,
        diretor: this.diretor,
        ano: this.ano
      }, {
        headers: { Authorization: `Bearer ${token}` }
      }).then(() => {
        this.$router.push('/list');
      });
    }
  }
}
</script>
