from aiogram.dispatcher.filters.state import State, StatesGroup


class TaskIndexDone(StatesGroup):
    index = State()

class TaskIndexDelete(StatesGroup):
    index = State()

