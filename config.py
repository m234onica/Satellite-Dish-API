import os

BUCKET_NAME = 'satellite-l5yx88bg3'

CATEGORY_DB = ['music', 'visual_art', 'market', 'theater']
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
PER_PAGE = 5
class Config:
  SECRET_KEY = os.urandom(24)
  FLASK_APP = os.environ.get('FLASK_APP')
  FLASK_ENV = os.environ.get('FLASK_ENV')
  
  DEBUG = True
  TEMPLATES_AUTO_RELOAD = True
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rootroot@localhost/testDB'
  SQLALCHEMY_TRACK_MODIFICATIONS = True
  JSON_AS_ASCII = False

