


import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///jedi_academy.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "a-strong-force-secret")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-force-secret")
    JWT_ACCESS_TOKEN_EXPIRES = False 