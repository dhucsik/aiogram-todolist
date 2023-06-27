from aiogram import executor

from commands import dp
from middleware import RegistrationMiddleware
from database import setup_db


async def on_startup(dispatcher):
    await setup_db()

    dp.middleware.setup(RegistrationMiddleware())


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)