<template>
  <div class="container">
    <h2>Adicionar Filme</h2>

    <form @submit.prevent="criarFilme">
      <input v-model="titulo" placeholder="Título" />
      <input v-model="diretor" placeholder="Diretor" />
      <input v-model="genero" placeholder="Gênero" />
      
      <div style="display: flex; gap: 10px; justify-content: center;">
        <input v-model="duracaoHoras" type="number" min="0" placeholder="Horas" style="width: 45%;" />
        <input v-model="duracaoMinutos" type="number" min="0" max="59" placeholder="Minutos" style="width: 45%;" />
      </div>
      
      <input v-model="ano" type="number" placeholder="Ano" />
      <input v-model="avaliacao" type="number" min="1" max="10" placeholder="Avaliação (1 a 10)" />
      <button type="submit">Salvar</button>
    </form>

    <button class="link" @click="voltar">Voltar para Lista</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      titulo: '',
      diretor: '',
      genero: '',
      duracaoHoras: '',
      duracaoMinutos: '',
      ano: '',
      avaliacao: ''
    }
  },
  methods: {
    criarFilme() {
      const token = localStorage.getItem('token');
      const duracaoFinal = `${this.duracaoHoras}h ${this.duracaoMinutos}min`;

      this.$http.post('http://localhost:5000/filmes', {
        titulo: this.titulo,
        diretor: this.diretor,
        genero: this.genero,
        duracao: duracaoFinal,
        ano: this.ano,
        avaliacao: this.avaliacao
      }, {
        headers: { Authorization: `Bearer ${token}` }
      }).then(() => {
        this.$router.push('/list');
      });
    },
    voltar() {
      this.$router.push('/list');
    }
  }
}
</script>
