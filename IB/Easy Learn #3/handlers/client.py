from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import basic_menu, test_ready, trainer_kb
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
        if message.text == 'Тренажер 🏋🏼':
                await bot.send_message(message.from_user.id, 'Пришло время улучшить навыки', reply_markup=trainer_kb)
        if message.text == 'Перевести предложение 💭':
                data = sqlite_db.sql_read_translate()
                await translate_send_first(data, message)
# async def translate_word(callback_query: types.CallbackQuery):
        # click_words.append(callback_query.data)
        
# async def translates_sentences(callback_query: types.CallbackQuery):
        # global click_words, translates_right, order_tr, laudatory_msg
        # if click_words in translates_right:
        #         choice = random.choice(laudatory_msg)
        #         await bot.send_message(callback_query.from_user.id, choice)
        #         time.sleep(1)
        # else:
        #         msg = 'Не верно, правильный вариант:\n'
        #         for word in translates_right[order_tr]:
        #                 msg += text(italic(word)) + ' '
        #         await bot.send_message(callback_query.from_user.id,  msg, parse_mode=ParseMode.MARKDOWN)
        #         time.sleep(2)
        # click_words = []
        # if order_tr<len(translates_btn)-1:
        #         order_tr +=1
        #         sentence = translates_btn[order_tr]
        #         translates_sentence = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
        #         translate_btn_array = []
        #         rus_translate = text(italic(translates_rus[order_tr]))
        #         for word in sentence:
        #                 word_btn = InlineKeyboardButton(word, callback_data=str(word))
        #                 translate_btn_array.append(word_btn)
        #         translates_sentence.row(*translate_btn_array)\
        #                 .add(InlineKeyboardButton("Отправить", callback_data='translate'))
        #         msg =  'Переведи предложение и выбери правильную очередность:\n' + rus_translate
        #         await bot.send_message(callback_query.from_user.id, msg, reply_markup=translates_sentence, parse_mode=ParseMode.MARKDOWN)    
        # else: 
        #         await bot.send_message(callback_query.from_user.id, 'Вопросы закончились 😅')    

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

async def translate_send_first(data, message):
        global translates_rus, translates_btn, translates_right, order_translate

        order_translate = 0 
        translates_rus = []
        for entry in data:
                rus_sentence = entry[0]
                translates_rus.append(rus_sentence)
    
        translates_btn = []
        for entry in data:
                wrong_sentence = entry[1]
                wrong_sentence = wrong_sentence.split(',')
                translates_btn.append(wrong_sentence)

        translates_right = []
        for entry in data:
                right_sentence = entry[2]
                right_sentence = right_sentence.split(",")
                translates_right.append(right_sentence)
        sentence = translates_btn[order_translate]
        translates_sentence = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
        translate_btn_array = []
        rus_translate = f'<u>{translates_rus[order_translate]}</u>'
        for word in sentence:
                word_btn = InlineKeyboardButton(word, callback_data=str(word))
                translate_btn_array.append(word_btn)
        translates_sentence.row(*translate_btn_array).\
                add(InlineKeyboardButton("Отправить", callback_data='next_translate'))
        msg =  'Переведи предложение и выбери правильную очередность:\n' + rus_translate
        await bot.send_message(message.from_user.id, msg, reply_markup=translates_sentence, parse_mode='HTML')    

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(text_message, content_types=['text'])
    dp.register_callback_query_handler(right_answer, text = 'right')


