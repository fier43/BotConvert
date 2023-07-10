import telebot
from constants import BOT_API_KEY, CRIPTO_KEY, keys
from extensions import ConvertionException, CriptoConverter


bot = telebot.TeleBot(BOT_API_KEY)



@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команды боту в следующем формате:\n<имя валюты> \
<в какую валюту перенести> \
<количество переводимой валюты>\nУвидить список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = "\n".join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    value = message.text.split(" ")

    try:
        if len(value) != 3:
            raise ConvertionException("Слишком много параметров.")

        quote, base, amout = value
        total_base = CriptoConverter.convert(quote, base, amout)
    except ConvertionException as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Неудалось обработать команду\n{e}")
    else:
        summ = (float(total_base) * float(amout))
        text = f"Цена {amout} {quote} в {base} : {summ}"
        bot.send_message(message.chat.id, text)


def start():
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except requests.exceptions.ConnectionError as _ex:
            print(_ex)
            sleep(15)


if __name__ == "__main__":
    try:
        start()
        # bot.polling(none_stop=True)
    except ConnectionError as e:
        print("Ошибка соединения: ", e)
    except Exception as r:
        print("Непридвиденная ошибка: ", r)
    finally:
        print("Здесь всё закончилось")

