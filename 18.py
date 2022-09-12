import random
import telebot

from telebot import types

token = '5060193439:AAEAmwRBjQKmRslF6-TzEWpFFIVcXRmbkK8'

bot = telebot.TeleBot('5060193439:AAEAmwRBjQKmRslF6-TzEWpFFIVcXRmbkK8')

@bot.message_handler(commands=["start"])
def welcome(message):
    welcome_str = f"Привет, {message.from_user.first_name}! <b>я Рандомайзер</b> и я помогу тебе сделать сложный выбор 🤖"
    
    simple_clava = types.ReplyKeyboardMarkup(resize_keyboard=True)
    random_answer = types.KeyboardButton("Да или нет?")
    random_food = types.KeyboardButton("Рандомное блюдо")

    simple_clava.add(random_answer, random_food)

    bot.send_message(message.chat.id, welcome_str, parse_mode="html", reply_markup=simple_clava)


@bot.message_handler(content_types=["text"])
def answers(message):
    if message.text == "Да или нет?":
        answers = ['Да', 'Нет']
        index = random.randint(0,1)
        bot.send_message(message.chat.id, answers[index])   
    elif message.text == "Рандомное блюдо":
        foods = ['пицца мицца', 'суши муши', 'сочный мощный восточный шаурма']
        index = random.randint(0, len(foods)-1)
        bot.send_message(message.chat.id, foods[index])
bot.polling(none_stop=True)