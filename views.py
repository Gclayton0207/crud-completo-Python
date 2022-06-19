from flask import render_template, request, redirect, session, flash, url_for, Flask
from app import app, db
from models import usuarios


@app.route('/')
def index():
    listaDeUsuarios = usuarios.query.order_by(usuarios.id)
    return render_template('lista.html', titulo='Usuarios', usuarios=listaDeUsuarios)


@app.route('/novo', methods=['POST', ])
def novo():
    return render_template('novo.html', titulo='Adicionar novo Usuario')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    usuario = usuarios.query.filter_by(nome=nome).first()

    if usuario:
        flash('Usuario já existente!')
        return redirect(url_for('index'))

    novo_usuario = usuarios(nome=nome, email=email, telefone=telefone)
    db.session.add(novo_usuario)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):

    usuario = usuarios.query.filter_by(id=id).first()
    return render_template('editar.html', titulo='Editando Usuario', usuario=usuario)


@app.route('/atualizar', methods=['POST', ])
def atualizar():
    usuario = usuarios.query.filter_by(id=request.form['id']).first()
    usuario.nome = request.form['nome']
    usuario.email = request.form['email']
    usuario.telefone = request.form['telefone']

    db.session.add(usuario)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):

    usuarios.query.filter_by(id=id).delete()
    db.session.commit()
    flash('O usuario foi deletado com sucesso')
    return redirect(url_for('index'))
