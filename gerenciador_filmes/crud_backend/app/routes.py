from flask import request, jsonify, render_template, redirect, url_for
from bson.objectid import ObjectId

def configure_routes(app):
    db = app.mongo['cinema']
    filmes = db['filmes']
    usuarios = db['usuarios']

    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            data = request.form
            usuario = usuarios.find_one({"username": data.get("username"), "password": data.get("password")})
            if usuario:
                return redirect(url_for('listar_filmes'))
            else:
                return render_template('login.html', erro="Usuário ou senha incorretos.")
        return render_template('login.html')

    @app.route('/filmes')
    def listar_filmes():
        todos_filmes = list(filmes.find())
        for filme in todos_filmes:
            filme["_id"] = str(filme["_id"])
        return render_template('listar_filmes.html', filmes=todos_filmes)

    @app.route('/filmes/create', methods=['GET', 'POST'])
    def create_filme():
        if request.method == 'POST':
            data = {
                "titulo": request.form.get("titulo"),
                "diretor": request.form.get("diretor"),
                "ano": request.form.get("ano"),
                "genero": request.form.get("genero")
            }
            filmes.insert_one(data)
            return redirect(url_for('listar_filmes'))
        return render_template('create_filme.html')

    @app.route('/filmes/update/<id>', methods=['GET', 'POST'])
    def update_filme(id):
        filme = filmes.find_one({"_id": ObjectId(id)})
        if not filme:
            return "Filme não encontrado", 404
        if request.method == 'POST':
            update_data = {
                "titulo": request.form.get("titulo"),
                "diretor": request.form.get("diretor"),
                "ano": request.form.get("ano"),
                "genero": request.form.get("genero")
            }
            filmes.update_one({"_id": ObjectId(id)}, {"$set": update_data})
            return redirect(url_for('listar_filmes'))
        filme["_id"] = str(filme["_id"])
        return render_template('update_filme.html', filme=filme)

    @app.route('/filmes/delete/<id>')
    def delete_filme(id):
        filmes.delete_one({"_id": ObjectId(id)})
        return redirect(url_for('listar_filmes'))
