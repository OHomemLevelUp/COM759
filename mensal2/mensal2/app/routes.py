from flask import render_template, request, jsonify, redirect, url_for
from app import app, db
from bson import ObjectId

# 1) Página inicial: listar as notas em HTML
@app.route('/')
def index():
    notas = list(db.notafiscal.find({}).sort("numero", 1))
    return render_template('listarNotas.html', notas=notas)

# 2) API JSON: listar todas as notas (opcional)
@app.route('/notas')
def listar_notas_json():
    notas = list(db.notafiscal.find({}, {"_id": 0}))
    return jsonify(status="OK", notas=notas)

# 3) Formulário de criação
@app.route('/create')
def create():
    return render_template('create.html')

# 4) Ação de criação
@app.route('/createAction', methods=['POST'])
def createAction():
    data = request.form.to_dict()
    if not data.get('numero'):
        return jsonify(mensagem='Erro: número obrigatório'), 400

    result = db.notafiscal.insert_one(data)
    if result.inserted_id:
        return jsonify(mensagem='Inserido')
    return jsonify(mensagem='Não inserido'), 500

# 5) Formulário de edição
@app.route('/update/<string:numero>')
def update(numero):
    nota = db.notafiscal.find_one({"numero": numero})
    if not nota:
        return jsonify(mensagem='Nota não existe'), 404
    return render_template('update.html', nota=nota)

# 6) Ação de edição
@app.route('/updateAction', methods=['POST'])
def updateAction():
    data = request.form.to_dict()
    original = data.pop('original_numero', None)
    new_numero = data.get('numero')

    if original and new_numero:
        update_fields = {
            'numero':    new_numero,
            'comprador': data.get('comprador'),
            'cnpj':      data.get('cnpj'),
            'endereco':  data.get('endereco'),
            'telefone':  data.get('telefone'),
            'data':      data.get('data'),
            'valor':     data.get('valor'),
            'itens':     data.get('itens')
        }
        res = db.notafiscal.update_one(
            {"numero": original},
            {"$set": update_fields}
        )
        if res.modified_count > 0:
            return jsonify(mensagem='Alterado')
    return jsonify(mensagem='Não alterado')

# 7) Ação de exclusão
@app.route('/delete/<string:numero>')
def delete(numero):
    res = db.notafiscal.delete_one({"numero": numero})
    return redirect(url_for('index'))
