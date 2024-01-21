from config import Token
from random import randint
import keyboards
import telebot

images = ["https://static.wikia.nocookie.net/dota2_gamepedia/images/2/23/Axe_icon.png/revision/latest?cb=20160411211422",
          "https://static.wikia.nocookie.net/halflife/images/1/19/Clarity_Level.png/revision/latest?cb=20151005104429&path-prefix=de",
          "https://static.wikia.nocookie.net/dota2_gamepedia/images/e/ed/Centaur_Warrunner_icon.png/revision/latest?cb=20160411210603",
          "https://cs13.pikabu.ru/post_img/2020/03/11/4/158390533813195488.jpg",
          "https://www.axe.com/ru/images/common/hero-sxn-img.png"]
bot = telebot.TeleBot(Token)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Если ты отправишь сюда стикер то ты получишь его айди", reply_markup=keyboards.Inmune)
@bot.message_handler(commands=['hero'])
def hero(message):
    bot.send_photo(message.chat.id,images[randint(0,4)], reply_markup=keyboards.menu)
@bot.message_handler(content_types=['sticker'])
def item(message):
    sticker_id = message.sticker.file_id
    bot.send_message(message.chat.id,f'айди стикера:{sticker_id}')
@bot.callback_query_handler(func=lambda call:True)
def call_inline(call):
    if call.data =='1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text = "douple_start",reply_markup=keyboards.Inmune)
def hello(message):
    bot.send_message(message.chat.id, "اذهب و عاشر نفسك" , reply_markup=keyboards.menu)
bot.polling(none_stop = True)