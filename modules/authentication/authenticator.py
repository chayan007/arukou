import hashlib

from config.database import DATABASE_DRIVER

from models.user import User


class Authenticator:

    def __init__(self):
        """Initialize instance variables."""
        self.db_session = DATABASE_DRIVER.SESSION

    def register(self, fullname: str, email: str, username: str, password: str, mobile: str):
        """Register an user."""
        user = User()
        user.fullname = fullname
        user.email = email
        user.username = username
        user.hashed_password = hashlib.md5(password.strip())
        user.mobile = mobile

        try:
            self.db_session.add(user)
            self.db_session.commit()
        except BaseException as e:
            raise e

    def login(self):
        """Login an user."""
        pass

    def verify(self):
        """Verify an user."""
        pass

    def reset_password(self):
        """Reset password for an user."""
        pass
