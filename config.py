import os

class Config:
  # SECRET_KEY = os.environ.get('SECRET_KEY')
  SECRET_KEY = os.environ.get('SECRET_KEY')
  FLASK_APP = os.environ.get('FLASK_APP')
  FLASK_ENV = os.environ.get('FLASK_ENV')
  FLASK_DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rootroot@localhost/testDB'

  SQLALCHEMY_TRACK_MODIFICATIONS = True
