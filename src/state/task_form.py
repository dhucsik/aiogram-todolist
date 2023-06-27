from aiogram.dispatcher.filters.state import State, StatesGroup


class TaskForm(StatesGroup):
    title = State()
    description = State()
