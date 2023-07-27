from flask_restful import Resource
from flask import jsonify,request
from .. import db
from main.models import SalonModel

class Salones(Resource):
    def get(self):
        salones = db.session.query(SalonModel).all()
        return jsonify(
            {
                "salones": [salon.to_json() for salon in salones]
            }
        )
    
    def post(self):
        salon = SalonModel.from_json(request.get_json())
        db.session.add(salon)
        db.session.commit()

        return salon.to_json(), 201
    
#-----------------------------search only 1, editar, o borrar
class Salon(Resource):
    def get(self,id):
        salon = db.session.query(SalonModel).get_or_404(id)
        try:
            return salon.to_json()
        except:
            return 'Resource not found', 404
        
    def put(self,id):
        salon = db.session.query(SalonModel).get_or_404(id)
        data = request.get_json().items()

        for key,value, in data:
            setattr(salon,key,value)
        
        try:
            db.session.add(salon)
            db.session.commit()
            return salon.to_json(), 201
        except:
            return '' , 404
        
    
    def delete(self,id):
        salon = db.session.query(SalonModel).get_or_404(id)
        try:
            db.session.delete(salon)
            db.session.commit()
        except:
            return '', 404