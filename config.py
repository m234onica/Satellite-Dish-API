import os

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY')
  FLASK_APP = os.environ.get('FLASK_APP')
  FLASK_ENV = os.environ.get('FLASK_ENV')
  FLASK_DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rootroot@localhost/testDB'
  JSON_AS_ASCII = False
  SQLALCHEMY_TRACK_MODIFICATIONS = True

db_category = ['music', 'visual_art', 'market', 'theater']
