# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flasgger import Swagger 
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///../instance/database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

swagger = Swagger(app)

from . import models
from .routers import api_bp

app.register_blueprint(api_bp, url_prefix='/api')

app.config['SWAGGER'] = {
    'title': 'Library API',
    'uiversion': 3
}
