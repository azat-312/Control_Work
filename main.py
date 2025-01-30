from aiogram import executor, types
import logging
from config import bot, Admins, dp
from handler import commands, FSM_store, FSM_product


commands.register_handlers(dp)
FSM_store.register_handlers_fsm_store(dp)
FSM_product.register_handlers(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
