from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')
# --- main menu

btnRandom = KeyboardButton('GAME')
btnOther = KeyboardButton('-- другое')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom,btnOther)

# --- other menu ---

btnInfo = KeyboardButton('Информация')
btnMoney = KeyboardButton('Курс валют')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMoney, btnMain)

