from dotenv import load_dotenv # Import library untuk mengakses file .env
import os # Import library untuk mengambil variabel dari komputer
from enum import Enum # Yang ini udah ikutin aja dulu

load_dotenv() # Memproses file .env semudah memanggil fungsi ini aja

class GENERAL_ACCESS_TOKEN(Enum):
    DISCORD = os.getenv("ACCESS_TOKEN_DISCORD")
    TWITTER = os.getenv("ACCESS_TOKEN_TWITTER")
    FACEBOOK = os.getenv("ACCESS_TOKEN_FACEBOOK")

class TWITTER_KEYS(Enum):
    API_KEY = os.getenv("TWITTER_API_KEY")
    API_SECRET = os.getenv("TWITTER_API_SECRET")
    ACCESS_TOKEN = GENERAL_ACCESS_TOKEN.TWITTER.value
    ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
