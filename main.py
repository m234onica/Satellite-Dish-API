from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db_session = db.session

def create_app():
  app = Flask(__name__)
  app.config.from_object('config.Config')
  db.init_app(app)
  # db.create_all()
  return app
  
