from src.config import dp, keyboard
from src.state import TaskIndexDone
from src.database import Task

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext


@dp.message_handler(Command("done", ignore_case=True))
async def create_handler(message: types.Message):
    await message.reply(
        "Enter task index..",
        reply_markup=keyboard.remove_keyboard
    )
    await TaskIndexDone.index.set()


@dp.message_handler(state=TaskIndexDone.index)
async def load_index(message: types.Message, state: FSMContext):
    index = message.text
    if not index.isdigit():
        await message.reply("Index have to contain only digits.")
        return

    task = await Task.get_or_none(id=int(index))

    if not task:
        await message.reply("Task not found.")
        return
    else:
        user = await task.user
        if user.uid != message.from_user.id:
            await message.reply("Method is not allowed.")
            return
        else:
            task.status = True
            await task.save()

    await message.reply("Task marked as done!", reply_markup=keyboard.command_task)
    await state.finish()