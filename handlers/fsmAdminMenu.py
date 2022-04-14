from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot

# states состоянии
class FSMAdmin(StatesGroup):
    photo = State()
    dish_name = State()
    Descriptions = State()
    price = State()
    region = State()

                                        ##меню##
async def hello(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('отправьте фото блюдо 🍝🍝')

#загрузка фото
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply("Теперь введите название блюдо 	🍔")


#описание блюдо
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dish_name'] = message.text
    await FSMAdmin.next()
    await message.reply("Введите описание ✏")

# цена
async def load_Des(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Descriptions'] = message.text
    await FSMAdmin.next()
    await message.reply("Теперь укажите цену 💵")


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)

        await state.finish()
        await bot.send_message(message.chat.id, "Все ваш заказ запишен 	✅")



async def cancal_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.reply("ОК")

def register_hendler_fsmAdminGetUser(dp: Dispatcher):
    dp.register_message_handler(cancal_reg, state="*", commands="cancel")
    dp.register_message_handler(cancal_reg, Text(equals='cancel', ignore_case=True),state="*")

    dp.register_message_handler(hello, commands=["dish"])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=["photo"])
    dp.register_message_handler(load_name, state=FSMAdmin.dish_name)
    dp.register_message_handler(load_Des, state=FSMAdmin.Descriptions)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
