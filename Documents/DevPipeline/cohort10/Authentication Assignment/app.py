


from flask import Flask
from db import db
from routes import user_routes, company_routes, product_routes  # etc.
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt = Bcrypt(app)

app.register_blueprint(user_routes.bp)

if __name__ == '__main__':
    app.run(debug=True)
