import telebot
from constants import (
    BOT_API_KEY,
    CRIPTO_KEY,
    CURRENCIES,
    HELP_TEXT,
    AVAILABLE_CURRENCIES_TEXT,
    MANY_PARAMETERS_ERROR,
    USER_ERROR,
    COMMAND_ERROR,
    RESPONSE_TEXT,
)
from extensions import ConvertionException, CriptoConverter


bot = telebot.TeleBot(BOT_API_KEY)


@bot.message_handler(commands=["start", "help"])
def help(message: telebot.types.Message):
    bot.reply_to(message, HELP_TEXT)


@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = AVAILABLE_CURRENCIES_TEXT
    for key in CURRENCIES.keys():
        text = "\n".join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def get_price(message: telebot.types.Message):
    value = message.text.split(" ")

    try:
        if len(value) != 3:
            raise ConvertionException(MANY_PARAMETERS_ERROR)

        quote, base, amout = value
        total_base = CriptoConverter.convert(quote, base, amout)
    except ConvertionException as e:
        bot.reply_to(message, f"{USER_ERROR}\n{e}")
    except Exception as e:
        bot.reply_to(message, f"{COMMAND_ERROR}\n{e}")
    else:
        summ = float(total_base) * float(amout)
        text = RESPONSE_TEXT.format(amout, quote, base, summ)
        bot.send_message(message.chat.id, text)


if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except ConnectionError as e:
        print("Ошибка соединения: ", e)
    except Exception as r:
        print("Непридвиденная ошибка: ", r)
    finally:
        print("Здесь всё закончилось")
