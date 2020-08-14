import pyowm
import telebot
from telebot import apihelper

# apihelper.proxy = {'https':'socks5h://157.119.207.10:6667'}

owm = pyowm.OWM('d259f445e96ca353a9cd38355d478ab4', language="ru")
bot = telebot.TeleBot("823384045:AAE9W7-H4VDbbnKWvTPxr_ivFihhe20W3Rk")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет, я сообщаю погоду на улице, для этого тебе нужно написать свой город')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай')
    elif message.text == 'город':
        try:

            observation = owm.weather_at_place(message.text)
            w = observation.get_weather()
            temp = w.get_temperature('celsius')["temp"]

            answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
            answer += "Темпереатура " + str(temp) + "\n"

            bot.send_message(message.chat.id, answer)
        except pyowm.exceptions.api_response_error.NotFoundError:
            bot.send_message(message.chat.id, 'Город не найден :(')
    else:
        bot.send_message(message.chat.id, 'я тебя не понимаю, я нахожусь в стадии разработки')


bot.polling(none_stop=True)
