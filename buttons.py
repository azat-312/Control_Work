from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove




submit = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(KeyboardButton('да'), KeyboardButton('нет'))

size = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True).add(KeyboardButton('XS'), KeyboardButton('S'),KeyboardButton('M'),KeyboardButton('L'),KeyboardButton('XL'),KeyboardButton('XXL'),)

cancel = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,
                             one_time_keyboard=True).add(KeyboardButton('отмена'))

# Удаление кнопок из интерфейса
remove_keyboard = ReplyKeyboardRemove()