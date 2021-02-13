from config.database import DATABASE_DRIVER

from models.user import User


class KYC:

    def __init__(self, user_id: str):
        """Declare all class variables."""
        self.user = DATABASE_DRIVER.SESSION.query(User).get(user_id)

    def initiate(self):
        """Initiate KYC for a user."""
        pass

    def accept(self):
        """Accept KYC status for a user."""
        pass

    def reject(self):
        """Reject KYC status for a user and ask them to validate again."""
        pass

    @staticmethod
    def status():
        """Get KYC status of an user."""
        pass
