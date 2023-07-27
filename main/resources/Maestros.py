from flask_restful import Resource
from flask import jsonify,request
from .. import db
from main.models import MaestroModel

class Maestros(Resource):
    def get(self):

        maestros = db.session.query(MaestroModel).all()
        return jsonify(
            {
                "maestros": [maestro.to_json() for maestro in maestros]
            }
        )

    def post(self):
        maestro = MaestroModel.from_json(request.get_json())
        db.session.add(maestro)
        db.session.commit()

        return maestro.to_json(), 201
    
#-----------------------------search only 1, editar, o borrar
class Maestro(Resource):
    def get(self,id):
        maestro = db.session.query(MaestroModel).get_or_404(id)
        try:
            return maestro.to_json()
        except:
            return 'resource not found', 404

    def put(self,id):
        maestro = db.session.query(MaestroModel).get_or_404(id)
        data = request.get_json().items()

        for key, value, in data:
            setattr(maestro,key,value)

        try:
            db.session.add(maestro)
            db.session.commit()
            return maestro.to_json(), 201
        except:
            return '', 404
        
    def delete(self, id):
        maestro = db.session.query(MaestroModel).get_or_404(id)
        try:
            db.session.delete(maestro)
            db.session.commit()
        except:
            return '', 404
        