from .. import db

class Materia(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(10),nullable=False)

    def __repr__(self):
        return f'{self.nombre}'
    
    def to_json(self):
        materia_json = {
            'id':self.id,
            'nombre': self.nombre
        }
        return materia_json
    
    @staticmethod
    def from_json(materia_json):
        id = materia_json.get('id')
        nombre = materia_json.get('nombre')

        return Materia(
            id = id,
            nombre=nombre
        )