from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

# Inicializa a aplicação Flask
app = Flask(__name__)
CORS(app)  # Permite chamadas externas do Vue.js

# Conecta ao MongoDB Atlas (substitua a string se necessário)
client = MongoClient("mongodb+srv://admin:admin@cluster0.pojhz.mongodb.net/Cluster0?retryWrites=true&w=majority")

# Acesse o banco e coleções
db = client["cinema"]
filmes = db["filmes"]
usuarios = db["usuarios"]

# ROTA: LOGIN
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = usuarios.find_one({
        "username": data["username"],
        "password": data["password"]
    })
    if usuario:
        return jsonify({"status": "ok", "msg": "Login bem-sucedido!"})
    return jsonify({"status": "erro", "msg": "Usuário ou senha incorretos!"}), 401

# ROTA: LISTAR FILMES
@app.route('/filmes', methods=['GET'])
def listar_filmes():
    return jsonify([
        {
            "_id": str(f["_id"]),
            "titulo": f["titulo"],
            "diretor": f["diretor"],
            "ano": f["ano"],
            "genero": f["genero"]
        } for f in filmes.find()
    ])

# ROTA: ADICIONAR FILME
@app.route('/filmes', methods=['POST'])
def adicionar_filme():
    data = request.json
    result = filmes.insert_one(data)
    return jsonify({"_id": str(result.inserted_id)})

# ROTA: ATUALIZAR FILME
@app.route('/filmes/<id>', methods=['PUT'])
def atualizar_filme(id):
    data = request.json
    filmes.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"msg": "Filme atualizado"})

# ROTA: DELETAR FILME
@app.route('/filmes/<id>', methods=['DELETE'])
def deletar_filme(id):
    filmes.delete_one({"_id": ObjectId(id)})
    return jsonify({"msg": "Filme deletado"})

# INICIAR SERVIDOR
if __name__ == '__main__':
    app.run(debug=True)
