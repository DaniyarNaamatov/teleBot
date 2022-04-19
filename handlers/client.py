from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from config import bot, ADMIN, dp
import random





# @dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"Салам хозяин {message.from_user.full_name}")




# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",

        callback_data="button_call_1"

    )
    markup.add(button_call_1)
    question = "Какого типа данных не существует в Python?"
    answers = ['int', 'str', 'elif', 'tuple']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        reply_markup=markup

                        )



# @dp.message_handler(commands=['mem'])
async def mem(message:types.Message):
    photo = open("media1/prikol.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)

    photo = open("media1/prikol2.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)

    photo = open("media1/prikol3.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)

    photo = open("media1/prikol4.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)

# @dp.message_handler(commands=["ban"], commands_prefix="!/")
async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id != ADMIN:
            await message.reply("Ты не мой БОСС!")

        if not message.reply_to_message:
            await message.reply("Команда должна быть ответом на сообщение!")

        else:
            await message.bot.delete_message(message.chat.id, message.message_id)
            await message.bot.kick_chat_member(message.chat.id, user_id=message.reply_to_message.from_user.id)
            await bot.send_message(
                message.chat.id,
                f"{message.reply_to_message.from_user.full_name} забанен по воле {message.from_user.full_name}")


    else:
        await message.answer("Это работает только в группах!")

async def show_random_user(message: types.Message):
    await bot.db.sql_command_random(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=["start"])
    dp.register_message_handler(quiz_1, commands=["quiz"])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(ban, commands=["ban"], commands_prefix="!/")
    dp.register_message_handler(show_random_user, commands=["random"])
