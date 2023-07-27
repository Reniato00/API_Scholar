from .. import db


class Alumno(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(45),nullable=False)
    email = db.Column(db.String(60),nullable=False, unique= True, index = True)

    def __repr__(self):
        return f'{self.nombre}'
    
    def to_json(self):
        alumno_json = {
            'id':self.id,
            'nombre': self.nombre,
            'email': self.email
        }
        return alumno_json
    
    @staticmethod
    def from_json(alumno_json):
        id = alumno_json.get('id')
        nombre = alumno_json.get('nombre')
        email = alumno_json.get('email')

        return Alumno(
            id = id,
            nombre=nombre,
            email=email
        )