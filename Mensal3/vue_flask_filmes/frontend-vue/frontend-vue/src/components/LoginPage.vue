<template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="Usuário" required />
      <input v-model="password" type="password" placeholder="Senha" required />
      <button>Entrar</button>
    </form>
    <p v-if="erro" style="color: red">{{ erro }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      username: '',
      password: '',
      erro: ''
    }
  },
  methods: {
    login() {
      axios.post('http://localhost:5000/login', {
        username: this.username,
        password: this.password
      }).then(() => {
        this.$emit('logado')
      }).catch(err => {
        this.erro = err.response.data.msg
      })
    }
  }
}
</script>
