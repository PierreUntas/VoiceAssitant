# config.py
from dotenv import load_dotenv
import os

load_dotenv()

WORD_TO_CALL = "yoda"
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
PERPLEXITY_MODEL = "sonar-pro"

DEEBOT_EMAIL = os.getenv("DEEBOT_EMAIL")
DEEBOT_PASSWORD = os.getenv("DEEBOT_PASSWORD")
DEEBOT_COUNTRY = "FR"
