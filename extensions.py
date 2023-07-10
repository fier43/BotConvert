import requests
import json
from constants import keys


class ConvertionException(Exception):
    pass

class CriptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amout: str):

        if quote == base:
            raise ConvertionException(f"Невозможно перевести одинаковые валюты {base}.")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"Неудалось обработать валюту {quote}.")

        try:
            quote_base = keys[base]
        except KeyError:
            raise ConvertionException(f"Неудалось обработать валюту {base}.")

        try:
            amout = float(amout)
        except:
            raise ConvertionException(f"Неудалось обработать количество {amout}.")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={quote_base}")
        total_base = json.loads(r.content)[keys[base]]

        return total_base
