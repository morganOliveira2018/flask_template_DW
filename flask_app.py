from flask import Flask

app = Flask(__name__)

@app.route('/about')
def home():
    return "Olá, pessoal!"

@app.route('/digaOi/<variavel>')
def diaOi(variavel):
    return f'Oi, {variavel}!'

# soma com números inteiros
@app.route('/soma/int/<int:a>/<int:b>')
def somaInt(a, b):
    return str(a+b)

# soma com números quebrados
@app.route('/soma/float/<int:a>/<int:b>')
def somaFloat(a, b):
    return str(a+b)

@app.route('/path/<path:caminho>')
def pather(caminho):
    return caminho