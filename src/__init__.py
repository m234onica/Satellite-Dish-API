from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config

db = SQLAlchemy()

from src.route.cms import cms
from src.route.api import api


def create_app(config_name):
  app = Flask(__name__)
  app.url_map.strict_slashes = False
  app.config.from_object(app_config[config_name])

  app.register_blueprint(cms)
  app.register_blueprint(api)
  db.init_app(app)

  return app
