from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import basic_menu, test_ready
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data_base import sqlite_db

async def command_start(message: types.Message):
        await bot.send_message(message.from_user.id, 'Привет! Что интерисует? 🤔 ', 
        reply_markup=basic_menu)

async def text_message(message: types.Message):
        if message.text == 'Тестирование 📝':
                await bot.send_message(message.from_user.id, 'Тест состоит из 5 вопросов. Готовы?', reply_markup=test_ready)
        if message.text == 'Да':
                data = sqlite_db.sql_read_tesing()
                await testing(data, message)
        if message.text == 'Нет'  or message.text == 'Назад ◀️':
                  await bot.send_message(message.from_user.id, 'Обратно в главном меню 🔙', reply_markup=basic_menu)

async def testing(data, message): 
        global questions, order_testing, rights, variants, right_answers
        rights = 0 
        order_testing = 0

        questions = []
        for entry in data:
                question = entry[0]
                questions.append(question)
    
        variants = []
        for entry in data:
                variant = entry[1]
                variant = variant.split(',')
                variants.append(variant)

        right_answers = []
        for entry in data:
                right = entry[2]
                right_answers.append(right)

        variant_kb = InlineKeyboardMarkup(resize_keyboard=True)
        for variant in variants[order_testing]:
                if variant == right_answers[order_testing]:
                        variant_btn = InlineKeyboardButton(variant, callback_data='right')
                else: 
                        variant_btn = InlineKeyboardButton(variant, callback_data='wrong')
                variant_kb.add(variant_btn)
        variant_kb.add(InlineKeyboardButton('Следующий вопрос', callback_data='next_testing_question'))
        await bot.send_message(message.from_user.id, questions[order_testing],reply_markup=variant_kb)

async def right_answer(callback_query: types.CallbackQuery):
        global rights
        rights += 1

async def send_next_testing_question(callback_query: types.CallbackQuery):
        global order_testing
        order_testing+=1
        if order_testing<len(questions)-1:
                variant_kb = InlineKeyboardMarkup(resize_keyboard=True)
                for variant in variants[order_testing]:
                        if variant == right_answers[order_testing]:
                                variant_btn = InlineKeyboardButton(variant, callback_data='right')
                        else: 
                                variant_btn = InlineKeyboardButton(variant, callback_data='wrong')
                        variant_kb.add(variant_btn)
                if order_testing<len(questions)-2:
                        variant_kb.add(InlineKeyboardButton('Следующий вопрос', callback_data='next_testing_question'))
                else: 
                        variant_kb.add(InlineKeyboardButton('Закончить тестирование', callback_data='next_testing_question'))
                await bot.send_message(callback_query.from_user.id, questions[order_testing],reply_markup=variant_kb)
        else: 
                await bot.send_message(callback_query.from_user.id, 'Результат теста: {0}/{1}'.format(rights, len(questions)),\
                         reply_markup=basic_menu)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(text_message, content_types=['text'])
    dp.register_callback_query_handler(right_answer, text = 'right')
    dp.register_callback_query_handler(send_next_testing_question, text = 'next_testing_question')


