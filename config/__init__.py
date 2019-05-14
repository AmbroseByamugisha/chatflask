from config.config_1 import app_config
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config_1.py')
    app.config['JWT_SECRET_KEY'] = 'Fuck the world'
    jwt = JWTManager(app)
    CORS(app)
    return app

