from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy_jsonfield import JSONField

from config.database import LOCAL_MODEL_SETTINGS


class Location(LOCAL_MODEL_SETTINGS.BASE):

    __tablename__ = 'locations'

    id = Column(Integer, Sequence('location_id_seq'), primary_key=True)

    latitude = Column(Integer)
    longitude = Column(Integer)
    city = Column(String(100), nullable=True)
    state = Column(String(100), nullable=True)
    country = Column(String(100), nullable=True)
    raw_location_record = Column(
        JSONField(
            enforce_string=True,
            enforce_unicode=False
        ),
        nullable=False
    )

    def __repr__(self):
        return f"<Location(latitude='{self.latitude}', longitude='{self.longitude}'): [{self.city}]>"
