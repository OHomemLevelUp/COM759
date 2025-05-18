# Gerenciador de Filmes - COM759

Projeto desenvolvido como Avaliação Mensal 3 da disciplina **Programação Avançada (COM759)** na FACAMP.

## 🧠 Descrição da Aplicação

Esta aplicação web permite a realização de operações CRUD (Criar, Listar, Atualizar, Deletar) sobre uma coleção de **filmes**, com as seguintes informações:
- Título
- Diretor
- Ano
- Gênero

Além disso, a aplicação implementa **autenticação por login e senha** e uma **interface simples e funcional**, com comunicação entre frontend (Vue.js) e backend (Flask), utilizando o banco de dados NoSQL **MongoDB Atlas**.

---

## 📁 Estrutura do Projeto

```
projeto/
├── backend-flask/
│   ├── app.py
│   └── requirements.txt
└── frontend-vue/
    ├── src/
    │   ├── App.vue
    │   └── components/
    │       ├── Filmes.vue
    │       └── Login.vue
```

---

## 💻 Tecnologias Utilizadas

- Frontend: Vue.js (Vue CLI)
- Backend: Flask + Flask-CORS + PyMongo
- Banco de dados: MongoDB Atlas (NoSQL)
- IDE recomendada: VSCode

---

## 🔧 Como Instalar e Configurar

### 1. Clonar o Repositório

```bash
git clone https://github.com/SEU_USUARIO/seu-repositorio.git
cd projeto
```

### 2. Backend (Flask)

```bash
cd COM759\Mensal3\vue_flask_filmes\backend-flask
python -m venv venv
# Ativação (Windows)
venv\Scripts\activate
# Ativação (Linux/macOS)
source venv/bin/activate

pip install -r requirements.txt
```

#### 🔗 Configurar MongoDB Atlas

1. Crie uma conta gratuita em [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Crie um banco de dados chamado `cinema`
3. Crie as collections: `filmes` e `usuarios`
4. Insira um usuário na collection `usuarios`:
```json
{
  "username": "admin",
  "password": "123"
}
```
5. Copie a **string de conexão URI** do Atlas e substitua no `app.py`:
```python
client = MongoClient("SUA_STRING_DE_CONEXÃO")
```

---

### 3. Frontend (Vue.js)

```bash
cd COM759\Mensal3\vue_flask_filmes\frontend-vue\frontend-vue
npm install
npm run serve
```

---

## ▶️ Como Executar a Aplicação

### 🖥️ Terminal 1 – Iniciar o Backend (Flask)

1. Abra um terminal.
2. Navegue até a pasta do backend:
```bash
cd caminho/para/projeto/backend-flask
```
3. Ative o ambiente virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```
4. Rode o servidor:
```bash
python app.py
```

---

### 🖥️ Terminal 2 – Iniciar o Frontend (Vue.js)

1. Abra **outro terminal**.
2. Navegue até a pasta do frontend:
```bash
cd caminho/para/projeto/frontend-vue
```
3. Rode a aplicação Vue:
```bash
npm run serve
```

---

3. Acesse no navegador: [http://localhost:8080](http://localhost:8080)

---

## 🔐 Como Usar

1. Faça login com:
   - **Usuário**: admin
   - **Senha**: 123
2. Após o login, será exibida a lista de filmes cadastrados.
3. Você poderá:
   - Adicionar um novo filme
   - Excluir um filme
   - (Melhorias futuras: editar filme)

---

## ✅ Requisitos Atendidos

- ✔️ CRUD completo via Web Services
- ✔️ Banco de dados MongoDB Atlas
- ✔️ Comunicação entre Frontend (Vue.js) e Backend (Flask)
- ✔️ Autenticação de acesso (login/senha)
- ✔️ Visual simples com interface clara
- ✔️ README com instruções de uso

---

