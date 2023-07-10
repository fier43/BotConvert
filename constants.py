import os

from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(".env"))

BOT_API_KEY = os.environ.get("BOT_API_KEY")
CRIPTO_KEY = os.environ.get("CRIPTO_KEY")

keys = {
    "рубль": "RUB",
    "евро": "EUR",
    "доллар": "USD",
}
