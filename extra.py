from aiogram import Bot, Dispatcher, types, executor, bot
from asyncio import sleep


@dp.message_handler(commands=['games'])
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


