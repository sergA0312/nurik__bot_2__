from aiogram.utils import executor
from config import dp
from handlers import start, chat_actions, callback
from database.sql_commands import  Database


async def on_start_up(_):
    db = Database()
    db.sql_create_db()


start.register_start_handlers(dp=dp)
callback.register_callback_handlers(dp=dp)
chat_actions.register_chat_actions_handlers(dp=dp)

if __name__ == "__main__":
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_start_up)