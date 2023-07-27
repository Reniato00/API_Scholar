from .. import db

class Maestro(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(45),nullable = False)
    email = db.Column(db.String(60), nullable = False, unique= True, index = True)
    materia = db.Column(db.String(45), nullable = False)

    def __repr__(self):
        return f'{self.nombre}'
    
    def to_json(self):
        maestro_json= {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'materia': self.materia
        }
        return maestro_json
    
    @staticmethod
    def from_json(maestro_json):
        id = maestro_json.get('id')
        nombre = maestro_json.get('nombre')
        email = maestro_json.get('email')
        materia = maestro_json.get('materia')
        return Maestro(
            id=id,
            nombre = nombre,
            email = email,
            materia=materia
        )