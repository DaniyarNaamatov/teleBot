from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from decouple import config
from asyncio import sleep

import markup as nav
import logging
import random



TOKEN = config("TOKEN")
ADMIN = 1790397125
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"йоу это домашка_1 {message.from_user.full_name}",reply_markup=nav.mainMenu)



@dp.message_handler(commands=['end'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"10? получил или нет?((  {message.from_user.full_name}")


@dp.message_handler(commands=['stop'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"все таки получил? {message.from_user.full_name}")




@dp.message_handler(commands=['mem'])
async def mem(message:types.Message):
    photo = open("media1/prikol.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)

    photo = open("media1/prikol2.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)

    photo = open("media1/prikol3.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)

    photo = open("media1/prikol4.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)

@dp.message_handler(commands=['quiz1'])
async def quiz_1(message: types.Message):
        markup0 = InlineKeyboardMarkup()
        button_call_1 = InlineKeyboardButton(
            "NEXT",
            callback_data="button_call_1"
        )
        markup0.add(button_call_1)

        photo = open("media/fizika.jpg", "rb")
        await bot.send_photo(message.chat.id, photo=photo),

        question = "Каждые сутки Земля «поправляется» на 400 т. За счет чего?:"
        answers = ["Космическая пыль", 'грунт', 'вода', 'земля', 'огонь', "шутка?"]
        await bot.send_poll(message.chat.id,
                            question=question,
                            options=answers,
                            is_anonymous=False,
                            type='quiz',
                            correct_option_id=0,
                            open_period=10,
                            reply_markup=markup0
                            )

@dp.message_handler(commands=['quiz2'])
async def quiz_2(message: types.Message):
        markup1 = InlineKeyboardMarkup()
        button_call_2 = InlineKeyboardButton(
            "NEXT",
            callback_data="button_call_2"
        )
        markup1.add(button_call_2)

        photo = open("media/fizika2.jpg", "rb")
        await bot.send_photo(message.chat.id, photo=photo),

        question = "Какая жидкость самая легкая?"
        answers = ['Вода', 'Воздух', 'Азот', 'Сжиженный водород']


        await bot.send_poll(message.chat.id,
                            question=question,
                            options=answers,
                            is_anonymous=False,
                            type='quiz',
                            correct_option_id=2,
                            open_period=10,
                            reply_markup=markup1
                            )


@dp.message_handler(commands=['quiz3'])
async def quiz_3(message: types.Message):
        markup2 = InlineKeyboardMarkup()
        button_call_3 = InlineKeyboardButton(
            "NEXT",

            callback_data="button_call_3"
        )
        markup2.add(button_call_3)

        photo = open("media/fizika3.jpg", "rb")
        await bot.send_photo(message.chat.id, photo=photo),

        question = "Как называется упорядоченное движение заряженных частиц??"
        answers = ['Электрический ток', 'Реакция', 'Растворение']
        await bot.send_poll(message.chat.id,
                            question=question,
                            options=answers,
                            is_anonymous=False,
                            type='quiz',
                            correct_option_id=3,
                            open_period=10,
                            reply_markup=markup2
                            )


@dp.message_handler(commands=['quiz4'])
async def quiz_4(message: types.Message):
        markup3 = InlineKeyboardMarkup()
        button_call_4 = InlineKeyboardButton(
            "NEXT",
            callback_data="botton_call_4"
        )
        markup3.add(button_call_4)

        photo = open("media/fizika4.jpg", "rb")
        await bot.send_photo(message.chat.id, photo=photo),

        question = "Как называется упорядоченное движение заряженных частиц??"
        answers = ['Электрический ток', 'Реакция', 'Растворение']
        await bot.send_poll(message.chat.id,
                            question=question,
                            options=answers,
                            is_anonymous=False,
                            type='quiz',
                            correct_option_id=0,
                            open_period=10,
                            reply_markup=markup3
                            )



############## ---callback---- ############


@dp.callback_query_handler(lambda func: func.data == "button_call_1")
async def quiz_1(call: types.CallbackQuery):
    markup0 = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data="botton_call_1"
    )
    markup0.add(button_call_1)
    photo = open("media/fizika.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)

    question = "Каждые сутки Земля «поправляется» на 400 т. За счет чего?:"
    answers = ["Космическая пыль", 'грунт', 'вода', 'земля', 'огонь', "шутка?"]



    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=5,
                        reply_markup=markup0
                        )



@dp.callback_query_handler(lambda func: func.data == "button_call_2")
async def quiz_2(call: types.CallbackQuery):
    markup1 = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_2"
    )
    markup1.add(button_call_2)

    photo = open("media/fizika3.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo),

    question = "Какая жидкость самая легкая?"
    answers = ['Вода', 'Воздух', 'Азот', 'Сжиженный водород']


    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=10,
                        reply_markup=markup1
                        )


@dp.callback_query_handler(lambda func: func.data == "button_call_3")
async def quiz_3(call: types.CallbackQuery):
    markup2 = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_3"
    )
    markup2.add(button_call_3)

    photo = open("media/fizika3.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo),

    question = "Как называется упорядоченное движение заряженных частиц??"
    answers = ['Электрический ток', 'Реакция', 'Растворение']
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=3,
                        open_period=10,
                        reply_markup=markup2
                        )





@dp.callback_query_handler(lambda func: func.data == "button_call_4")
async def quiz_4(call: types.CallbackQuery):
        markup3 = InlineKeyboardMarkup()
        button_call_4 = InlineKeyboardButton(
            "NEXT",
            callback_data="button_call_4"
        )
        markup3.add(button_call_4)

        photo = open("media/fizika4.jpg", "rb")
        await bot.send_photo(call.message.chat.id, photo=photo),

        question = "Как называется упорядоченное движение заряженных частиц??"
        answers = ['Электрический ток', 'Реакция', 'Растворение']
        await bot.send_poll(call.message.chat.id,
                            question=question,
                            options=answers,
                            is_anonymous=False,
                            type='quiz',
                            correct_option_id=0,
                            open_period=10,
                            reply_markup=markup3
                            )








@dp.message_handler(commands=["pin"], commands_prefix="!/")
async def pin(message: types.Message):
        if message.from_user.id != ADMIN:
            await message.reply("Ты не админ!")
        if message.text.startswith('!pin'):

            if not message.reply_to_message:
                await message.reply('Команда должна быть ответом на сообщение!')
            else:
                await bot.pin_chat_message(message.chat.id, message.message_id)


# @dp.message_handler(commands=['games'])
# async def dice_1(message: types.Message):
#     await bot.send_message(message.from_user.id, f"привет, {message.from_user.full_name}! Это игра в кости")
#
#
#     computer = await bot.send_dice(message.from_user.id)
#     computer = computer['dice'] ['value']
#     await sleep(5)
#
#     user = await bot.send_dice(message.from_user.id)
#     user = user['dice'] ['value']
#     await sleep(5)
#
#     if computer > user:
#         await bot.send_message(message.from_user.id, 'Ты проиграл')
#     elif computer < user:
#         await bot.send_message(message.from_user.id, 'Ты победил')
#     else:
#         await bot.send_message(message.from_user.id, 'Ничья')









@dp.message_handler()
async def game(message: types.Message):
    emodji = '🏀, 🎲, 🎯, 🎳, 🎰'.split()
    emo = random.choice(emodji)
    if message.text == 'GAME':
        await bot.send_dice(message.from_user.id,emoji=emo),

    elif message.text == 'другое':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=nav.mainMenu)

    elif message.text == 'другое':
        await bot.send_message(message.from_user.id, 'другое', reply_markup=nav.btnOther)




                            ############ MENU #############
btnMain = KeyboardButton('Главное меню')
# --- main menu

btnRandom = KeyboardButton('GAME')
btnOther = KeyboardButton('-- другое')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom,btnOther)

# --- other menu ---

btnInfo = KeyboardButton('Информация')
btnMoney = KeyboardButton('Курс валют')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMoney, btnMain)

btnMain = KeyboardButton('Главное меню')





if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)
