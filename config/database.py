from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from config.server import server_environment

from constants.environment import Environment


class GlobalDBHelper:

    BASE = None
    ENGINE = None
    SESSION = None

    def __init__(self):
        if server_environment == Environment.LOCAL:
            self.__setup_local_database()

        if server_environment == Environment.PRODUCTION:
            self.__setup_production_database()

    def __setup_local_database(self):
        self.ENGINE = create_engine('sqlite:///:memory:', echo=True)
        self.BASE = declarative_base()
        self.SESSION = Session(bind=self.ENGINE)

    def __setup_production_database(self):
        pass


LOCAL_MODEL_SETTINGS = GlobalDBHelper()
