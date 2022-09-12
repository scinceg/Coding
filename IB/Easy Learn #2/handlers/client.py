from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import basic_menu, test_ready
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data_base import sqlite_db
import time

async def command_start(message: types.Message):
        await bot.send_message(message.from_user.id, 'Привет! Что интерисует? 🤔 ', 
        reply_markup=basic_menu)

async def text_message(message: types.Message):
        global rights
        if message.text == 'Тестирование 📝':
                await bot.send_message(message.from_user.id, 'Тест состоит из 5 вопросов. Готов?', reply_markup=test_ready)
        if message.text == 'Да':
                data = sqlite_db.sql_read_tesing()
                await testing(data, message)
        if message.text == 'Нет'  or message.text == 'Назад ◀️':
                  await bot.send_message(message.from_user.id, 'Обратно в главном меню 🔙', reply_markup=basic_menu)

async def testing(data, message):
        rights = 0 
        global questions
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

        for number_of_question in range(len(questions)):
                variant_kb = InlineKeyboardMarkup(resize_keyboard=True)
                for variant in variants[number_of_question]:
                        if variant == right_answers[number_of_question]:
                                variant_btn = InlineKeyboardButton(variant, callback_data='right')
                        else: 
                                variant_btn = InlineKeyboardButton(variant, callback_data='wrong')
                        variant_kb.add(variant_btn)
                await bot.send_message(message.from_user.id, questions[number_of_question],reply_markup=variant_kb)
                time.sleep(4)
        await bot.send_message(message.from_user.id, 
                'Результат теста: {0}/{1}'.format(rights, len(questions)), reply_markup=basic_menu)

async def right_answer(callback_query: types.CallbackQuery):
        global rights
        rights += 1

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(text_message, content_types=['text'])
    dp.register_callback_query_handler(right_answer, text = 'right')


