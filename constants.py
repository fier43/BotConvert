import os

from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(".env"))

BOT_API_KEY = os.environ.get("BOT_API_KEY")
CRIPTO_KEY = os.environ.get("CRIPTO_KEY")

CURRENCIES = {
    "рубль": "RUB",
    "евро": "EUR",
    "доллар": "USD",
}

HELP_TEXT = (
    "Чтобы начать работу введите команды боту в следующем формате:\n\n"
    "<имя валюты> <в какую валюту перенести> <количество переводимой валюты>\n\n"
    "Увидить список всех доступных валют: /values"
)
AVAILABLE_CURRENCIES_TEXT = "Доступные валюты:"
RESPONSE_TEXT = "Цена {0} {1} в {2} : {3}"

MANY_PARAMETERS_ERROR = "Слишком много параметров."
USER_ERROR = "Ошибка пользователя"
COMMAND_ERROR = "Неудалось обработать команду"

