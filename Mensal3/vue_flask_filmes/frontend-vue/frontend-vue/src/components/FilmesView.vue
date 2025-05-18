<template>
  <div>
    <h2>Gerenciador de Filmes</h2>
    <form @submit.prevent="adicionarFilme">
      <input v-model="novo.titulo" placeholder="Título">
      <input v-model="novo.diretor" placeholder="Diretor">
      <input v-model="novo.ano" placeholder="Ano">
      <input v-model="novo.genero" placeholder="Gênero">
      <button>Adicionar</button>
    </form>
    <ul>
      <li v-for="f in filmes" :key="f._id">
        {{ f.titulo }} - {{ f.diretor }} ({{ f.ano }})
        <button @click="deletarFilme(f._id)">Excluir</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      filmes: [],
      novo: { titulo: '', diretor: '', ano: '', genero: '' }
    }
  },
  mounted() {
    this.listarFilmes()
  },
  methods: {
    listarFilmes() {
      axios.get('http://localhost:5000/filmes')
        .then(res => this.filmes = res.data)
    },
    adicionarFilme() {
      axios.post('http://localhost:5000/filmes', this.novo)
        .then(() => {
          this.listarFilmes()
          this.novo = { titulo: '', diretor: '', ano: '', genero: '' }
        })
    },
    deletarFilme(id) {
      axios.delete(`http://localhost:5000/filmes/${id}`)
        .then(this.listarFilmes)
    }
  }
}
</script>
