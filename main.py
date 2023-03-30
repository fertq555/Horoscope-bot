import telebot
import requests
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
import tk
from googletrans import Translator, constants


TOKEN = tk.token

bot = telebot.TeleBot(TOKEN)

url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"

keyboard = types.InlineKeyboardMarkup()
key_oven = types.InlineKeyboardButton(text='♈ Овен ♈', callback_data='Aries')
keyboard.add(key_oven)
key_telec = types.InlineKeyboardButton(text='♉ Телец ♉', callback_data='Taurus')
keyboard.add(key_telec)
key_bliznecy = types.InlineKeyboardButton(text='♊ Близнецы ♊', callback_data='Gemini')
keyboard.add(key_bliznecy)
key_rak = types.InlineKeyboardButton(text='♋ Рак ♋', callback_data='Cancer')
keyboard.add(key_rak)
key_lev = types.InlineKeyboardButton(text='♌ Лев ♌', callback_data='Leo')
keyboard.add(key_lev)
key_deva = types.InlineKeyboardButton(text='♍ Дева ♍', callback_data='Virgo')
keyboard.add(key_deva)
key_vesy = types.InlineKeyboardButton(text='♎ Весы ♎', callback_data='Libra')
keyboard.add(key_vesy)
key_scorpion = types.InlineKeyboardButton(text='♏ Скорпион ♏', callback_data='Scorpio')
keyboard.add(key_scorpion)
key_strelec = types.InlineKeyboardButton(text='♐ Стрелец ♐', callback_data='Sagittarius')
keyboard.add(key_strelec)
key_kozerog = types.InlineKeyboardButton(text='♑ Козерог ♑', callback_data='Capricorn')
keyboard.add(key_kozerog)
key_vodoley = types.InlineKeyboardButton(text='♒ Водолей ♒', callback_data='Aquarius')
keyboard.add(key_vodoley)
key_ryby = types.InlineKeyboardButton(text='♓ Рыбы ♓', callback_data='Pisces')
keyboard.add(key_ryby)



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет я Гороскоп-бот, я расскажу тебе твой гороскоп на сегодня')
    bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global znak
    if call.data == "Aries":
        znak = 'Aries'
    elif call.data == 'Taurus':
        znak = 'Taurus'
    elif call.data == 'Gemini':
        znak = 'Gemini'
    elif call.data == 'Cancer':
        znak = 'Cancer'
    elif call.data == 'Leo':
        znak = 'Leo'
    elif call.data == 'Virgo':
        znak = 'Virgo'
    elif call.data == 'Libra':
        znak = 'Libra'
    elif call.data == 'Scorpio':
        znak = 'Scorpio'
    elif call.data == 'Sagittarius':
        znak = 'Sagittarius'
    elif call.data == 'Capricorn':
        znak = 'Capricorn'
    elif call.data == 'Aquarius':
        znak = 'Aquarius'
    elif call.data == 'Pisces':
        znak = 'Pisces'


    querystring = {"sign": znak, "day": "today"}

    headers = {
        "X-RapidAPI-Key": "6adb1ecdc2msh523ef67e40e0d86p191567jsnb3e001c3c76d",
        "X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com"
    }

    response = requests.request("POST", url, headers=headers, params=querystring)



    a = response.json()['description']

    luky = response.json()['lucky_number']
    lucky_time = response.json()['lucky_time']
    translator = Translator()

    result = translator.translate(a, src='en', dest='ru')
    ru_znak = translator.translate(znak, src='en', dest='ru')

    answer = result.text
    answer_ru_znak = ru_znak.text

    n = f'{answer_ru_znak}:{answer}\n' \
        f'Ваше счастливое число:{luky}.\n' \
        f'Ваше счастливое время : {lucky_time}'

    bot.send_message(call.message.chat.id,n)
    bot.polling(none_stop=True, interval=10000)

bot.infinity_polling()
