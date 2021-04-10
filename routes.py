from flask import current_app as app, render_template, request

@app.route('/')
def inicio():
    return render_template('filha.html')

# @app.route('/')
# def inicio():
#     return render_template('cad.html')
# @app.route('/cadastro', methods=['POST'])
# def cadastro():
#     nome_da_pessoa = request.form['nome']
#     senha_da_pessoa = request.form['senha']
    
#     if nome_da_pessoa == 'morganaribeiro':
#         if senha == '123456':
#             return 'Login com sucesso'
#         else:
#             return 'Errou a senha'
#     else:
#         return 'Usuário inexistente'