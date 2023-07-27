import os
from flask import Flask
from dotenv import load_dotenv

#Importo el modulo para crear la api-rest
from flask_restful import Api
api = Api()
#Import the module to connect to the bd
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()




def create_app():
    app = Flask(__name__)
    #Cargo las variables de entorno
    load_dotenv()

    #Configuracion de la base de datos:
    PATH = os.getenv("DATABASE_PATH")
    DB_NAME = os.getenv("DATABASE_NAME")
    if not os.path.exists(f'{PATH}/{DB_NAME}'):
        os.chdir(f'{PATH}')
        file = os.open(f'{DB_NAME}', os.O_CREAT)

    #Configuracion predefinidas de la app sobre la db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{PATH}{DB_NAME}'
    db.init_app(app)


    import main.resources as resources
    api.add_resource(resources.AlumnosResource, '/Alumnos')
    api.add_resource(resources.AlumnoResource, '/Alumno/<id>')
    api.add_resource(resources.MaestrosResource, '/Maestros')
    api.add_resource(resources.MaestroResource, '/Maestro/<id>')
    api.add_resource(resources.SalonesResource, '/Salones')
    api.add_resource(resources.SalonResource, '/Salon/<id>')
    api.add_resource(resources.MateriasResource, '/Materias')
    api.add_resource(resources.MateriaResource, '/Materia/<id>')

    api.init_app(app)

    return app



