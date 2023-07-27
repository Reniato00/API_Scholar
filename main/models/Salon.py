from .. import db

class Salon(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(10),nullable=False)

    def __repr__(self):
        return f'{self.nombre}'
    
    def to_json(self):
        salon_json = {
            'id': self.id,
            'nombre':self.nombre
        }
        return salon_json
    
    @staticmethod
    def from_json(salon_json):
        id =salon_json.get('id')
        nombre = salon_json.get('nombre')
        return Salon(
            id = id,
            nombre = nombre
        )
