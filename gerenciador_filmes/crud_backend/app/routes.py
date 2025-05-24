from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from . import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


main = Blueprint('main', __name__)

@main.route('/filmes', methods=['GET'])
def listar_filmes():
    filmes = mongo.db.filmes.find()
    lista = []
    for filme in filmes:
        filme['_id'] = str(filme['_id'])
        lista.append(filme)
    return jsonify(lista)

@main.route('/filmes', methods=['POST'])
@jwt_required()
def criar_filme():
    data = request.get_json()
    mongo.db.filmes.insert_one(data)
    return jsonify({'msg': 'Filme criado com sucesso'}), 201

@main.route('/filmes/<id>', methods=['PUT'])
@jwt_required()
def atualizar_filme(id):
    data = request.get_json()
    mongo.db.filmes.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify({'msg': 'Filme atualizado com sucesso'})

@main.route('/filmes/<id>', methods=['DELETE'])
@jwt_required()
def deletar_filme(id):
    mongo.db.filmes.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': 'Filme deletado com sucesso'})


@main.route('/register', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')

    if not nome or not email or not senha:
        return jsonify({'erro': 'Preencha nome, email e senha'}), 400

    if mongo.db.usuarios.find_one({'email': email}):
        return jsonify({'erro': 'Email já cadastrado'}), 409

    senha_hash = generate_password_hash(senha)

    usuario = {
        'nome': nome,
        'email': email,
        'senha': senha_hash
    }

    mongo.db.usuarios.insert_one(usuario)
    return jsonify({'msg': 'Usuário registrado com sucesso'}), 201

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    if not email or not senha:
        return jsonify({'erro': 'Preencha email e senha'}), 400

    usuario = mongo.db.usuarios.find_one({'email': email})
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

    if not check_password_hash(usuario['senha'], senha):
        return jsonify({'erro': 'Senha incorreta'}), 401

    access_token = create_access_token(identity=email)

    return jsonify({
        'msg': 'Login realizado com sucesso',
        'access_token': access_token
    }), 200

