from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import basic_menu, test_ready, materials_kb
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import time


async def command_start(message: types.Message):
        await bot.send_message(message.from_user.id, 'Привет! Что интерисует? 🤔 ', 
        reply_markup=basic_menu)

async def right_answer(callback_query: types.CallbackQuery):
        global rights
        rights = rights + 1

async def wrong_anwear(callback_query: types.CallbackQuery):
        pass


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])

