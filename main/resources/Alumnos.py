from flask_restful import Resource
from flask import jsonify, request
from .. import db
from main.models import AlumnoModel



class Alumnos(Resource):
    def get(self):

        alumnos = db.session.query(AlumnoModel).all()

        return jsonify(
            {
            "alumnos": [alumno.to_json() for alumno in alumnos]
            }
        )
    
    def post(self):
        alumno = AlumnoModel.from_json(request.get_json())
        db.session.add(alumno)
        db.session.commit()

        return alumno.to_json(), 201
    
#-----------------------------search only 1, editar, o borrar
class Alumno(Resource):
    def get(self,id):

        alumno = db.session.query(AlumnoModel).get_or_404(id)
        try:
            return alumno.to_json()
        except:
            return 'Resource not found', 404
        
    def put(self, id):
        alumno = db.session.query(AlumnoModel).get_or_404(id)
        data = request.get_json().items()
        for key, value, in data:
            setattr(alumno, key, value)
        
        try:
            db.session.add(alumno)
            db.session.commit()
            return alumno.to_json(), 201
        except:
            return '', 404
        
    def delete(self,id):
        alumno = db.session.query(AlumnoModel).get_or_404(id)
        try:
            db.session.delete(alumno)
            db.session.commit()
        except:
            return '', 404

    