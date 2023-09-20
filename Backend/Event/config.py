import os
from dotenv import load_dotenv


load_dotenv(".env")


class App_Config:
    # SECRET_KEY = os.environ.get("SECRET_KEY")
    SECRET_KEY = 'SKJJSJSJSJJSJS'



    # basedir = os.path.abspath(os.path.dirname(__file__))

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = "postgresql://shabzy:1111@localhost:5432/hng"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
