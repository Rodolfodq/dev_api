from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habil
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
     'id': '0',
     'nome': 'Rodolfo',
     'habilidades': ['Python', 'Flask']
    },
    {
         'id': '1',
         'nome': 'Queiroz',
         'habilidades': ['Python', 'Djnago']
    }
]

#devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return (response)

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído'}

#lista todos os desenvolvedores e inclui um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habil, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)