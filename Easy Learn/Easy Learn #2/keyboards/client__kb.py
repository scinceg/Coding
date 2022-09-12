from aiogram import types

test = types.KeyboardButton('Тестирование 📝')
materials = types.KeyboardButton('Материалы 📚')
news = types.KeyboardButton('Новости 📰')
trainer = types.KeyboardButton('Тренажер 🏋🏼')
basic_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
basic_menu.add(test, materials, news, trainer)

yes = types.KeyboardButton('Да')
no = types.KeyboardButton('Нет')
test_ready = types.ReplyKeyboardMarkup(resize_keyboard=True)
test_ready.add(yes, no)