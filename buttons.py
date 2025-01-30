from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(
    KeyboardButton('/start'))




size = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True).add(KeyboardButton('XS'), KeyboardButton('S'),KeyboardButton('M'),KeyboardButton('L'),KeyboardButton('XL'),KeyboardButton('XXL'),)

cancel = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,
                             one_time_keyboard=True).add(KeyboardButton('отмена'))

# Удаление кнопок из интерфейса
remove_keyboard = ReplyKeyboardRemove()