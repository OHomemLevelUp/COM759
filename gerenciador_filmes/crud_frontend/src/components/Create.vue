<template>
  <div>
    <h2>Adicionar Filme</h2>
    <form @submit.prevent="criarFilme">
      <label>Título:</label><br/>
      <input v-model="titulo" placeholder="Ex: Interstellar" /><br/>

      <label>Diretor:</label><br/>
      <input v-model="diretor" placeholder="Ex: Christopher Nolan" /><br/>

      <label>Ano:</label><br/>
      <input v-model="ano" type="number" placeholder="Ex: 2014" /><br/>

      <label>Gênero:</label><br/>
      <input v-model="genero" placeholder="Ex: Ficção Científica" /><br/><br/>

      <button type="submit">Criar Filme</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      titulo: '',
      diretor: '',
      ano: '',
      genero: ''
    };
  },
  methods: {
    criarFilme() {
      this.$http.post('http://localhost:5000/create', {
        titulo: this.titulo,
        diretor: this.diretor,
        ano: this.ano,
        genero: this.genero
      }).then(response => {
        alert(response.body.mensagem);
        this.titulo = '';
        this.diretor = '';
        this.ano = '';
        this.genero = '';
      }).catch(error => {
        alert("Erro ao criar filme.");
        console.log(error);
      });
    }
  }
}
</script>

<style scoped>
input {
  margin-bottom: 10px;
  width: 300px;
  padding: 5px;
}
button {
  padding: 8px 15px;
}
</style>
