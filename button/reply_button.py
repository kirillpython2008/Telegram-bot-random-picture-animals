from aiogram import types

animals_reply_kb = [[types.KeyboardButton(text='Кот'),
                      types.KeyboardButton(text='Собака')],
                      [types.KeyboardButton(text='Лиса')]]

animals_reply_keyboard = types.ReplyKeyboardMarkup(keyboard=animals_reply_kb, resize_keyboard=True)
