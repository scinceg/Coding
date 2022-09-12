from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='5060193439:AAEAmwRBjQKmRslF6-TzEWpFFIVcXRmbkK8')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message):
	basic_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	
	test = types.KeyboardButton('Тестирование 📝')
	materials = types.KeyboardButton('Материалы 📚')
	news = types.KeyboardButton('Новости 📰')
	trainer = types.KeyboardButton('Тренажер 🏋🏼')
	
	basic_menu.add(test, materials, news, trainer)
	
	await bot.send_message(message.from_user.id, '<code>Привет!</code> Что интерисует? 🤔 ', 
	reply_markup=basic_menu, parse_mode="HTML")

@dp.message_handler(content_types=['text'])
async def mess(message):
	if message.text == "Каталог 🗂":
		clava = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		tshirts = types.KeyboardButton('Футболки 👕')
		jeans = types.KeyboardButton('Джинсы 👖')
		shoes = types.KeyboardButton('Обувь 👟')
		shirts = types.KeyboardButton('Рубашки 👔')
		suit = types.KeyboardButton("Костюмы 🎩")
		dress = types.KeyboardButton("Платья 👗")
		back = types.KeyboardButton("Назад ◀️")
		clava.add(tshirts, jeans, shoes, shirts, suit, dress, back)
		send_mess = "Отлично! Что именно интерисует?"
		await bot.send_message(message.from_user.id, send_mess, reply_markup=clava)

	elif message.text == "Обувь 👟":
		clava = types.InlineKeyboardMarkup()
		unity = types.InlineKeyboardButton("Перейти", url="https://intertop.kz/brands/")
		clava.add(unity)
		
		send_mess = "Весь ассортимент можно посмотреть на нашем сайте 👀"
		await bot.send_message(message.from_user.id, send_mess, 
		parse_mode='html', reply_markup=clava)

	elif message.text == 'Назад ◀️':
		clava = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		
		catalog = types.KeyboardButton('Каталог 🗂')
		basket = types.KeyboardButton('Корзина 🛍')
		orders = types.KeyboardButton('Заказы 📦')
		feedback = types.KeyboardButton('Оставить отзыв 📝')
		
		clava.add(catalog, basket, orders, feedback)

		send_mess = f"Отлично! Готов оформлять заказ?"
		await bot.send_message(message.from_user.id, send_mess,
		 parse_mode='html', reply_markup=clava)
	
	elif message.text == "Обувь 👟":
		clava = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		sneakers = types.KeyboardButton('Кроссовки 👟')
		boots = types.KeyboardButton('Ботинки 🥾')
		shoes = types.KeyboardButton('Туфли 🥿')
		slates = types.KeyboardButton('Сланцы 🩴')
		back = types.KeyboardButton("Назад ◀️")
		clava.add(sneakers, boots, shoes, slates, back)
		send_mess = "Хорошо, какую обувь ищещь?"
		await bot.send_message(message.from_user.id, send_mess, reply_markup=clava)

executor.start_polling(dp, skip_updates=True)