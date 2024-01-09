from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager

import os


import models

from db import db

from resources.mall import blp as MallBlueprint

def create_app(db_url=None):
    app = Flask(__name__)

    #we need app in the JWTManager(app) to create the endpoint

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Navigation_api"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app) #this is the same as db = SQLAlchemy(app)

    api = Api(app) 

    with app.app_context(): #this is needed to create the tables in the database
        db.create_all()

    api.register_blueprint(MallBlueprint)

    return app