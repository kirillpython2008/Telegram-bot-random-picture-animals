from pars.pars_pic_animals import return_url_cat, return_url_dog, return_url_fox
from button.reply_button import animals_reply_keyboard

from aiogram import Dispatcher, types, F
from aiogram.filters import Command
from random import choice


async def start(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.first_name}\n"
                        "Нажмите на кнопку с названием животного, картинку которого хотите получить",
                        reply_markup=animals_reply_keyboard)
    

async def message_cat(message: types.Message):
    await message.answer_photo(return_url_cat(), caption=choice(["Вот ваше фото кота, как и просили",
                                                                 "Как и заказывали, фото кота",
                                                                 "Вот ваше фото кота, как и обещал"]))


async def message_dog(message: types.Message):
    await message.answer_photo(return_url_dog(), caption=choice(["Вот ваше фото собаки, как и просили",
                                                                 "Как и заказывали, фото собаки",
                                                                 "Вот ваше фото собаки, как и обещал"]))


async def message_fox(message: types.Message):
    await message.answer_photo(return_url_fox(), caption=choice(["Вот ваше фото лисы, как и просили",
                                                                 "Как и заказывали, фото лисы",
                                                                 "Вот ваше фото лисы, как и обещал"]))


def registration(dp: Dispatcher):
    dp.message.register(start, Command('start'))

    dp.message.register(message_cat, F.text == 'Кот')

    dp.message.register(message_dog, F.text == 'Собака')

    dp.message.register(message_fox, F.text == 'Лиса')
