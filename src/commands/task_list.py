from src.config import dp, keyboard
from src.database import Task

from aiogram import types
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("list", ignore_case=True))
async def list_handler(message: types.Message):
    out = ""
    tasks = await Task.filter(user__uid=message.from_user.id)

    if not tasks:
        await message.answer("You don't have any tasks.")
        return

    for task in tasks:
        out += f"{task.id} | {task.title} | {task.print_status()}\n{task.description}\n"

    await message.answer(out, reply_markup=keyboard.command_task)
