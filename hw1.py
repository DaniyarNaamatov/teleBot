from aiogram import executor
from config import dp
import logging
from handlers import callback,client,notic,fsmAdminMenu, fsmAdminGetUser
from database import bot_db



async def on_start_up(_):
    bot_db.sql_create()


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
# fsmAdminGetUser.register_hendler_fsmAdminGetUser(dp)
fsmAdminMenu.register_hendler_fsmAdminMenu(dp)


notic.register_handlers_notification(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False, on_startup=(on_start_up))
