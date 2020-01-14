import os

BUCKET_NAME = 'satellite-l5yx88bg3'

CATEGORY_DB = ['music', 'visual_art', 'market', 'theater']
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
PER_PAGE = 10

SECRET_KEY = '4u90qj4o6juponj4q6uqjonj4ti6'
FLASK_APP = os.environ.get('FLASK_APP')
FLASK_ENV = os.environ.get('FLASK_ENV')

DEBUG = True
TEMPLATES_AUTO_RELOAD = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:]fgnoYM,7R/zyxF#WyC8@localhost/SatelliteDish'
SQLALCHEMY_TRACK_MODIFICATIONS = True
JSON_AS_ASCII = False

