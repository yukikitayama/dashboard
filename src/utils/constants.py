import os
from dotenv import load_dotenv

load_dotenv()

# OANDA
API_KEY = os.environ["API_KEY"]
API_URL = os.environ["API_URL"]
INSTRUMENT = "USD_JPY"
ALIGNMENT_TIMEZONE = "UTC"