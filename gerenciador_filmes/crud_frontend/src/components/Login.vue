<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="email" placeholder="Email" />
      <input v-model="senha" placeholder="Senha" type="password" />
      <button type="submit">Entrar</button>
    </form>
    <p v-if="erro">{{ erro }}</p>
    <p>
      Não tem conta?
      <button @click="irParaCadastro">Cadastre-se</button>
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      senha: '',
      erro: ''
    }
  },
  methods: {
    login() {
      this.$http.post('http://localhost:5000/login', {
        email: this.email,
        senha: this.senha
      }).then(res => {
        localStorage.setItem('token', res.body.access_token);
        this.$router.push('/list');
      }).catch(err => {
        this.erro = err.body.erro || 'Erro no login';
      });
    },
    irParaCadastro() {
      this.$router.push('/register');
    }
  }
}
</script>
