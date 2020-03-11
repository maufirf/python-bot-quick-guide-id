from dotenv import load_dotenv
import os
from enum import Enum

load_dotenv()

class GENERAL_ACCESS_TOKEN(Enum):
    DISCORD = os.getenv("ACCESS_TOKEN_DISCORD")
    TWITTER = os.getenv("ACCESS_TOKEN_TWITTER")
    FACEBOOK = os.getenv("ACCESS_TOKEN_FACEBOOK")

class TWITTER_KEYS(Enum):
    API_KEY = os.getenv("")
    API_SECRET = os.getenv("")
    ACCESS_TOKEN = GENERAL_ACCESS_TOKEN.TWITTER.value
    ACCESS_TOKEN_SECRET = os.getenv("")
