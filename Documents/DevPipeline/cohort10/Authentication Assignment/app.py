


from flask import Flask
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

from db import db, create_tables
from utils.blueprints import register_blueprints

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt = Bcrypt(app)

create_tables(app)            
register_blueprints(app)      

if __name__ == '__main__':
    app.run(debug=True)
