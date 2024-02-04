import telebot
from googletrans import Translator
from langdetect import detect
translator = Translator()

# Задаем исходные язык и целевой язык
src = 'en'
dest = 'ru'

# Настраиваем бота
bot = telebot.TeleBot('6522236291:AAGCzISqWMQVuB94-veW4ifYMZk')

# Определяем функцию для обработки сообщений
@bot.message_handler(func=lambda m: True)
def translate_message(message):
  # Берем полученное сообщение и переводим его
  translated_text = translator.translate(message.text, src=src, dest=dest).text
  # Отправляем переведенное сообщение
  bot.send_message(message.chat.id, translated_text)

# Запускаем бота
bot.polling()
