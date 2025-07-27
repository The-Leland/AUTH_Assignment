


from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from db import db
from util.blueprints import register_blueprints
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    db.init_app(app)
    JWTManager(app)
    CORS(app)

    register_blueprints(app)

    with app.app_context():
        db.create_all()

    return app
