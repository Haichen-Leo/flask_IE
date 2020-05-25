from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/forheart?charset=utf8"
    app.config["SQLALCHEMY_POOL_SIZE"] = 5
    app.config["SQLALCHEMY_POOL_TIMEOUT"] = 5
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app
