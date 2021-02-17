from models.location import Location

from models.user import User


class Tracker:

    def current_location(self, user: User):
        pass

    def nearby_profiles(self, location: Location):
        pass

    def estimate_path(self, source: Location, destination: Location):
        pass
