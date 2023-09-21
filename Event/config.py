"""
summary
"""
import os
from dotenv import load_dotenv


load_dotenv(".env")

# pylint: disable=invalid-name
class App_Config:
    """_summary_
    """
    # SECRET_KEY = os.environ.get("SECRET_KEY")
    SECRET_KEY = 'dwddwfwdg'


    SQLALCHEMY_DATABASE_URI = "postgresql://shabzy:1111@localhost:5432/hng"


    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI",
    #                                          "sqlite:///test.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    def nothing(self):
        """_summary_
        """

    def another(self):
        """_summary_
        """
