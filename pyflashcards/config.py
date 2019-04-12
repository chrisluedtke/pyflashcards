from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = getenv('FLASK_ENV')
