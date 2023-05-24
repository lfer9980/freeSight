from os import environ
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    CORS(app)

    app.config['SQLALCHEMY_ECHO'] = False

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['TRAP_HTTP_EXCEPTIONS'] = True

    from .public import public_bp
    app.register_blueprint(public_bp)

    db.init_app(app)

    return app
