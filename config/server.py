import os

from dotenv import load_dotenv

from fastapi import FastAPI

load_dotenv()

app = FastAPI()

server_environment = os.environ.get('ENVIRONMENT')
