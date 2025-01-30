from aiogram import executor, types
import logging
from config import bot, Admins, dp
from handler import commands, FSM_store, FSM_product
from db import main_db
from buttons import start

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот включен!', reply_markup=start)

    await main_db.create_db()

commands.register_handlers(dp)
FSM_store.register_handlers_fsm_store(dp)
FSM_product.register_handlers(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
