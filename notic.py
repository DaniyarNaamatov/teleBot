from aiogram import types, Dispatcher
from aiogram.types import message

from database import bot_db
import database
from config import bot, dp, ADMIN
import asyncio
from asyncio import sleep
import aioschedule
import random

async def notification():
    await database.bot_db.sql_command_random(message)


async def scheduler():
    aioschedule.every(1).day.at("20:00").do(notification())
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def echo_message(message: types.Message):
    global chat_id
    chat_id = message.chat.id

# @dp.message_handler(commands=['games'])
async def dice_1(message: types.Message):
    await bot.send_message(message.from_user.id, f"привет, {message.from_user.full_name}! Это игра в кости")

    computer = await bot.send_dice(message.from_user.id)
    computer = computer['dice'] ['value']
    await sleep(5)

    user = await bot.send_dice(message.from_user.id)
    user = user['dice'] ['value']
    await sleep(5)

    if computer > user:
        await bot.send_message(message.from_user.id, 'Ты проиграл')
    elif computer < user:
        await bot.send_message(message.from_user.id, 'Ты победил')
    else:
        await bot.send_message(message.from_user.id, 'Ничья')


# @dp.message_handler(commands=["pin"], commands_prefix="!/")
async def pin(message: types.Message):
        if message.from_user.id != ADMIN:
            await message.reply("Ты не админ!")
            await message.bot.delete_message(message.chat.id, message.message_id)
        if message.text.startswith('!pin'):

            if not message.reply_to_message:
                await message.reply('Команда должна быть ответом на сообщение!')
            else:
                await bot.pin_chat_message(message.chat.id, message_id=message.message_id)


#
# async def hello(message: types.Message):
#         #noticfations
#         if message.text.startswith("разбуди меня в"):
#             await message.reply("ok")
#             await scheduler(message.text.replace("разубди меня", ""))



# @dp.message_handler()
async def game(message: types.Message):
    emodji = '🏀, 🎲, 🎯, 🎳, 🎰'.split()
    emo = random.choice(emodji)
    if message.text == 'GAME':
        await bot.send_dice(message.from_user.id,emoji=emo),


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(dice_1, commands=["games"])
    dp.register_message_handler(pin, commands=["pin"])
    dp.register_message_handler(game)
