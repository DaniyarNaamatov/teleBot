from aiogram import types, Dispatcher
from config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# @dp.callback_query_handler(lambda func: func.data == "button_call_1")
async def quiz_1(call: types.CallbackQuery):
    photo = open("media/fizika.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)

    question = "&:"
    answers = ["Космическая пыль", 'грунт', 'вода', 'земля', 'огонь', "шутка?"]



    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=5,
                        )



# @dp.callback_query_handler(lambda func: func.data == "button_call_2")
async def quiz_2(call: types.CallbackQuery):

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
                        )


# @dp.callback_query_handler(lambda func: func.data == "button_call_3")
async def quiz_3(call: types.CallbackQuery):
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
                        )





# @dp.callback_query_handler(lambda func: func.data == "button_call_4")
async def quiz_4(call: types.CallbackQuery):

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
                            )



def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(
                quiz_1,
                lambda func: func.data == "button_call_1"

            )
    dp.register_callback_query_handler(
                quiz_2,
                lambda func: func.data == "button_call_2"

            )
    dp.register_callback_query_handler(
                quiz_3,
                lambda func: func.data == "button_call_3"

            )
    dp.register_callback_query_handler(
                quiz_4,
                lambda func: func.data == "button_call_4"

            )






