from sqlalchemy import Column, Integer, Sequence, String, ForeignKey

from config.database import DATABASE_DRIVER

from models.location import Location

from models.user import User


class Meet(DATABASE_DRIVER.BASE):

    __tablename__ = 'meets'

    id = Column(Integer, Sequence('meet_id_seq'), primary_key=True)

    inviter_id = Column(Integer, ForeignKey(User.id))
    invitee_id = Column(Integer, ForeignKey(User.id))
    source_location_id = Column(Integer, ForeignKey(Location.id))
    destination_location_id = Column(Integer, ForeignKey(Location.id))
    time_selected = Column(String(100), nullable=True)

    def __repr__(self):
        return f"<Location(name='{self.latitude}', username='{self.longitude}'): [{self.city}]>"
