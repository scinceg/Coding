import telebot

Token = '5060193439:AAEAmwRBjQKmRslF6-TzEWpFFIVcXRmbkK8'

bot = telebot.TeleBot(Token)

@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "Бот запущен!")

@bot.message_handler(commands=["help"])
def welcome(message):
    bot.send_message(message.chat.id, "Какая помощь вам нужна?")

bot.polling(none_stop=True)