<template>
  <div>
    <h2>Cadastro</h2>
    <form @submit.prevent="register">
      <input v-model="nome" placeholder="Nome" />
      <input v-model="email" placeholder="Email" />
      <input v-model="senha" placeholder="Senha" type="password" />
      <button type="submit">Cadastrar</button>
    </form>
    <p v-if="erro">{{ erro }}</p>
    <p>
      Já tem conta?
      <button @click="irParaLogin">Faça login</button>
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      nome: '',
      email: '',
      senha: '',
      erro: ''
    }
  },
  methods: {
    register() {
      this.$http.post('http://localhost:5000/register', {
        nome: this.nome,
        email: this.email,
        senha: this.senha
      }).then(() => {
        this.$router.push('/login');
      }).catch(err => {
        this.erro = err.body.erro || 'Erro no cadastro';
      });
    },
    irParaLogin() {
      this.$router.push('/login');
    }
  }
}
</script>
