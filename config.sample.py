import os

BUCKET_NAME = 'satellite-l5yx88bg3'

CATEGORY_DB = ['music', 'visual_art', 'market', 'theatre']
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
PER_PAGE = 10

SECRET_KEY = ''
FLASK_APP = os.environ.get('FLASK_APP')
FLASK_ENV = os.environ.get('FLASK_ENV')

DEBUG = True
TEMPLATES_AUTO_RELOAD = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rootroot@localhost/SatelliteDish?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = True
JSON_AS_ASCII = False

BASE_URL = ''
if BASE_URL.endswith(os.path.sep):
  BASE_URL = BASE_URL[:-1]
