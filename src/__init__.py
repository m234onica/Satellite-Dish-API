from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from src.route.cms import cms
from src.route.api import api


def create_app():
  app = Flask(__name__)
  app.config.from_object('config')

  app.register_blueprint(cms)
  app.register_blueprint(api)
  db.init_app(app)

  return app
