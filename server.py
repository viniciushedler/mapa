from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def barra():
    return render_template('inicio.html')

@app.route('/listar')
def listar():
    return render_template('listar_pessoas.html')

@app.route('/form_inserir_pessoa')
def form_inserir_pessoa():
    return render_template('form_inserir_pessoa.html')

@app.route('/form_alterar_pessoa')
def form_alterar_pessoa():
    return render_template('form_alterar_pessoa.html')

@app.route('/inserir_pessoa')
def inserir_pessoa():
    return render_template('.html')

@app.route('/alterar_pessoa')
def alterar_pessoa():
    return render_template('.html')

@app.route('/excluir_pessoa')
def excluir_pessoa():
    return render_template('.html')


app.run()