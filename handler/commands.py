from aiogram import Dispatcher, types, bot
from config import bot
from db import main_db


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}!\n'
                                f'Твой telegram ID - {message.from_user.id}\n')

    await message.answer('Привет!')


async def info_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'этот бот создан для теста он нужен что вы могли смотреть что в списке и добавлять заказы')
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])

