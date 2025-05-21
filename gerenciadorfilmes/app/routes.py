from flask import request, jsonify
from bson import json_util
from bson.objectid import ObjectId
from app import app, db
import json

@app.route('/')
def index():
    filmes = db.filmes.find().sort("_id", 1)
    return jsonify(json.loads(json_util.dumps(filmes)))

@app.route('/create', methods=['POST'])
def create():
    json_data = request.json
    if json_data:
        db.filmes.insert_one(json_data)
        return jsonify(mensagem='filme criado')
    return jsonify(mensagem='erro ao criar filme')

@app.route('/getid/<string:filme_id>')
def getid(filme_id):
    filme = db.filmes.find_one({"_id": ObjectId(filme_id)})
    return jsonify(json.loads(json_util.dumps(filme)))

@app.route('/delete/<string:filme_id>')
def delete(filme_id):
    result = db.filmes.delete_one({"_id": ObjectId(filme_id)})
    if result.deleted_count > 0:
        return jsonify(mensagem='filme removido')
    return jsonify(mensagem='filme não encontrado')

@app.route('/update', methods=['POST'])
def update():
    json_data = request.json
    if json_data and db.filmes.find_one({"_id": ObjectId(json_data["id"])}):
        db.filmes.update_one({'_id': ObjectId(json_data["id"])}, {"$set": {
            'titulo': json_data["titulo"],
            'diretor': json_data["diretor"],
            'ano': json_data["ano"],
            'genero': json_data["genero"]
        }})
        return jsonify(mensagem='filme atualizado')
    return jsonify(mensagem='erro ao atualizar filme')
