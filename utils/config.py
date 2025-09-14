import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")

# xyz