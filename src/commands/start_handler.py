from src.config import dp, keyboard

from aiogram import types
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("start", ignore_case=True))
async def start_handler(message: types.Message):
    await message.answer("""
        Welcome to our to-do list Telegram Bot!
        /add - For creating task.
        /done - For marking task as done.
        /list - For showing a list of all tasks.
        /delete - For deleting a task from the list.
    """, reply_markup=keyboard.command_task)