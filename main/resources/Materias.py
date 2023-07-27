from flask_restful import Resource
from flask import jsonify,request
from .. import db
from main.models import MateriaModel

class Materias(Resource):
    def get(self):
        materias = db.session.query(MateriaModel).all()
        return jsonify(
            {
                "materias": [materia.to_json() for materia in materias]
            }
        )
        
    def post(self):
        materia = MateriaModel.from_json(request.get_json())
        db.session.add(materia)
        db.session.commit()

        return materia.to_json(), 201
    
#-----------------------------search only 1, editar, o borrar----------------------
class Materia(Resource):
    def get(self,id):
        materia = db.session.query(MateriaModel).get_or_404(id)
        try:
            return materia.to_json()
        except:
            return 'Resource not found', 404
        
    def put(self,id):
        materia = db.session.query(MateriaModel).get_or_404(id)
        data = request.get_json().items()
        for key,value,in data:
            setattr(materia,key,value)
        
        try:
            db.session.add(materia)
            db.session.commit()
            return materia.to_json(), 201
        except:
            return '', 404
        
    def delete(self,id):
        materia = db.session.query(MateriaModel).get_or_404(id)
        try:
            db.session.delete(materia)
            db.session.commit()
        except:
            return '', 404
        
        
