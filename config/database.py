from config.server import server_environment

from constants.environment import Environment

if server_environment == Environment.LOCAL:
    pass

if server_environment == Environment.PRODUCTION:
    pass
