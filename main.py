from handlers.user_handlers import registration

import asyncio
from aiogram import Bot, Dispatcher


async def main():
    bot = Bot(token='TOKEN')
    dp = Dispatcher()

    registration(dp=dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
