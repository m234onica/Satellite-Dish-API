import os
import os

BUCKET_NAME = 'satellite-l5yx88bg3'

CATEGORY_DB = ['music', 'visual_art', 'market', 'theatre']
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
PER_PAGE = 10
class Config(object):
  DEBUG = True

  SECRET_KEY = ''
  FLASK_APP = os.environ.get('FLASK_APP')
  FLASK_ENV = os.environ.get('FLASK_ENV')

  JSON_AS_ASCII = False
  TEMPLATES_AUTO_RELOAD = True
  SQLALCHEMY_TRACK_MODIFICATIONS = True

class GoogleConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql: // {username}: {passwword}@/{db_name}?unix_socket=/cloudsql/{instance_connection_name}'
  BASE_URL = 'https://asia-northeast1-momoka-244303.cloudfunctions.net/satellitedish'


class NgrokConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{username}:{passwword}@{host}/{db_name}'
  BASE_URL = "https://ngrok.momoka.tw/joyce"


class LocalConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{username}:{passwword}@{host}/{db_name}'
  BASE_URL = ""


app_config = {
    'google_function': GoogleConfig,
    'ngrok': NgrokConfig,
    'local': LocalConfig
}


