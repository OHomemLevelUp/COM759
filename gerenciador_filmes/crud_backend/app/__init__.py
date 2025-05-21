from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from .routes import configure_routes
import config

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config')
    app.mongo = MongoClient(app.config['MONGO_URI'])
    configure_routes(app)
    return app