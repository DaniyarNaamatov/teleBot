# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from aiogram import Bot, Dispatcher, types, executor, bot
# from config import bot, dp
# import markup as nav
#
# btnMain = KeyboardButton('Главное меню')
# # --- main menu
# @dp.message_handler(commands=['start'])
# async def hello(message: types.Message):
#     await bot.send_message(message.chat.id, f"йоу это домашка_1 {message.from_user.full_name}",reply_markup=nav.mainMenu)
#
#
#     btnRandom = KeyboardButton('GAME')
#     btnOther = KeyboardButton('-- другое')
#
#     mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom,btnOther)
#
# # --- other menu ---
#     await bot.send_message(message.from_user.id, 'другое', reply_markup=nav.btnOther)
#     btnInfo = KeyboardButton('Информация')
#     btnMoney = KeyboardButton('Курс валют')
#     otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMoney, btnMain)
#     btnMain = KeyboardButton('Главное меню')
# # --- main menu
#
#     btnRandom = KeyboardButton('GAME')
#     btnOther = KeyboardButton('-- другое')
#
#     mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom,btnOther)
#
# # --- other menu ---
#
#     btnInfo = KeyboardButton('Информация')
#     btnMoney = KeyboardButton('Курс валют')
#     otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMoney, btnMain)
#
#     btnMain = KeyboardButton('Главное меню')
