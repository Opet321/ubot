from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_HASH = getenv("API_HASH", "")
API_ID = int(getenv("API_ID", None))
PREFIXES_CMD = getenv("PREFIXES_CMD", ".")
SESSION_STRING = getenv("SESSION_STRING", "")
