from sqlalchemy import Column, Integer, Sequence, String, Float

from config.database import LOCAL_MODEL_SETTINGS


class User(LOCAL_MODEL_SETTINGS.BASE):

    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    fullname = Column(String(50))
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    hashed_password = Column(String(255))
    image_url = Column(String(255), nullable=True)
    rating = Column(Float(10), default=0.0)

    def __repr__(self):
        return f"<User(name='{self.fullname}', username='{self.username}')>"
