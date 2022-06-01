from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Neto', idade=50)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    #pessoa = Pessoas.query.filter_by(nome='Neto').first()
    #print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Tricca').first()
    pessoa.nome = 'TTN'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Neto').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_usuario('Neto', '1234')
    #insere_usuario('Netinho', '4321')
    consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    consulta_pessoas()