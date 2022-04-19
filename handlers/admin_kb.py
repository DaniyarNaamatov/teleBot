from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_button = KeyboardButton("Отмена")
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)

cancel_markup.row(cancel_button)


button_load = KeyboardButton("Загрузить")
button_delete = KeyboardButton("Удалить")

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)\
                    .add(button_delete)