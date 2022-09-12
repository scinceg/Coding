from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '5060193439:AAEAmwRBjQKmRslF6-TzEWpFFIVcXRmbkK8'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)