from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot

# states
class FSMAdmin(StatesGroup):
    photo = State()
    dish_name = State()
    Descriptions = State()
    price = State()
    region = State()

# start fsm
async def fsm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await bot.send_message(message.chat.id,
                           f"Привет {message.from_user.full_name}, отправьте фото блюдо, которую хотите заказать...")

# load photo
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await bot.send_message(message.chat.id, "это точно?")

#load name
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dish_name'] = message.text
    await FSMAdmin.next()
    await bot.send_message(message.chat.id, "Название блюда?")

#load surname
async def load_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Descriptions'] = message.text
    await FSMAdmin.next()
    await bot.send_message(message.chat.id, "Опишите блюдо")


async def load_age(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['price$'] = int(message.text)
        await FSMAdmin.next()
        await bot.send_message(message.chat.id, "Где живешь?")
    except:
        await bot.send_message(message.chat.id, "Я сказал только числа!!!")

#load region
async def load_region(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text
    async with state.proxy() as data:
        await bot.send_message(message.chat.id, str(data))
    await state.finish()
    await bot.send_message(message.chat.id, "Все свободен)")

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

    dp.register_message_handler(fsm_start, commands=["dish"])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=["photo"])
    dp.register_message_handler(load_name, state=FSMAdmin.dish_name)
    dp.register_message_handler(load_surname, state=FSMAdmin.Descriptions)
    dp.register_message_handler(load_age, state=FSMAdmin.price)
    dp.register_message_handler(load_region, state=FSMAdmin.region)

