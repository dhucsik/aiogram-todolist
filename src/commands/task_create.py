from src.config import dp, keyboard
from src.state import TaskForm
from src.database import Task, User

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext


@dp.message_handler(Command("add", ignore_case=True))
async def create_handler(message: types.Message):
    await message.reply(
        "Enter task title..",
        reply_markup=keyboard.remove_keyboard
    )
    await TaskForm.title.set()


@dp.message_handler(state=TaskForm.title)
async def form_title(message: types.Message, state: FSMContext):
    if len(message.text) > 50:
        await message.reply("Title have to be no longer than 50 symbols.")
        return

    async with state.proxy() as data:
        data['title'] = message.text

    await message.reply(
        "The title was successfully set!\n"
        "Enter the description")
    await TaskForm.next()


@dp.message_handler(state=TaskForm.description)
async def form_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text

    user = await User.get(uid=message.from_user.id)
    task = Task(user=user, title=data['title'], description=data['description'], status=False)
    await task.save()

    await message.reply("Task created successfully!", reply_markup=keyboard.command_task)
    await state.finish()
