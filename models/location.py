from sqlalchemy import Column, Integer, Sequence, String

from config.database import GlobalDBHelper


class Location(GlobalDBHelper().BASE):

    __tablename__ = 'locations'
    id = Column(Integer, Sequence('location_id_seq'), primary_key=True)
    latitude = Column(Integer)
    longitude = Column(Integer)
    city = Column(String(100), nullable=True)
    state = Column(String(100), nullable=True)
    country = Column(String(100), nullable=True)

    def __repr__(self):
        return f"<Location(name='{self.latitude}', username='{self.longitude}'): [{self.city}]>"
