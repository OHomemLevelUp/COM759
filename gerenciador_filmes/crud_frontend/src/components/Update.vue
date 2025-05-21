<template>
  <div>
    <h2>Atualizar Filme</h2>
    <form @submit.prevent="atualizarFilme">
      <label>ID do Filme:</label><br/>
      <input v-model="id" placeholder="Cole aqui o ID do filme" /><br/>

      <label>Novo Título:</label><br/>
      <input v-model="titulo" placeholder="Novo título" /><br/>

      <label>Novo Diretor:</label><br/>
      <input v-model="diretor" placeholder="Novo diretor" /><br/>

      <label>Novo Ano:</label><br/>
      <input v-model="ano" type="number" placeholder="Novo ano" /><br/>

      <label>Novo Gênero:</label><br/>
      <input v-model="genero" placeholder="Novo gênero" /><br/><br/>

      <button type="submit">Atualizar</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      id: '',
      titulo: '',
      diretor: '',
      ano: '',
      genero: ''
    };
  },
  methods: {
    atualizarFilme() {
      this.$http.post('http://localhost:5000/update', {
        id: this.id,
        titulo: this.titulo,
        diretor: this.diretor,
        ano: this.ano,
        genero: this.genero
      }).then(response => {
        alert(response.body.mensagem);
        this.id = '';
        this.titulo = '';
        this.diretor = '';
        this.ano = '';
        this.genero = '';
      }).catch(error => {
        alert("Erro ao atualizar filme.");
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
