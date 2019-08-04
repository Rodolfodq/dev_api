from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']
class Habil(Resource):
    def get(self):
        return lista_habilidades
